$ErrorActionPreference = 'Stop'

$srcDir = 'results/Produktbeskrivelser'
$outDir = 'web/hugo-prototype/content/ressursoversikt/produkter'
$repoBlobBase = 'https://github.com/suphiro-arch/NA-kunnskap/blob/main'
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$patternCurrent = '^(?<id>\d+)-(?<name>.+)-produkt-canvas-v(?<ver>\d+)-(?<author>[^.]+)\.md$'
$patternNoAuthor = '^(?<id>\d+)-(?<name>.+)-produkt-canvas-v(?<ver>\d+)\.md$'
$patternLegacy = '^(?<id>\d+)-(?<name>.+)-produkt-canvas(?:-(?<author>[^.]+))?\.md$'
$items = @()

Get-ChildItem $srcDir -File | ForEach-Object {
  if ($_.Name -match $patternCurrent) {
    $items += [PSCustomObject]@{
      Id = [int]$Matches.id
      Name = $Matches.name
      Version = [int]$Matches.ver
      Author = $Matches.author
      FileName = $_.Name
      RelativePath = "results/Produktbeskrivelser/$($_.Name)"
      FullPath = $_.FullName
      LastWriteTime = $_.LastWriteTime
      IsLegacy = $false
    }
  }
  elseif ($_.Name -match $patternNoAuthor) {
    $items += [PSCustomObject]@{
      Id = [int]$Matches.id
      Name = $Matches.name
      Version = [int]$Matches.ver
      Author = 'ukjent'
      FileName = $_.Name
      RelativePath = "results/Produktbeskrivelser/$($_.Name)"
      FullPath = $_.FullName
      LastWriteTime = $_.LastWriteTime
      IsLegacy = $false
    }
  }
  elseif ($_.Name -match $patternLegacy) {
    $items += [PSCustomObject]@{
      Id = [int]$Matches.id
      Name = $Matches.name
      Version = 0
      Author = $(if ($Matches.author) { $Matches.author } else { 'legacy' })
      FileName = $_.Name
      RelativePath = "results/Produktbeskrivelser/$($_.Name)"
      FullPath = $_.FullName
      LastWriteTime = $_.LastWriteTime
      IsLegacy = $true
    }
  }
}

$latest = $items |
  Group-Object Id |
  ForEach-Object {
    $_.Group |
      Sort-Object -Property @{ Expression = 'Version'; Descending = $true }, @{ Expression = 'LastWriteTime'; Descending = $true }, @{ Expression = 'FileName'; Descending = $true } |
      Select-Object -First 1
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

    $clean = $trim -replace '\*\*', ''
    $parts += $clean

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

function Extract-DisplayName {
  param(
    [string[]]$Lines,
    [string]$Fallback
  )

  $section = Extract-Section -Lines $Lines -Heading 'Navn'
  foreach ($line in $section) {
    $trim = $line.Trim()
    if ($trim) {
      return $trim
    }
  }

  return (($Fallback -replace '-', ' ').Trim())
}

$index = @(
  '---',
  'title: "Produkter"',
  'weight: 31',
  '---',
  '',
  '# Produkter (siste versjon)',
  '',
  'Denne oversikten viser siste versjon per produkt basert på høyeste versjonsnummer.',
  '',
  '| Produkt | Siste versjon | Kort beskrivelse | Markdown |',
  '|---|---|---|---|'
)

foreach ($p in $latest) {
  $raw = Get-Content -Path $p.FullPath -Encoding utf8
  $displayName = Extract-DisplayName -Lines $raw -Fallback $p.Name
  $descriptionSection = Extract-Section -Lines $raw -Heading 'Kort beskrivelse'
  $shortDescription = Clean-ShortDescription -Section $descriptionSection

  $blobUrl = ('{0}/{1}' -f $repoBlobBase, $p.RelativePath)
  $safeDescription = ($shortDescription -replace '\|', '/')
  $versionLabel = if ($p.Version -gt 0) { "v$($p.Version)" } else { 'legacy' }
  $authorLabel = if ($p.Author) { $p.Author } else { 'ukjent' }

  $index += ('| {0} | {1} ({2}) | {3} | [Fil]({4}) |' -f $displayName, $versionLabel, $authorLabel, $safeDescription, $blobUrl)
}

Set-Content -Path (Join-Path $outDir '_index.md') -Value $index -Encoding utf8

Get-ChildItem $outDir -File |
  Where-Object { $_.Name -ne '_index.md' } |
  Remove-Item -Force

Write-Output ("Genererte oversikt for produkter: {0}" -f $latest.Count)
