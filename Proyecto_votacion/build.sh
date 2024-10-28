#!/usr/bin/env bash
#exit on error
set -o errexit

#poetry install
cd Proyecto_votacion
pip install -r requirements.txt
python manage.py migrate
python manage.py makemigrations