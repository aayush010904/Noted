# Noted

A simple Django note-taking app with authentication, personal notes, and tags.

## Features

- User signup, login, and logout
- Create, read, update, and delete personal notes
- Notes are private to each logged-in user
- Tag notes with comma-separated tags
- Search notes by title, body text, or tag
- Filter notes by a selected tag

## Tech Stack

- Python
- Django 6
- SQLite (default database)

## Quick Start

1. Clone the repository and move into the project folder.
2. Create and activate a virtual environment.
3. Install dependencies.
4. Run migrations.
5. Start the development server.

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open the app at:

- http://127.0.0.1:8000/

## Main Routes

- `/` - home page
- `/signup/` - create an account
- `/login/` - log in
- `/logout/` - log out
- `/smart/notes/` - list notes
- `/smart/notes/new` - create a note
- `/smart/notes/<id>` - view note details
- `/smart/notes/<id>/edit` - edit note
- `/smart/notes/<id>/delete` - delete note

## Project Structure

- `home/` - auth and landing views/templates
- `notes/` - notes, tags, forms, and CRUD views
- `noted/` - Django project settings and root URLs
- `templates/` - shared base template
- `static/` - global CSS

## Notes

- This project uses Django's development server and settings.
- Do not use `DEBUG=True` configuration in production.
