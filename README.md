# EcommerceLab

Flask-based ecommerce application built with Bootstrap and prepared for Azure App Service deployment.

## Features

* User registration and login
* Product catalog
* Product search
* Sorting and pagination
* Shopping cart
* Order placement
* Admin dashboard
* Order status management
* Customer order history

## Local Development

### Create virtual environment

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Application URL:

```
http://127.0.0.1:5000
```

## Health Check

```
http://127.0.0.1:5000/health
```

Expected response:

```json
{"status": "ok"}
```

## Production Startup

```bash
gunicorn --bind=0.0.0.0:8000 app:app
```

## Environment Variables

Create a `.env` file for local development:

```ini
APP_NAME=EcommerceLab
APP_VERSION=1.0.0
FLASK_ENV=development
SECRET_KEY=local-dev-secret-key
```

## Azure App Service

Startup command:

```bash
bash startup.sh
```

App settings to configure in Azure:

* `SECRET_KEY`
* `FLASK_ENV=production`
* `APP_NAME`
* `APP_VERSION`

## Git Workflow

* `main` → production releases
* `develop` → integration branch
* `feature/*` → feature development

Example:

```bash
git checkout develop
git checkout -b feature/new-feature
git add .
git commit -m "feat: add new feature"
git checkout develop
git merge --no-ff feature/new-feature
```

## License

Learning project for DevOps and Azure deployment practice.
