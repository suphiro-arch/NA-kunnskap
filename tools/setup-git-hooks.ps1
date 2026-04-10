param(
  [string]$RepoRoot = '.'
)

$ErrorActionPreference = 'Stop'

$root = (Resolve-Path $RepoRoot).Path
Set-Location $root

$hookPath = '.githooks'
if (-not (Test-Path $hookPath)) {
  New-Item -ItemType Directory -Path $hookPath | Out-Null
}

# Ensure required hook files exist.
$requiredHooks = @('pre-commit', 'pre-push')
foreach ($hookName in $requiredHooks) {
  $hookFile = Join-Path $hookPath $hookName
  if (-not (Test-Path $hookFile)) {
    throw "Mangler hook-fil: $hookFile"
  }
}

git config core.hooksPath $hookPath
Write-Host "Git hooksPath satt til: $hookPath"
Write-Host "Pre-commit og pre-push hooks aktivert."
