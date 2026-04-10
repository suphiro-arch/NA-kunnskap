$ErrorActionPreference = 'Stop'

$outDirRel = 'web/hugo-prototype/content/ressursoversikt/produkter'
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
    Title = 'Operative løsninger og tjenester'
    Description = 'Ressurser som brukes direkte i drift, integrasjon eller løsningsdesign.'
    Weight = 1
  },
  [PSCustomObject]@{
    Slug = 'normerende-ressurser'
    Title = 'Normerende ressurser'
    Description = 'Ressurser som primært gir føringer for modeller, standarder, arkitektur og samordning.'
    Weight = 2
  },
  [PSCustomObject]@{
    Slug = 'samarbeidsfora'
    Title = 'Samarbeidsfora'
    Description = 'Arenaer for koordinering, prioritering og samordning på tvers av aktører.'
    Weight = 3
  },
  [PSCustomObject]@{
    Slug = 'andre-ressurser'
    Title = 'Andre ressurser'
    Description = 'Ressurser som foreløpig ikke er plassert i egen ressursmappe med tydelig hovedtype.'
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
    if ($cells.Count -lt 9) { continue }
    if ($cells[0] -notmatch '^\d+$') { continue }

    $documentCell = $cells[8]
    if (-not $documentCell -or $documentCell -eq '-') { continue }
    if ($documentCell -notmatch '\((?<path>[^)]+\.md)\)') { continue }

    $fullPath = [System.IO.Path]::GetFullPath((Join-Path $registerBase $Matches.path))
    if (-not (Test-Path -LiteralPath $fullPath)) { continue }

    $entries += [PSCustomObject]@{
      SortOrder = [int]$cells[0]
      ResourceId = ($cells[1] -replace '`', '').Trim()
      Name = ($cells[2] -replace '`', '').Trim()
      Category = ($cells[3] -replace '`', '').Trim()
      ResourceType = ($cells[4] -replace '`', '').Trim()
      VersionLabel = ($cells[7] -replace '`', '').Trim()
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

  return $resourceTypeDefinitions | Where-Object { $_.Slug -eq 'andre-ressurser' } | Select-Object -First 1
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
    [string[]]$Lines
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
        $url = "../../kapabiliteter/$($capability.capability_slug)/$($capability.subcapability_slug)/"
        $key = "$($capability.capability_slug)/$($capability.subcapability_slug)"
      } else {
        $label = $capability.capability_name
        $url = "../../kapabiliteter/$($capability.capability_slug)/"
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
    $parts += ("<span class=`"capability-chip capability-chip--more`">+{0}</span>" -f $remaining)
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
    [string]$SectionSlug
  )

  $cardLines = New-Object System.Collections.Generic.List[string]
  $ownerSet = New-Object System.Collections.Generic.HashSet[string]
  $typeSet = New-Object System.Collections.Generic.HashSet[string]
  $capabilitySet = New-Object System.Collections.Generic.HashSet[string]

  foreach ($p in $Entries) {
    $raw = Get-Content -Path $p.FullPath -Encoding utf8
    $displayName = Extract-DisplayName -Lines $raw -Fallback $p.Name
    $descriptionSection = Extract-Section -Lines $raw -Heading 'Kort beskrivelse'
    $shortDescription = Shorten-OverviewDescription -Text (Clean-ShortDescription -Section $descriptionSection)
    $owner = Extract-OwnerFromResourceId -ResourceId $p.ResourceId
    $purposeLine = Extract-PurposeLine -Lines $raw
    $primaryDocUrl = Extract-PrimaryDocumentationLink -Lines $raw
    $capabilityItems = @(Get-CapabilityItems -RelativePath $p.RelativePath -Lines $raw)

    [void]$ownerSet.Add($owner)
    [void]$typeSet.Add($p.ResourceType)
    foreach ($capability in $capabilityItems) {
      if ($capability.Label) {
        [void]$capabilitySet.Add($capability.Label)
      }
    }

    $blobUrl = ('{0}/{1}' -f $repoBlobBase, $p.RelativePath)
    $capabilityHtml = Render-CapabilityChips -Items $capabilityItems -MaxVisible 3
    $capabilitySearch = ($capabilityItems | ForEach-Object { $_.Label }) -join ' '
    $searchable = ($displayName + ' ' + $p.ResourceId + ' ' + $owner + ' ' + $p.Category + ' ' + $p.ResourceType + ' ' + $shortDescription + ' ' + $capabilitySearch).ToLowerInvariant()

    $cardLines.Add('<article class="resource-card" ' +
      ('data-owner="{0}" ' -f (Html-Encode $owner)) +
      ('data-type="{0}" ' -f (Html-Encode $p.ResourceType)) +
      ('data-capabilities="{0}" ' -f (Html-Encode ($capabilitySearch.ToLowerInvariant()))) +
      ('data-search="{0}">' -f (Html-Encode $searchable)))
    $cardLines.Add(('  <h2 class="resource-card__title">{0}</h2>' -f (Html-Encode $displayName)))
    $cardLines.Add(('  <p class="resource-card__meta"><strong>Ressurs-ID:</strong> <code>{0}</code> | <strong>Siste versjon:</strong> {1}</p>' -f (Html-Encode $p.ResourceId), (Html-Encode $p.VersionLabel)))
    $cardLines.Add(('  <p class="resource-card__facts"><strong>Eier:</strong> {0} | <strong>Kategori:</strong> {1} | <strong>Type:</strong> {2}</p>' -f (Html-Encode $owner), (Html-Encode $p.Category), (Html-Encode $p.ResourceType)))
    $cardLines.Add(('  <p class="resource-card__description">{0}</p>' -f (Html-Encode $shortDescription)))
    if ($purposeLine) {
      $cardLines.Add(('  <p class="resource-card__purpose"><strong>Formaal/mandat:</strong> {0}</p>' -f (Html-Encode $purposeLine)))
    }
    $cardLines.Add(('  <p class="resource-card__capabilities"><strong>Kapabiliteter:</strong> {0}</p>' -f $capabilityHtml))
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

  $lines = New-Object System.Collections.Generic.List[string]
  $lines.Add(('<div class="resource-listing" data-section="{0}">' -f (Slugify-Value $SectionSlug)))
  $lines.Add('  <div class="resource-filters">')
  $lines.Add('    <div class="resource-filters__row">')
  $lines.Add('      <label>Sok <input type="search" class="resource-filter" data-filter="search" placeholder="Navn, ID, type, kapabilitet" /></label>')
  $lines.Add('      <label>Eier <select class="resource-filter" data-filter="owner"><option value="">Alle</option>')
  foreach ($option in $ownerOptions) {
    $lines.Add(('        <option value="{0}">{1}</option>' -f (Html-Encode $option), (Html-Encode $option)))
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
  $lines.Add('      function norm(v){ return (v || "").toLowerCase(); }')
  $lines.Add('      function apply(){')
  $lines.Add('        var q = norm(search && search.value);')
  $lines.Add('        var o = norm(owner && owner.value);')
  $lines.Add('        var t = norm(type && type.value);')
  $lines.Add('        var c = norm(capability && capability.value);')
  $lines.Add('        var visible = 0;')
  $lines.Add('        cards.forEach(function(card){')
  $lines.Add('          var ok = true;')
  $lines.Add('          if (q && card.dataset.search.indexOf(q) === -1) ok = false;')
  $lines.Add('          if (o && norm(card.dataset.owner) !== o) ok = false;')
  $lines.Add('          if (t && norm(card.dataset.type) !== t) ok = false;')
  $lines.Add('          if (c && norm(card.dataset.capabilities).indexOf(c) === -1) ok = false;')
  $lines.Add('          card.style.display = ok ? "block" : "none";')
  $lines.Add('          if (ok) visible += 1;')
  $lines.Add('        });')
  $lines.Add('        if (count) { count.textContent = "Viser " + visible + " av " + cards.length + " ressurser"; }')
  $lines.Add('      }')
  $lines.Add('      [search, owner, type, capability].forEach(function(el){ if (el) { el.addEventListener("input", apply); el.addEventListener("change", apply); } });')
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
  '# Ressurser (siste versjon)',
  '',
  'Denne oversikten viser siste registrerte versjon per ressurs basert paa `arkitektur/ressurser/produktnummerering.md`.',
  '',
  'Bruk siden for aa finne riktig ressursbeskrivelse raskt, og gaa derfra videre til detaljene i markdownfilen paa GitHub eller via relevante kapabilitetssider.',
  '',
  'Ressursene er gruppert etter hovedtype, med egne undersider for operative løsninger og tjenester, normerende ressurser og samarbeidsfora.'
)

foreach ($typeDef in $resourceTypeDefinitions) {
  $typeEntries = @($latest | Where-Object { $_.ResourceTypeSlug -eq $typeDef.Slug })
  if ($typeEntries.Count -eq 0) { continue }

  $index += ''
  $index += ("## [{0}](./{1}/)" -f $typeDef.Title, $typeDef.Slug)
  $index += ''
  $index += $typeDef.Description
  $index += ''
  $index += ("Antall ressurser: **{0}**" -f $typeEntries.Count)
}

foreach ($typeDef in $resourceTypeDefinitions) {
  $typeEntries = @($latest | Where-Object { $_.ResourceTypeSlug -eq $typeDef.Slug })
  if ($typeEntries.Count -eq 0) { continue }

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
    ('# {0}' -f $typeDef.Title),
    '',
    $typeDef.Description,
    '',
    ('Denne siden viser siste registrerte versjon av ressurser i kategorien **{0}**.' -f $typeDef.Title)
  )

  $typeIndex += ''
  $typeIndex += (New-ResourceListingBlock -Entries $typeEntries -SectionSlug $typeDef.Slug)

  Write-Utf8NoBomFile -Path (Join-Path $typeDir '_index.md') -Lines $typeIndex
}

Write-Utf8NoBomFile -Path (Join-Path $outDir '_index.md') -Lines $index

$topLevelOverviewFile = Join-Path $repoRoot 'web/hugo-prototype/content/ressursoversikt/_index.md'
$allResourcesIndex = @(
  '---',
  'title: "Ressursoversikt"',
  'weight: 30',
  'description: "Inngang til produktbeskrivelser og andre felles ressurser som understøtter kapabilitetene i modellen."',
  'hideToc: true',
  'hideSectionOverview: true',
  '---',
  '',
  '# Ressursoversikt',
  '',
  'Denne siden viser samlet oversikt over siste registrerte versjon per ressurs basert paa `arkitektur/ressurser/produktnummerering.md`.',
  '',
  'Bruk filtrene for aa finne riktige ressurser raskt paa tvers av typer, eiere og kapabiliteter.',
  '',
  '## Undersider',
  '',
  '- [Operative løsninger og tjenester](produkter/operative-losninger-og-tjenester/)',
  '- [Normerende ressurser](produkter/normerende-ressurser/)',
  '- [Samarbeidsfora](produkter/samarbeidsfora/)',
  '',
  '## Ressurser (siste versjon)',
  ''
)
$allResourcesIndex += (New-ResourceListingBlock -Entries @($latest) -SectionSlug 'alle-ressurser')
Write-Utf8NoBomFile -Path $topLevelOverviewFile -Lines $allResourcesIndex

Get-ChildItem $outDir -File |
  Where-Object { $_.Name -ne '_index.md' } |
  Remove-Item -Force

Write-Output ("Genererte oversikt for ressurser: {0}" -f $latest.Count)


