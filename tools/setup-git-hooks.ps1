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

# Ensure pre-commit exists.
$preCommit = Join-Path $hookPath 'pre-commit'
if (-not (Test-Path $preCommit)) {
  throw "Mangler hook-fil: $preCommit"
}

git config core.hooksPath $hookPath
Write-Host "Git hooksPath satt til: $hookPath"
Write-Host "Pre-commit hook aktivert."
