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

  return (($Fallback -replace '-', ' ').Trim())
}

function Convert-ToSlug {
  param([string]$Value)

  $slug = $Value.Trim().ToLowerInvariant()
  $slug = $slug.Replace('æ', 'ae').Replace('ø', 'o').Replace('å', 'a')
  $slug = $slug -replace '[^a-z0-9]+', '-'
  return $slug.Trim('-')
}

function Resolve-CapabilitySlug {
  param([string]$Value)

  $slug = Convert-ToSlug $Value
  $aliases = @{
    'datautveksling' = 'datautveksling-og-integrasjon'
    'samhandling' = 'samarbeid'
    'informasjonsstyring' = 'informasjonsforvaltning'
    'informasjonssikkerheit' = 'informasjonssikkerhet'
  }

  if ($aliases.ContainsKey($slug)) {
    return $aliases[$slug]
  }

  return $slug
}

function Extract-CapabilityLinks {
  param([string[]]$Section)

  $links = New-Object System.Collections.Generic.List[string]
  $seen = @{}
  $capabilityRoot = 'web/hugo-prototype/content/kapabiliteter'

  foreach ($line in $Section) {
    $trim = $line.Trim()
    if ($trim -notmatch '^- ') { continue }
    if ($trim -notmatch '^\-\s+\*\*(.+?)\*\*') { continue }

    $label = $Matches[1].Trim()
    $parts = ($label -split ':', 2) | ForEach-Object { $_.Trim() }

    if ($parts.Count -eq 2 -and $parts[1]) {
      $mainSlug = Resolve-CapabilitySlug $parts[0]
      $subSlug = Convert-ToSlug $parts[1]
      $targetDir = Join-Path $capabilityRoot (Join-Path $mainSlug $subSlug)
      if (Test-Path $targetDir) {
        $key = "$mainSlug/$subSlug"
        if (-not $seen.ContainsKey($key)) {
          $links.Add(("[{0}](../../kapabiliteter/{1}/{2}/)" -f $parts[1], $mainSlug, $subSlug))
          $seen[$key] = $true
        }
        continue
      }
    }

    $mainSlugOnly = Resolve-CapabilitySlug $parts[0]
    $mainDir = Join-Path $capabilityRoot $mainSlugOnly
    if (Test-Path $mainDir) {
      $key = $mainSlugOnly
      if (-not $seen.ContainsKey($key)) {
        $links.Add(("[{0}](../../kapabiliteter/{1}/)" -f $parts[0], $mainSlugOnly))
        $seen[$key] = $true
      }
      continue
    }

    $subSlugOnly = Convert-ToSlug $parts[0]
    $subMatch = Get-ChildItem -Directory -Recurse $capabilityRoot |
      Where-Object { $_.Name -eq $subSlugOnly } |
      Select-Object -First 1
    if ($subMatch) {
      $relative = $subMatch.FullName.Substring((Resolve-Path $capabilityRoot).Path.Length).TrimStart('\') -replace '\\', '/'
      $key = $relative
      if (-not $seen.ContainsKey($key)) {
        $links.Add(("[{0}](../../kapabiliteter/{1}/)" -f $parts[0], $relative))
        $seen[$key] = $true
      }
      continue
    }

    if (-not $seen.ContainsKey($label)) {
      $links.Add($label)
      $seen[$label] = $true
    }
  }

  if ($links.Count -eq 0) {
    return 'Ikke koblet til kapabilitetssider ennå.'
  }

  return ($links -join ' · ')
}

$index = @(
  '---',
  'title: "Produkter"',
  'weight: 31',
  'description: "Samlet oversikt over siste publiserte versjon av hver produktbeskrivelse."',
  'hideToc: true',
  '---',
  '',
  '# Produkter (siste versjon)',
  '',
  'Denne oversikten viser siste versjon per produkt basert på høyeste versjonsnummer.',
  '',
  'Bruk siden for å finne riktig produktbeskrivelse raskt, og gå derfra videre til detaljene i markdownfilen på GitHub eller via relevante kapabilitetssider.',
  '',
  'Produktene er presentert som egne oversiktsblokker, slik at kapabilitetene kan leses som en del av produktets kontekst i stedet for som en smal tabellkolonne.'
)

foreach ($p in $latest) {
  $raw = Get-Content -Path $p.FullPath -Encoding utf8
  $displayName = Extract-DisplayName -Lines $raw -Fallback $p.Name
  $descriptionSection = Extract-Section -Lines $raw -Heading 'Kort beskrivelse'
  $capabilitySection = Extract-Section -Lines $raw -Heading 'Kapabiliteter'
  $shortDescription = Shorten-OverviewDescription -Text (Clean-ShortDescription -Section $descriptionSection)
  $capabilityLinks = Extract-CapabilityLinks -Section $capabilitySection

  $blobUrl = ('{0}/{1}' -f $repoBlobBase, $p.RelativePath)
  $versionLabel = if ($p.Version -gt 0) { "v$($p.Version)" } else { 'legacy' }
  $authorLabel = if ($p.Author) { $p.Author } else { 'ukjent' }

  $index += ''
  $index += ("## {0}" -f $displayName)
  $index += ''
  $index += ("**Siste versjon:** `{0} ({1})` · [Markdown]({2})" -f $versionLabel, $authorLabel, $blobUrl)
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

Write-Output ("Genererte oversikt for produkter: {0}" -f $latest.Count)
