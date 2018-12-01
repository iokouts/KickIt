#!/bin/bash

./manage.py migrate
./manage.py collectstatic --no-input

exec gunicorn KickIt.wsgi:application --config KickIt/wsgi/config.py
