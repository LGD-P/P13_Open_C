#!/bin/bash
poetry run python3 manage.py migrate
# poetry run python3 manage.py runserver 0.0.0.0:8000
poetry run gunicorn core.wsgi:oc_lettings_site --bind 0.0.0.0:8000
