param(
  [string]$Root = '.',
  [switch]$StagedOnly
)

$ErrorActionPreference = 'Stop'

$patterns = @(
  [string]([char]0x00C3),
  [string]([char]0x00C2),
  [string]([char]0x00E2),
  [string]([char]0xFFFD)
)
$extensions = @('.md', '.yaml', '.yml', '.toml', '.html', '.json', '.txt')

function Get-TargetFiles {
  param([string]$Base, [bool]$OnlyStaged)

  if ($OnlyStaged) {
    $staged = git diff --cached --name-only
    return $staged |
      Where-Object { $_ } |
      Where-Object { $extensions -contains [System.IO.Path]::GetExtension($_).ToLowerInvariant() } |
      ForEach-Object { Join-Path $Base $_ } |
      Where-Object { Test-Path $_ }
  }

  return Get-ChildItem -Path $Base -Recurse -File |
    Where-Object {
      $extensions -contains $_.Extension.ToLowerInvariant() -and
      $_.FullName -notmatch '[\\/](\.git|node_modules|\.venv|venv)[\\/]'
    } |
    Select-Object -ExpandProperty FullName
}

$repoRoot = (Resolve-Path $Root).Path
$files = Get-TargetFiles -Base $repoRoot -OnlyStaged:$StagedOnly
$findings = @()

foreach ($file in $files) {
  $text = [System.IO.File]::ReadAllText($file, [System.Text.Encoding]::UTF8)
  $lines = $text -split "`r?`n"
  for ($i = 0; $i -lt $lines.Count; $i++) {
    foreach ($p in $patterns) {
      if ($lines[$i].Contains($p)) {
        $rel = $file.Replace($repoRoot + [System.IO.Path]::DirectorySeparatorChar, '')
        $findings += "{0}:{1}: {2}" -f $rel, ($i + 1), $lines[$i].Trim()
        break
      }
    }
  }
}

if ($findings.Count -eq 0) {
  Write-Host "OK: Ingen mistenkelige mojibake-sekvenser funnet."
  exit 0
}

Write-Host "FEIL: Fant mistenkelige mojibake-sekvenser:"
$findings | Select-Object -First 200 | ForEach-Object { Write-Host $_ }
if ($findings.Count -gt 200) {
  Write-Host "... og $($findings.Count - 200) flere linjer"
}
exit 1
