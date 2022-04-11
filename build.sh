rm deployment.zip
. .venv/bin/activate
pip freeze > requirements.txt
python manage.py collectstatic --noinput
zip -r deployment.zip . -x "*git*" "*.venv*"