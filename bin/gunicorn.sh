#!/bin/bash

./manage.py migrate

exec gunicorn KickIt.wsgi:application --config KickIt/wsgi/config.py
