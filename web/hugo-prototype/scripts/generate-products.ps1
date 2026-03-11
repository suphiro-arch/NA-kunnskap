$ErrorActionPreference = 'Stop'

$srcDir = 'results/Produktbeskrivelser'
$outDir = 'web/hugo-prototype/content/ressursoversikt/produkter'
$repoBlobBase = 'https://github.com/suphiro-arch/NA-kunnskap/blob/main'
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$pattern = '^(?<id>\d+)-(?<name>.+)-produkt-canvas-v(?<ver>\d+)-(?<author>[^.]+)\.md$'
$items = @()

Get-ChildItem $srcDir -File | ForEach-Object {
  if ($_.Name -match $pattern) {
    $items += [PSCustomObject]@{
      Id = [int]$Matches.id
      Name = $Matches.name
      Version = [int]$Matches.ver
      Author = $Matches.author
      FileName = $_.Name
      RelativePath = "results/Produktbeskrivelser/$($_.Name)"
      FullPath = $_.FullName
    }
  }
}

$latest = $items |
  Group-Object Id |
  ForEach-Object {
    $_.Group | Sort-Object -Property Version, FileName -Descending | Select-Object -First 1
  } |
  Sort-Object Id

function Extract-Section {
  param(
    [string[]]$Lines,
    [string]$Heading
  )

  $start = -1
  for ($i = 0; $i -lt $Lines.Count; $i++) {
    if ($Lines[$i] -eq "## $Heading") {
      $start = $i + 1
      break
    }
  }
  if ($start -lt 0) { return @() }

  $end = $Lines.Count - 1
  for ($j = $start; $j -lt $Lines.Count; $j++) {
    if ($Lines[$j] -match '^##\s+') {
      $end = $j - 1
      break
    }
  }

  if ($end -lt $start) { return @() }
  return $Lines[$start..$end]
}

function Clean-ShortDescription {
  param([string[]]$Section)

  $parts = @()
  foreach ($line in $Section) {
    $trim = $line.Trim()
    if (-not $trim) { continue }
    if ($trim.StartsWith('- ')) { continue }
    if ($trim.StartsWith('Grunnlag:')) { continue }
    if ($trim.StartsWith('**Deduksjon:**')) { continue }
    if ($trim.StartsWith('**Fakta:**')) { continue }

    # Fjern enkel markdown-stil for ren tabelltekst.
    $clean = $trim -replace '\*\*', ''
    $parts += $clean

    # Hold beskrivelsen kort i oversikten.
    if (($parts -join ' ').Length -ge 260) { break }
  }

  if ($parts.Count -eq 0) {
    return 'Kort beskrivelse er ikke oppgitt.'
  }

  $text = ($parts -join ' ') -replace '\s+', ' '
  if ($text.Length -gt 220) {
    return ($text.Substring(0, 220).TrimEnd() + '...')
  }
  return $text
}

function To-Slug {
  param([string]$Name)

  $slug = $Name.ToLower()
  $slug = $slug -replace 'æ', 'ae'
  $slug = $slug -replace 'ø', 'o'
  $slug = $slug -replace 'å', 'a'
  $slug = $slug -replace '[^a-z0-9]+', '-'
  return $slug.Trim('-')
}

$index = @(
  '---',
  'title: "Produkter"',
  'weight: 31',
  '---',
  '',
  '# Produkter (siste versjon)',
  '',
  'Denne oversikten viser kun siste versjon per produkt.',
  '',
  '| Produkt | Siste versjon | Kort beskrivelse | Markdown |',
  '|---|---|---|---|'
)

foreach ($p in $latest) {
  $raw = Get-Content -Path $p.FullPath -Encoding utf8
  $descriptionSection = Extract-Section -Lines $raw -Heading 'Kort beskrivelse'
  $shortDescription = Clean-ShortDescription -Section $descriptionSection

  $blobUrl = ('{0}/{1}' -f $repoBlobBase, $p.RelativePath)
  $safeDescription = ($shortDescription -replace '\|', '/')

  $index += ('| {0} | v{1} ({2}) | {3} | [Fil]({4}) |' -f $p.Name, $p.Version, $p.Author, $safeDescription, $blobUrl)
}

Set-Content -Path (Join-Path $outDir '_index.md') -Value $index -Encoding utf8

# Fjern individuelle produktsider - vi beholder kun samlet oversikt.
Get-ChildItem $outDir -File |
  Where-Object { $_.Name -ne '_index.md' } |
  Remove-Item -Force

Write-Output ("Genererte oversikt for produkter: {0}" -f $latest.Count)
