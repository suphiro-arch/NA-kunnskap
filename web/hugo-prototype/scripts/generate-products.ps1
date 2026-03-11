$ErrorActionPreference = 'Stop'

$srcDir = 'results/Produktbeskrivelser'
$outDir = 'web/hugo-prototype/content/ressursoversikt/produkter'
$repoBlobBase = 'https://github.com/suphiro-arch/NA-kunnskap/blob/main'
$repoRawBase = 'https://raw.githubusercontent.com/suphiro-arch/NA-kunnskap/main'
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

function Clean-Status {
  param([string[]]$Section)
  $status = @()
  foreach ($line in $Section) {
    $trim = $line.Trim()
    if ($trim -and -not $trim.StartsWith('**Fakta:**') -and -not $trim.StartsWith('**Deduksjon:**')) {
      $status += $trim
    }
  }
  if ($status.Count -eq 0) { return 'Ikke oppgitt' }
  return ($status -join ' ')
}

function Extract-Capabilities {
  param([string[]]$Section)
  $caps = @()
  foreach ($line in $Section) {
    $trim = $line.Trim()
    if ($trim -match '^-\s+\*\*(.+?)\*\*') {
      $caps += $Matches[1]
    }
  }
  return $caps
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
  '| Produkt | Siste versjon | Status/livsfase | Produktside | Markdown |',
  '|---|---|---|---|---|'
)

$expected = @()
foreach ($p in $latest) {
  $raw = Get-Content -Path $p.FullPath -Encoding utf8
  $statusSection = Extract-Section -Lines $raw -Heading 'Status/Livsfase'
  $capSection = Extract-Section -Lines $raw -Heading 'Kapabiliteter'

  $status = Clean-Status -Section $statusSection
  $caps = Extract-Capabilities -Section $capSection

  $slugName = ($p.Name.ToLower() -replace '[^a-z0-9]+', '-').Trim('-')
  $slug = ('{0:D2}-{1}' -f $p.Id, $slugName)
  $expected += ($slug + '.md')

  $statusOneLine = ($status -replace '\|', '/')
  $blobUrl = ('{0}/{1}' -f $repoBlobBase, $p.RelativePath)
  $rawUrl = ('{0}/{1}' -f $repoRawBase, $p.RelativePath)

  $productLines = @(
    '---',
    ('title: "{0:D2} - {1}"' -f $p.Id, $p.Name),
    '---',
    '',
    ('# {0:D2} - {1}' -f $p.Id, $p.Name),
    '',
    '## Kilde for siste versjon',
    '',
    ('- Fil: `{0}`' -f $p.RelativePath),
    ('- Versjon: `v{0}`' -f $p.Version),
    ('- Opprettet av: `{0}`' -f $p.Author),
    '',
    '## Status/livsfase',
    '',
    ('{0}' -f $status),
    '',
    '## Kapabilitetsmapping',
    ''
  )

  if ($caps.Count -gt 0) {
    foreach ($c in $caps) {
      $productLines += ('- {0}' -f $c)
    }
  } else {
    $productLines += '- Ikke oppgitt i kildedokumentet.'
  }

  $productLines += ''
  $productLines += '## Lenke til kildedokument'
  $productLines += ''
  $productLines += ('- [Aapne markdown pa GitHub]({0})' -f $blobUrl)
  $productLines += ('- [Aapne raw markdown]({0})' -f $rawUrl)

  Set-Content -Path (Join-Path $outDir ($slug + '.md')) -Value $productLines -Encoding utf8

  $index += ('| {0} | v{1} ({2}) | {3} | [{0}](/ressursoversikt/produkter/{4}/) | [Fil]({5}) |' -f $p.Name, $p.Version, $p.Author, $statusOneLine, $slug, $blobUrl)
}

Set-Content -Path (Join-Path $outDir '_index.md') -Value $index -Encoding utf8

Get-ChildItem $outDir -File |
  Where-Object { $_.Name -ne '_index.md' -and $expected -notcontains $_.Name } |
  Remove-Item -Force

Write-Output ("Generated pages: {0}" -f $latest.Count)
