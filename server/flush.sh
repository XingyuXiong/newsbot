#! /bin/bash
python manage.py flush --noinput
python manage.py loaddata initdata.json