#!/bin/bash

./manage.py migrate
./manage.py collectstatic --no-input
./manage.py update_index

exec gunicorn KickIt.wsgi:application --config KickIt/wsgi/config.py
