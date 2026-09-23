# Amazon Python CI/CD Clone

A basic Amazon-inspired e-commerce web application built with Python Flask. The main purpose of this project is to demonstrate CI/CD for a Python application using GitHub Actions.

## Technology Stack

- Python 3.12
- Flask
- HTML5 / CSS3
- pytest
- SonarQube
- GitHub Actions
- AWS EC2
- Gunicorn
- Nginx

## Features

- Amazon-inspired home page
- Product listing
- Category filtering
- Product detail pages
- Basic cart page
- Health endpoint
- No database
- No authentication
- No payment integration

## Run locally

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux
source venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000`.

## Run tests

```bash
pytest -v
```

## CI/CD flow

```text
Developer
   |
   | git push
   v
GitHub
   |
   v
GitHub Actions
   |
   +--> Checkout
   +--> Setup Python
   +--> pip install
   +--> pytest
   +--> SonarQube
   +--> Build ZIP artifact
   |
   v
AWS EC2
   |
   +--> Python virtual environment
   +--> Gunicorn
   +--> Nginx
   |
   v
Live Flask Application
```

## GitHub Secrets for CD

Add these repository secrets:

- `EC2_HOST`
- `EC2_USER`
- `EC2_SSH_KEY`

For SonarQube:

- `SONAR_TOKEN`
- `SONAR_HOST_URL`

If the SonarQube secrets are not configured, the workflow skips the SonarQube scan and continues with the rest of CI.

## EC2

The workflow deploys the application to:

```text
/opt/amazon-python-cicd
```

Gunicorn listens on port `5000`. Nginx can proxy public HTTP traffic from port `80` to port `5000`.

> This is an educational Amazon-inspired clone. It is not affiliated with Amazon.
