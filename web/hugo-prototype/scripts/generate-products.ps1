$ErrorActionPreference = 'Stop'

$outDirRel = 'web/hugo-prototype/content/ressursoversikt/ressurser'
$registerFileRel = 'arkitektur/ressurser/produktnummerering.md'
$mapFileRel = 'arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml'
$repoBlobBase = 'https://github.com/suphiro-arch/NA-kunnskap/blob/main'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$outDir = Join-Path $repoRoot $outDirRel
$registerFile = Join-Path $repoRoot $registerFileRel
$mapFile = Join-Path $repoRoot $mapFileRel
$registerBase = Split-Path -Parent $registerFile
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$resourceTypeDefinitions = @(
  [PSCustomObject]@{
    Slug = 'operative-losninger-og-tjenester'
    Title = 'Gjenbrukbare løsninger'
    Description = 'Tekniske komponenter, applikasjoner og tjenester som leverer funksjonalitet eller dataprodukter som kan brukes av flere.'
    Weight = 1
  },
  [PSCustomObject]@{
    Slug = 'normerende-ressurser'
    Title = 'Standarder og veiledning'
    Description = 'Ressurser som setter regler eller gir retning, som standarder, veiledere, referansearkitekturer og metodikk.'
    Weight = 2
  },
  [PSCustomObject]@{
    Slug = 'samarbeidsfora'
    Title = 'Samhandlingsarenaer og organisering'
    Description = 'Organiserte nettverk og styringsorganer for dialog, strategisk samarbeid og samordning.'
    Weight = 3
  },
  [PSCustomObject]@{
    Slug = 'rammer-og-virkemidler'
    Title = 'Økonomiske og juridiske rammer og virkemidler'
    Description = 'Finansielle og regulative virkemidler som muliggjør gjennomføring og setter handlingsrom.'
    Weight = 4
  }
)

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
    if ($cells.Count -lt 6) { continue }
    if ($cells[0] -notmatch '^\d+$') { continue }

    $documentCell = $null
    for ($idx = $cells.Count - 1; $idx -ge 0; $idx--) {
      if ($cells[$idx] -match '\((?<path>[^)]+\.md)\)') {
        $documentCell = $cells[$idx]
        break
      }
    }
    if (-not $documentCell -or $documentCell -eq '-') { continue }
    if ($documentCell -notmatch '\((?<path>[^)]+\.md)\)') { continue }

    $docRelativePath = [Uri]::UnescapeDataString($Matches.path)
    $fullPath = [System.IO.Path]::GetFullPath((Join-Path $registerBase $docRelativePath))
    if (-not (Test-Path -LiteralPath $fullPath)) { continue }

    $resourceId = ''
    $name = ''
    $category = 'Ikke oppgitt'
    $resourceType = ''
    $versionLabel = ''

    if ($cells.Count -ge 9) {
      # Legacy table format.
      $resourceId = ($cells[1] -replace '`', '').Trim()
      $name = ($cells[2] -replace '`', '').Trim()
      $category = ($cells[3] -replace '`', '').Trim()
      $resourceType = ($cells[4] -replace '`', '').Trim()
      $versionLabel = ($cells[7] -replace '`', '').Trim()
    } else {
      # Current table format: Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument
      $resourceId = ($cells[1] -replace '`', '').Trim()
      $name = ($cells[2] -replace '`', '').Trim()
      $resourceType = ($cells[3] -replace '`', '').Trim()
      $category = ($cells[4] -replace '`', '').Trim()
    }

    if (-not $versionLabel) {
      $fileName = [System.IO.Path]::GetFileName($fullPath)
      if ($fileName -match '-(v\d+)-([a-z0-9]+)\.md$') {
        $versionLabel = "$($Matches[1]) ($($Matches[2]))"
      } elseif ($fileName -match '-(v\d+)\.md$') {
        $versionLabel = $Matches[1]
      } else {
        $versionLabel = 'Ukjent'
      }
    }

    $entries += [PSCustomObject]@{
      SortOrder = [int]$cells[0]
      ResourceId = $resourceId
      Name = $name
      Category = $category
      ResourceType = $resourceType
      VersionLabel = $versionLabel
      RelativePath = Get-RepoRelativePath -Path $fullPath
      FullPath = $fullPath
    }
  }

  return $entries | Sort-Object SortOrder
}

