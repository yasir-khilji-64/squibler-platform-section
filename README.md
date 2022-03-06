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

### API Details
- Register: Navigate to `127.0.0.1:8000/auth/register` and register using email and password. Sample request/response flow is provided
```json
Request
{
	"email": "yasir@squibler.io",
	"password": "password123"
}
Response
{
	"id": 1,
	"email": "yasir@squibler.io",
	"gravatar_url": "https://www.gravatar.com/avatar/37a0d19eabbc84c31a8e7dc61bd214ac?s=400&d=identicon",
	"created_at": "2022-03-06T21:06:46.497482Z"
}
```
- Login: Navigate to `127.0.0.1:8000/auth/login` and login using email and password, Sample request/response flow is provided
```json
Request
{
	"email": "yasir@squibler.io",
	"password": "password123"
}
Response
{
	"email": "yasir@squibler.io",
	"gravatar_url": "https://www.gravatar.com/avatar/37a0d19eabbc84c31a8e7dc61bd214ac?s=400&d=identicon",
	"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0NjY0NzM4MiwiaWF0IjoxNjQ2NjA0MTgyLCJqdGkiOiJmYWI2MDcyYWFiNmI0MjlhOTc0MTg0OWRlZTkwZjFmNCIsInVzZXJfaWQiOjEsImF1ZCI6InNxdWlibGVyIiwiaXNzIjoic3F1aWJsZXIuaW8ifQ.8PNTI4yFCj26BIFaMXm0HqKMG3g83ihfGzCMNIfMoEY",
	"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ2NjA1MDgyLCJpYXQiOjE2NDY2MDQxODIsImp0aSI6IjIzNDhhMzg2YmI1NjRkYTc5MWM2NjA3NjQ4ZGI4NTNhIiwidXNlcl9pZCI6MSwiYXVkIjoic3F1aWJsZXIiLCJpc3MiOiJzcXVpYmxlci5pbyJ9.i0e-rPbLNXNrzqQ-a8hbbe-q-AmKvMzvyhekcj7TM_I"
}
```
- Token Refresh: After 15 minutes, the access token from login will be expired. To refresh access token, simply navigate to `127.0.0.1:8000/auth/token/refresh` and provide the refresh token from login. It will geberate new tokens, and previous tokens will be blacklisted. Sample request/response flow is provided
```json
Request
{
	"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0NjU5MTg5NSwiaWF0IjoxNjQ2NTA1NDk1LCJqdGkiOiJjZDE4ZDRiNWZmNjU0ZmRhYjkzZmQyZDFkZTYwZDA1NCIsInVzZXJfaWQiOjEsImlzcyI6InNxdWlibGVyLmlvIn0.RpbVt7OkFQmfwjbNF1BzJ8TN5bRL4GoA-NnUHvOPgr4"
}
Response
{
	"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ2NTA2NjI2LCJpYXQiOjE2NDY1MDU0OTUsImp0aSI6IjcyZjc2MmE0N2MyZDQ4ZWI5ZDliNjJjNTFlMGM1ODM4IiwidXNlcl9pZCI6MSwiaXNzIjoic3F1aWJsZXIuaW8ifQ.1xEoLKuurR_bHX2KKIQCQHL-3p9GzI45WWmlOZXCwio",
	"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0NjU5MjkwNiwiaWF0IjoxNjQ2NTA2NTA2LCJqdGkiOiI1N2ZlYTQ0NTM3N2E0N2UwYjgzYzA3ZjI0N2JhZmVlZiIsInVzZXJfaWQiOjEsImlzcyI6InNxdWlibGVyLmlvIn0.uxbFCmDvXEj6UwhtRKNlf7iSy2k5cLeybLvLbdH84Ck"
}
```
- Section get/post: Navigate to `127.0.0.1:8000/api/v1/sections/`, providing the access token in Header Authorization with prefix as **Bearer AccessToken**, you can access the API.
Sample JSON request/response is provided
```json
Request
{
  "title": "Intro"
}
Response
{
	"id": 1,
	"title": "Intro",
	"parent": null,
	"subsections": []
}
```
- Subsection get/post: Just like sections, subsections can also be access on `127.0.0.1:8000/api/v1/sections/`, providing the access token in Header Authorization with prefix as **Bearer AccessToken**.
Sample request creating new subsection for section `id: 1` is provided
```json
Request
{
  "title": "Intro to platform",
  "parent": 1
}
Response
{
  "id": 2,
  "title": "Intro to platform",
  "parent": 1,
  "subsections": []
}
```
- Sections get: After creating a handful of sections and subsections, the nested view can be viewed on `127.0.0.1:8000/api/v1/sections/`, providing the access token in Header Authorization with prefix as **Bearer AccessToken**. Sample request/response flow is provided
```json
Response
[
	{
		"id": 1,
		"title": "Intro",
		"parent": null,
		"subsections": [
			{
				"id": 2,
				"title": "Intro to platform",
				"parent": 1,
				"subsections": []
			}
		]
	}
]
```