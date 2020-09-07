#!/bin/bash
npm install
./manage.py migrate
./manage.py compress
./manage.py collectstatic --no-input
./manage.py update_index

exec gunicorn KickIt.wsgi:application --config KickIt/wsgi/config.py
