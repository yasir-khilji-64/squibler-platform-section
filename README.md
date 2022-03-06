# Squibler Platform Sections
Assessment for squibler.io for backend engineer using Python Django

## Dev Environment
- Python: 3.6+ (used 3.9)
- Django + DRF
- PyTest
- Sqlite3
- Github Actions

## Script for Local Setup
- Copy sample env to env and change env variables: `cp .env.sample .env`
- Create Virtual Environment: `python -m venv env`
- Activate Virtual Environment
  - Windows (Powershell): `.\env\Scripts\Activate.ps1`
  - Linux: `source env/bin/activate`
- Install Dependencies: python -m pip install -r requirements.txt`
- Migrations: `python manage.py migrate`
- Test: `pytest`
- Run dev server: `python manage.py runserver`

## Stretch Goals
- Can use email verification and password reset.
- Can use MySQL or Postgresql for production
- Can use docker for hassle free develpoment.