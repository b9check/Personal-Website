# Brian Check - Personal Website

A personal portfolio website showcasing engineering and software projects.

**Live site:** [briancheck.net](https://www.briancheck.net)

## Tech Stack

- **Backend:** Django 5.1 (Python 3.12)
- **Web Server:** nginx (reverse proxy)
- **Application Server:** gunicorn (WSGI)
- **Database:** SQLite
- **Hosting:** AWS EC2

## Project Structure

```
personalsite/
├── main/                    # Main Django app
│   ├── static/              # Source static files (CSS, images, videos)
│   ├── templates/           # HTML templates
│   ├── views.py             # View functions
│   └── urls.py              # URL routing
├── personalsite/            # Django project settings
│   ├── settings.py
│   └── urls.py
├── staticfiles/             # Collected static files (served by nginx)
├── venv/                    # Python virtual environment
└── manage.py
```

## Local Development

```bash
cd personalsite
python -m venv venv
source venv/bin/activate
pip install django gunicorn
python manage.py runserver
```

## Deployment

After making changes:

```bash
# Collect static files
cd personalsite
source venv/bin/activate
python manage.py collectstatic --noinput

# Restart the application server
sudo systemctl restart gunicorn
```

## Features

- Dark theme with modern UI
- Hero video background on home page
- Mobile-responsive hamburger navigation
- Project portfolio with categorized sections (Software & Robotics, Mechanical)
- SSL/HTTPS via Let's Encrypt
