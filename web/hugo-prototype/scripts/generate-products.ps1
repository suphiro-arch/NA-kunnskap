$ErrorActionPreference = 'Stop'

$outDir = 'web/hugo-prototype/content/ressursoversikt/produkter'
$registerFile = 'arkitektur/produkter/produktnummerering.md'
$mapFile = 'arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml'
$repoBlobBase = 'https://github.com/suphiro-arch/NA-kunnskap/blob/main'
$repoRoot = (Resolve-Path '.').Path
$registerBase = Split-Path -Parent (Join-Path $repoRoot $registerFile)

New-Item -ItemType Directory -Force -Path $outDir | Out-Null
$productCapabilityMap = Get-Content -Raw $mapFile -Encoding utf8 | ConvertFrom-Json

function Get-RepoRelativePath {
  param([string]$Path)

  $fullPath = [System.IO.Path]::GetFullPath($Path)
  if ($fullPath.StartsWith($repoRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
    return $fullPath.Substring($repoRoot.Length + 1).Replace('\', '/')
  }

  return $fullPath.Replace('\', '/')
}

function Get-RegisterEntries {
  $lines = Get-Content -Path $registerFile -Encoding utf8
  $entries = @()

  foreach ($line in $lines) {
    $trimmed = $line.Trim()
    if (-not $trimmed.StartsWith('|')) { continue }
    if ($trimmed -match '^\|\s*---') { continue }

    $cells = $trimmed.Trim('|').Split('|') | ForEach-Object { $_.Trim() }
    if ($cells.Count -lt 9) { continue }
    if ($cells[0] -notmatch '^\d+$') { continue }

    $documentCell = $cells[8]
    if (-not $documentCell -or $documentCell -eq '-') { continue }
    if ($documentCell -notmatch '\((?<path>[^)]+\.md)\)') { continue }

    $fullPath = [System.IO.Path]::GetFullPath((Join-Path $registerBase $Matches.path))
    if (-not (Test-Path -LiteralPath $fullPath)) { continue }

    $entries += [PSCustomObject]@{
      SortOrder = [int]$cells[0]
      ResourceId = $cells[1]
      Name = $cells[2]
      Category = $cells[3]
      ResourceType = $cells[4]
      VersionLabel = $cells[7]
      RelativePath = Get-RepoRelativePath -Path $fullPath
      FullPath = $fullPath
    }
  }

  return $entries | Sort-Object SortOrder
}

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
  }

  if ($parts.Count -eq 0) {
    return 'Kort beskrivelse er ikke oppgitt.'
  }

  $text = ($parts -join ' ') -replace '\s+', ' '
  return $text
}

function Shorten-OverviewDescription {
  param(
    [string]$Text,
    [int]$MaxLength = 320
  )

  if (-not $Text) {
    return 'Kort beskrivelse er ikke oppgitt.'
  }

  if ($Text.Length -le $MaxLength) {
    return $Text
  }

  $candidate = $Text.Substring(0, $MaxLength)
  $lastSpace = $candidate.LastIndexOf(' ')
  if ($lastSpace -gt 180) {
    $candidate = $candidate.Substring(0, $lastSpace)
  }

  return ($candidate.TrimEnd('.', ' ') + '...')
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

  foreach ($line in $Lines) {
    if ($line -match '^#\s+(.+?)\s*$') {
      return $Matches[1].Trim()
    }
  }

  return (($Fallback -replace '-', ' ').Trim())
}

function Extract-CapabilitiesFromSection {
  param([string[]]$Lines)

  $section = Extract-Section -Lines $Lines -Heading 'Kapabiliteter'
  $items = New-Object System.Collections.Generic.List[string]

  foreach ($line in $section) {
    $trim = $line.Trim()
    if (-not $trim) { continue }
    if (-not $trim.StartsWith('- ')) { continue }

    $clean = $trim.Substring(2).Trim()
    $clean = $clean -replace '\*\*', ''
    if ($clean) {
      $items.Add($clean)
    }
  }

  if ($items.Count -eq 0) {
    return 'Ikke koblet til kapabilitetssider ennaa.'
  }

  return ($items -join ' | ')
}

function Extract-CapabilityLinks {
  param(
    [string]$RelativePath,
    [string[]]$Lines
  )

  $links = New-Object System.Collections.Generic.List[string]
  $seen = @{}
  $productEntry = $productCapabilityMap.products |
    Where-Object { $_.relative_path -eq $RelativePath } |
    Select-Object -First 1

  if (-not $productEntry) {
    return (Extract-CapabilitiesFromSection -Lines $Lines)
  }

  foreach ($capability in $productEntry.capabilities) {
    if ($capability.subcapability_slug) {
      $key = "{0}/{1}" -f $capability.capability_slug, $capability.subcapability_slug
      if (-not $seen.ContainsKey($key)) {
        $links.Add(("[{0}](../../kapabiliteter/{1}/{2}/)" -f $capability.subcapability_name, $capability.capability_slug, $capability.subcapability_slug))
        $seen[$key] = $true
      }
      continue
    }

    $key = $capability.capability_slug
    if (-not $seen.ContainsKey($key)) {
      $links.Add(("[{0}](../../kapabiliteter/{1}/)" -f $capability.capability_name, $capability.capability_slug))
      $seen[$key] = $true
    }
  }

  if ($links.Count -eq 0) {
    return (Extract-CapabilitiesFromSection -Lines $Lines)
  }

  return ($links -join ' | ')
}

$latest = Get-RegisterEntries

$index = @(
  '---',
  'title: "Ressurser"',
  'weight: 31',
  'description: "Samlet oversikt over siste publiserte versjon av hver ressursbeskrivelse."',
  'hideToc: true',
  '---',
  '',
  '# Ressurser (siste versjon)',
  '',
  'Denne oversikten viser siste registrerte versjon per ressurs basert paa `arkitektur/produkter/produktnummerering.md`.',
  '',
  'Bruk siden for aa finne riktig ressursbeskrivelse raskt, og gaa derfra videre til detaljene i markdownfilen paa GitHub eller via relevante kapabilitetssider.',
  '',
  'Ressursene er presentert som egne oversiktsblokker, slik at kapabilitetene kan leses som en del av ressursens kontekst i stedet for som en smal tabellkolonne.'
)

foreach ($p in $latest) {
  $raw = Get-Content -Path $p.FullPath -Encoding utf8
  $displayName = Extract-DisplayName -Lines $raw -Fallback $p.Name
  $descriptionSection = Extract-Section -Lines $raw -Heading 'Kort beskrivelse'
  $shortDescription = Shorten-OverviewDescription -Text (Clean-ShortDescription -Section $descriptionSection)
  $capabilityLinks = Extract-CapabilityLinks -RelativePath $p.RelativePath -Lines $raw

  $blobUrl = ('{0}/{1}' -f $repoBlobBase, $p.RelativePath)

  $index += ''
  $index += ("## {0}" -f $displayName)
  $index += ''
  $index += ("**Ressurs-ID:** `{0}` | **Siste versjon:** `{1}` | [Markdown]({2})" -f $p.ResourceId, $p.VersionLabel, $blobUrl)
  $index += ''
  $index += ("**Kategori:** {0} | **Type:** {1}" -f $p.Category, $p.ResourceType)
  $index += ''
  $index += $shortDescription
  $index += ''
  $index += ("**Kapabiliteter:** {0}" -f $capabilityLinks)
  $index += ''
  $index += '---'
}

Set-Content -Path (Join-Path $outDir '_index.md') -Value $index -Encoding utf8

Get-ChildItem $outDir -File |
  Where-Object { $_.Name -ne '_index.md' } |
  Remove-Item -Force

Write-Output ("Genererte oversikt for ressurser: {0}" -f $latest.Count)
