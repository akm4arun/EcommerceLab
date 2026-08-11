Write-Host "Running database migrations..."
flask db upgrade

Write-Host "Starting application..."
flask run