function Write-Utf8NoBomFile {
  param(
    [string]$Path,
    [string[]]$Lines
  )

  $content = [string]::Join([Environment]::NewLine, $Lines)
  [System.IO.File]::WriteAllText($Path, $content, $utf8NoBom)
}

function Get-ResourceTypeInfo {
  param([string]$RelativePath)

  if ($RelativePath -match '^arkitektur/ressurser/operative-losninger-og-tjenester/') {
    return $resourceTypeDefinitions | Where-Object { $_.Slug -eq 'operative-losninger-og-tjenester' } | Select-Object -First 1
  }

  if ($RelativePath -match '^arkitektur/ressurser/normerende-ressurser/') {
    return $resourceTypeDefinitions | Where-Object { $_.Slug -eq 'normerende-ressurser' } | Select-Object -First 1
  }

  if ($RelativePath -match '^arkitektur/ressurser/samarbeidsfora/') {
    return $resourceTypeDefinitions | Where-Object { $_.Slug -eq 'samarbeidsfora' } | Select-Object -First 1
  }

  if ($RelativePath -match '^arkitektur/ressurser/rammer-og-virkemidler/') {
    return $resourceTypeDefinitions | Where-Object { $_.Slug -eq 'rammer-og-virkemidler' } | Select-Object -First 1
  }

  throw "Uklassifisert ressurssti uten rammeverkskategori: $RelativePath"
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

function Html-Encode {
  param([string]$Text)
  if ($null -eq $Text) { return '' }
  return [System.Net.WebUtility]::HtmlEncode($Text)
}

function Slugify-Value {
  param([string]$Text)

  if ($null -eq $Text) { $Text = '' }
  $value = $Text.ToLowerInvariant().Trim()
  if (-not $value) { return '' }

  $normalized = $value.Normalize([Text.NormalizationForm]::FormD)
  $sb = New-Object System.Text.StringBuilder
  foreach ($ch in $normalized.ToCharArray()) {
    $unicodeCategory = [Globalization.CharUnicodeInfo]::GetUnicodeCategory($ch)
    if ($unicodeCategory -ne [Globalization.UnicodeCategory]::NonSpacingMark) {
      [void]$sb.Append($ch)
    }
  }

  $clean = $sb.ToString().Normalize([Text.NormalizationForm]::FormC)
  $clean = $clean -replace '[^a-z0-9]+', '-'
  $clean = $clean.Trim('-')
  return $clean
}

function Extract-OwnerFromResourceId {
  param([string]$ResourceId)

  if ($ResourceId -match '^([A-Z0-9]+)-') {
    return $Matches[1]
  }

  return 'UKJENT'
}

function Get-OwnerDisplayName {
  param([string]$OwnerCode)

  $ownerMap = @{
    'DIGDIR' = 'Digdir'
    'KS'     = 'KS Digital'
    'NHN'    = 'Norsk helsenett'
    'NAV'    = 'NAV'
    'SKATT'  = 'Skatteetaten'
    'KART'   = 'Kartverket'
    'BRREG'  = 'Brønnøysundregistrene'
    'SIKT'   = 'Sikt'
    'HDIR'   = 'Helsedirektoratet'
    'HELFO'  = 'Helfo'
    'SSB'    = 'SSB'
    'SVV'    = 'Statens vegvesen'
    'NOVARI' = 'Novari'
    'FHI'    = 'FHI'
    'OPP'    = 'OpenPeppol'
    'FLERE'  = 'Flere virksomheter'
  }

  if ([string]::IsNullOrWhiteSpace($OwnerCode)) {
    return ''
  }

  if ($ownerMap.ContainsKey($OwnerCode)) {
    return $ownerMap[$OwnerCode]
  }

  return $OwnerCode
}

function Extract-CapabilityItemsFromSection {
  param([string[]]$Lines)

  $section = Extract-Section -Lines $Lines -Heading 'Kapabiliteter'
  $items = New-Object System.Collections.Generic.List[object]

  foreach ($line in $section) {
    $trim = $line.Trim()
    if (-not $trim) { continue }
    if (-not $trim.StartsWith('- ')) { continue }

    $clean = $trim.Substring(2).Trim() -replace '\*\*', ''
    if ($clean) {
      $items.Add([PSCustomObject]@{ Label = $clean; Url = '' })
    }
  }

  return $items.ToArray()
}

function Get-CapabilityItems {
  param(
    [string]$RelativePath,
    [string[]]$Lines,
    [string]$CapabilityLinkPrefix = '../../../'
  )

  $items = New-Object System.Collections.Generic.List[object]
  $seen = @{}

  $productEntry = $productCapabilityMap.products |
    Where-Object { $_.relative_path -eq $RelativePath } |
    Select-Object -First 1

  if ($productEntry) {
    foreach ($capability in $productEntry.capabilities) {
      $label = ''
      $url = ''
      $key = ''

      if ($capability.subcapability_slug) {
        $label = $capability.subcapability_name
        $url = "$($CapabilityLinkPrefix)kapabiliteter/$($capability.capability_slug)/$($capability.subcapability_slug)/"
        $key = "$($capability.capability_slug)/$($capability.subcapability_slug)"
      } else {
        $label = $capability.capability_name
        $url = "$($CapabilityLinkPrefix)kapabiliteter/$($capability.capability_slug)/"
        $key = $capability.capability_slug
      }

      if (-not $label) { continue }
      if ($seen.ContainsKey($key)) { continue }

      $items.Add([PSCustomObject]@{ Label = $label; Url = $url })
      $seen[$key] = $true
    }
  }

  if ($items.Count -gt 0) {
    return $items.ToArray()
  }

  return (Extract-CapabilityItemsFromSection -Lines $Lines)
}

function Render-CapabilityChips {
  param(
    [object[]]$Items,
    [int]$MaxVisible = 3
  )

  if (-not $Items -or $Items.Count -eq 0) {
    return '<span class="capability-chip capability-chip--empty">Ikke koblet</span>'
  }

  $parts = @()
  $visibleCount = [Math]::Min($Items.Count, $MaxVisible)
  for ($i = 0; $i -lt $visibleCount; $i++) {
    $item = $Items[$i]
    $label = Html-Encode $item.Label
    if ($item.Url) {
      $parts += ("<a class=`"capability-chip`" href=`"{0}`">{1}</a>" -f $item.Url, $label)
    } else {
      $parts += ("<span class=`"capability-chip`">{0}</span>" -f $label)
    }
  }

  if ($Items.Count -gt $MaxVisible) {
    $remaining = $Items.Count - $MaxVisible

    $hiddenParts = @()
    for ($i = $MaxVisible; $i -lt $Items.Count; $i++) {
      $item = $Items[$i]
      $label = Html-Encode $item.Label
      if ($item.Url) {
        $hiddenParts += ("<a class=`"capability-chip`" href=`"{0}`">{1}</a>" -f $item.Url, $label)
      } else {
        $hiddenParts += ("<span class=`"capability-chip`">{0}</span>" -f $label)
      }
    }

    $parts += ("<details class=`"capability-chip-disclosure`"><summary class=`"capability-chip capability-chip--more`" title=`"Vis/skjul flere kapabiliteter`">+{0}</summary><span class=`"capability-chip-disclosure__items`"> {1}</span></details>" -f $remaining, ($hiddenParts -join ' '))
  }

  return ($parts -join ' ')
}

function Extract-StatusLabel {
  param(
    [string[]]$Lines,
    [string]$Fallback
  )

  $section = Extract-Section -Lines $Lines -Heading 'Status/Livsfase'
  foreach ($line in $section) {
    $trim = ($line -replace '\*\*', '').Trim()
    if (-not $trim) { continue }
    if ($trim.StartsWith('- ')) { continue }
    return $trim
  }

  return $Fallback
}

function Extract-PurposeLine {
  param([string[]]$Lines)

  $sections = @('Mandat og rolle', 'Formaal og normerende rolle', 'Formål og normerende rolle')
  foreach ($heading in $sections) {
    $section = Extract-Section -Lines $Lines -Heading $heading
    foreach ($line in $section) {
      $trim = ($line -replace '\*\*', '').Trim()
      if (-not $trim) { continue }
      if ($trim.StartsWith('- ')) { continue }
      return (Shorten-OverviewDescription -Text $trim -MaxLength 200)
    }
  }

  return ''
}

function Extract-PrimaryDocumentationLink {
  param([string[]]$Lines)

  $section = Extract-Section -Lines $Lines -Heading 'Lenke til dokumentasjon'
  foreach ($line in $section) {
    $trim = $line.Trim()
    if ($trim -match 'https?://\S+') {
      return $Matches[0].TrimEnd(')', '.', ',')
    }
  }

  return ''
}

function New-ResourceListingBlock {
  param(
    [object[]]$Entries,
    [string]$SectionSlug,
    [string]$CapabilityLinkPrefix = '../../../'
  )

  $cardLines = New-Object System.Collections.Generic.List[string]
  $ownerSet = New-Object System.Collections.Generic.HashSet[string]
  $typeSet = New-Object System.Collections.Generic.HashSet[string]
  $capabilitySet = New-Object System.Collections.Generic.HashSet[string]
  $topicSet = New-Object System.Collections.Generic.HashSet[string]

  foreach ($p in $Entries) {
    $raw = Get-Content -Path $p.FullPath -Encoding utf8
    $displayName = Extract-DisplayName -Lines $raw -Fallback $p.Name
    $descriptionSection = Extract-Section -Lines $raw -Heading 'Kort beskrivelse'
    $shortDescription = Shorten-OverviewDescription -Text (Clean-ShortDescription -Section $descriptionSection)
    $owner = Extract-OwnerFromResourceId -ResourceId $p.ResourceId
    $ownerDisplay = Get-OwnerDisplayName -OwnerCode $owner
    $purposeLine = Extract-PurposeLine -Lines $raw
    $primaryDocUrl = Extract-PrimaryDocumentationLink -Lines $raw
    $capabilityItems = @(Get-CapabilityItems -RelativePath $p.RelativePath -Lines $raw -CapabilityLinkPrefix $CapabilityLinkPrefix)

    [void]$ownerSet.Add($owner)
    [void]$typeSet.Add($p.ResourceType)
    $topic = ''
    if ($p.Category) { $topic = ([string]$p.Category).Trim() }
    if ($topic) { [void]$topicSet.Add($topic) }
    foreach ($capability in $capabilityItems) {
      if ($capability.Label) {
        [void]$capabilitySet.Add($capability.Label)
      }
    }

    $blobUrl = ('{0}/{1}' -f $repoBlobBase, $p.RelativePath)
    $capabilityHtml = Render-CapabilityChips -Items $capabilityItems -MaxVisible 3
    $capabilitySearch = ($capabilityItems | ForEach-Object { $_.Label }) -join ' '
    $searchable = ($displayName + ' ' + $p.ResourceId + ' ' + $owner + ' ' + $ownerDisplay + ' ' + $p.ResourceTypeTitle + ' ' + $p.ResourceType + ' ' + $shortDescription + ' ' + $capabilitySearch + ' ' + $topic).ToLowerInvariant()

    $cardLines.Add('<article class="resource-card" ' +
      ('data-owner="{0}" ' -f (Html-Encode $owner)) +
      ('data-type="{0}" ' -f (Html-Encode $p.ResourceType)) +
      ('data-capabilities="{0}" ' -f (Html-Encode ($capabilitySearch.ToLowerInvariant()))) +
      ('data-emne="{0}" ' -f (Html-Encode $topic)) +
      ('data-search="{0}">' -f (Html-Encode $searchable)))
    $cardLines.Add(('  <h2 class="resource-card__title">{0}</h2>' -f (Html-Encode $displayName)))
    $cardLines.Add(('  <p class="resource-card__meta"><strong>Ressurs-ID:</strong> <code>{0}</code> | <strong>Siste versjon:</strong> {1}</p>' -f (Html-Encode $p.ResourceId), (Html-Encode $p.VersionLabel)))
    $cardLines.Add(('  <p class="resource-card__facts"><strong>Eier:</strong> {0} | <strong>Type:</strong> {1}</p>' -f (Html-Encode $ownerDisplay), (Html-Encode $p.ResourceTypeTitle)))
    $cardLines.Add(('  <p class="resource-card__description">{0}</p>' -f (Html-Encode $shortDescription)))
    if ($purposeLine) {
      $cardLines.Add(('  <p class="resource-card__purpose"><strong>Formaal/mandat:</strong> {0}</p>' -f (Html-Encode $purposeLine)))
    }
    $cardLines.Add(('  <div class="resource-card__capabilities"><strong>Kapabiliteter:</strong> {0}</div>' -f $capabilityHtml))
    $actions = New-Object System.Collections.Generic.List[string]
    $actions.Add(('<a class="resource-card__button resource-card__button--primary" href="{0}">Full beskrivelse (md-fil)</a>' -f (Html-Encode $blobUrl)))
    if ($primaryDocUrl) {
      $actions.Add(('<a class="resource-card__button resource-card__button--ghost" href="{0}">Offisiell lenke</a>' -f (Html-Encode $primaryDocUrl)))
    }
    $cardLines.Add(('  <p class="resource-card__actions">{0}</p>' -f ($actions -join ' ')))
    $cardLines.Add('</article>')
  }

  $ownerOptions = @($ownerSet | Sort-Object)
  $typeOptions = @($typeSet | Sort-Object)
  $capabilityOptions = @($capabilitySet | Sort-Object)
  $topicOptions = @($topicSet | Sort-Object)

  $lines = New-Object System.Collections.Generic.List[string]
  $lines.Add(('<div class="resource-listing" data-section="{0}">' -f (Slugify-Value $SectionSlug)))
  $lines.Add('  <div class="resource-filters">')
  $lines.Add('    <div class="resource-filters__row">')
  $lines.Add('      <label>Søk <input type="search" class="resource-filter" data-filter="search" placeholder="Navn, ID, kapabilitet" /></label>')
  $lines.Add('      <label>Eier <select class="resource-filter" data-filter="owner"><option value="">Alle</option>')
  foreach ($option in $ownerOptions) {
    $lines.Add(('        <option value="{0}">{1}</option>' -f (Html-Encode $option), (Html-Encode (Get-OwnerDisplayName -OwnerCode $option))))
  }
  $lines.Add('      </select></label>')
  $lines.Add('      <label>Type <select class="resource-filter" data-filter="type"><option value="">Alle</option>')
  foreach ($option in $typeOptions) {
    $lines.Add(('        <option value="{0}">{1}</option>' -f (Html-Encode $option), (Html-Encode $option)))
  }
  $lines.Add('      </select></label>')
  $lines.Add('      <label>Kapabilitet <select class="resource-filter" data-filter="capability"><option value="">Alle</option>')
  foreach ($option in $capabilityOptions) {
    $lines.Add(('        <option value="{0}">{1}</option>' -f (Html-Encode $option), (Html-Encode $option)))
  }
  $lines.Add('      </select></label>')
  if ($topicOptions.Count -gt 0) {
    $lines.Add('      <label>Emne <select class="resource-filter" data-filter="emne"><option value="">Alle</option>')
    foreach ($option in $topicOptions) {
      $lines.Add(('        <option value="{0}">{1}</option>' -f (Html-Encode $option), (Html-Encode $option)))
    }
    $lines.Add('      </select></label>')
  }
  $lines.Add('    </div>')
  $lines.Add(('    <p class="resource-filters__result" data-role="count">Viser {0} av {0} ressurser</p>' -f $Entries.Count))
  $lines.Add('  </div>')
  $lines.Add('  <div class="resource-cards">')
  foreach ($line in $cardLines) { $lines.Add($line) }
  $lines.Add('  </div>')
  $lines.Add('  <script>')
  $lines.Add('    (function(){')
  $lines.Add('      var root = document.currentScript.closest(".resource-listing");')
  $lines.Add('      if (!root) { return; }')
  $lines.Add('      var cards = Array.prototype.slice.call(root.querySelectorAll(".resource-card"));')
  $lines.Add('      var count = root.querySelector("[data-role=count]");')
  $lines.Add('      var search = root.querySelector("[data-filter=search]");')
  $lines.Add('      var owner = root.querySelector("[data-filter=owner]");')
  $lines.Add('      var type = root.querySelector("[data-filter=type]");')
  $lines.Add('      var capability = root.querySelector("[data-filter=capability]");')
  $lines.Add('      var emne = root.querySelector("[data-filter=emne]");')
  $lines.Add('      function norm(v){ return (v || "").toLowerCase(); }')
  $lines.Add('      function apply(){')
  $lines.Add('        var q = norm(search && search.value);')
  $lines.Add('        var o = norm(owner && owner.value);')
  $lines.Add('        var t = norm(type && type.value);')
  $lines.Add('        var c = norm(capability && capability.value);')
  $lines.Add('        var e = norm(emne && emne.value);')
  $lines.Add('        var visible = 0;')
  $lines.Add('        cards.forEach(function(card){')
  $lines.Add('          var ok = true;')
  $lines.Add('          if (q && card.dataset.search.indexOf(q) === -1) ok = false;')
  $lines.Add('          if (o && norm(card.dataset.owner) !== o) ok = false;')
  $lines.Add('          if (t && norm(card.dataset.type) !== t) ok = false;')
  $lines.Add('          if (c && norm(card.dataset.capabilities).indexOf(c) === -1) ok = false;')
  $lines.Add('          if (e && norm(card.dataset.emne) !== e) ok = false;')
  $lines.Add('          card.style.display = ok ? "block" : "none";')
  $lines.Add('          if (ok) visible += 1;')
  $lines.Add('        });')
  $lines.Add('        if (count) { count.textContent = "Viser " + visible + " av " + cards.length + " ressurser"; }')
  $lines.Add('      }')
  $lines.Add('      [search, owner, type, capability, emne].forEach(function(el){ if (el) { el.addEventListener("input", apply); el.addEventListener("change", apply); } });')
  $lines.Add('      apply();')
  $lines.Add('    })();')
  $lines.Add('  </script>')
  $lines.Add('</div>')

  return $lines.ToArray()
}

$latest = Get-RegisterEntries

foreach ($entry in $latest) {
  $typeInfo = Get-ResourceTypeInfo -RelativePath $entry.RelativePath
  Add-Member -InputObject $entry -NotePropertyName ResourceTypeSlug -NotePropertyValue $typeInfo.Slug
  Add-Member -InputObject $entry -NotePropertyName ResourceTypeTitle -NotePropertyValue $typeInfo.Title
  Add-Member -InputObject $entry -NotePropertyName ResourceTypeDescription -NotePropertyValue $typeInfo.Description
}

$index = @(
  '---',
  'title: "Ressurser"',
  'weight: 31',
  'description: "Samlet oversikt over siste publiserte versjon av hver ressursbeskrivelse."',
  'hideInNav: true',
  'hideToc: true',
  '---',
  '',
  'Denne oversikten viser siste registrerte versjon per ressurs, gruppert etter rammeverkskategori.'
)

foreach ($typeDef in $resourceTypeDefinitions) {
  $typeEntries = @($latest | Where-Object { $_.ResourceTypeSlug -eq $typeDef.Slug })
  $index += ''
  $index += ("## [{0}](./{1}/)" -f $typeDef.Title, $typeDef.Slug)
  $index += ''
  $index += $typeDef.Description
  $index += ''
  $index += ("Antall ressurser: **{0}**" -f $typeEntries.Count)
}

foreach ($typeDef in $resourceTypeDefinitions) {
  $typeEntries = @($latest | Where-Object { $_.ResourceTypeSlug -eq $typeDef.Slug })
  $typeDir = Join-Path $outDir $typeDef.Slug
  New-Item -ItemType Directory -Force -Path $typeDir | Out-Null

  $typeIndex = @(
    '---',
    ('title: "{0}"' -f $typeDef.Title),
    ('weight: {0}' -f $typeDef.Weight),
    ('description: "{0}"' -f $typeDef.Description),
    'hideToc: true',
    '---',
    '',
    ('Denne siden viser siste registrerte versjon av ressurser i kategorien **{0}**.' -f $typeDef.Title)
  )

  $typeIndex += ''
  $typeIndex += (New-ResourceListingBlock -Entries $typeEntries -SectionSlug $typeDef.Slug -CapabilityLinkPrefix '../../../')

  Write-Utf8NoBomFile -Path (Join-Path $typeDir '_index.md') -Lines $typeIndex
}

Write-Utf8NoBomFile -Path (Join-Path $outDir '_index.md') -Lines $index

$topLevelOverviewFile = Join-Path $repoRoot 'web/hugo-prototype/content/ressursoversikt/_index.md'
$resourceTypeCardLines = New-Object System.Collections.Generic.List[string]
$resourceTypeCardLines.Add('<div class="resource-type-grid">')
foreach ($typeDef in $resourceTypeDefinitions) {
  $typeEntries = @($latest | Where-Object { $_.ResourceTypeSlug -eq $typeDef.Slug })
  $resourceTypeCardLines.Add('  <article class="resource-type-card">')
  $resourceTypeCardLines.Add(('    <h3><a href="ressurser/{0}/">{1}</a></h3>' -f $typeDef.Slug, $typeDef.Title))
  $resourceTypeCardLines.Add(('    <p>{0}</p>' -f $typeDef.Description))
  $resourceTypeCardLines.Add(('    <p class="resource-type-card__count">{0} ressurser</p>' -f $typeEntries.Count))
  $resourceTypeCardLines.Add('  </article>')
}
$resourceTypeCardLines.Add('</div>')

$allResourcesIndex = @(
  '---',
  'title: "Ressursoversikt"',
  'weight: 30',
  'description: "Inngang til ressursbeskrivelser som understøtter kapabilitetene i modellen."',
  'eyebrow: "Under arbeid"',
  'hideToc: true',
  'hideSectionOverview: true',
  '---',
  '',
  '## Utforsk per type',
  '',
  ($resourceTypeCardLines -join [Environment]::NewLine),
  '',
  '## Ressursliste',
  ''
)
$allResourcesIndex += (New-ResourceListingBlock -Entries @($latest) -SectionSlug 'alle-ressurser' -CapabilityLinkPrefix '../')
Write-Utf8NoBomFile -Path $topLevelOverviewFile -Lines $allResourcesIndex

$validTypeSlugs = @($resourceTypeDefinitions | ForEach-Object { $_.Slug })
Get-ChildItem $outDir -Directory |
  Where-Object { $validTypeSlugs -notcontains $_.Name } |
  Remove-Item -Recurse -Force

Get-ChildItem $outDir -File |
  Where-Object { $_.Name -ne '_index.md' } |
  Remove-Item -Force

Write-Output ("Genererte oversikt for ressurser: {0}" -f $latest.Count)
