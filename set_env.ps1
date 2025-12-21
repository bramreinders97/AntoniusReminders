param(
    [string]$EnvFile = ".env.antonius"
)

if (-not (Test-Path $EnvFile)) {
    Write-Error "Environment file '$EnvFile' not found!"
    exit 1
}

Write-Host "Loading environment from: $EnvFile"
get-content $EnvFile | foreach {
    $name, $value = $_.split('=')
    set-content env:\$name $value
}