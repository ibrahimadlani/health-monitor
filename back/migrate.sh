#!/bin/bash

# Collecte des fichiers statiques (si nécessaire)
# /py/bin/python manage.py collectstatic --noinput

# Exécution des migrations
/py/bin/python manage.py makemigrations
/py/bin/python manage.py migrate --noinput

# Création du superutilisateur
/py/bin/python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()

# Vérification si le superutilisateur existe déjà
try:
    user = User.objects.get(email='$DJANGO_SUPERUSER_EMAIL')
except User.DoesNotExist:
    # Création du superutilisateur s'il n'existe pas
    User.objects.create_superuser(
        email='$DJANGO_SUPERUSER_EMAIL',
        username='$DJANGO_SUPERUSER_USERNAME',
        first_name='$DJANGO_SUPERUSER_FIRSTNAME',
        last_name='$DJANGO_SUPERUSER_LASTNAME',
        country_code='$DJANGO_SUPERUSER_COUNTRY_CODE',
        city='$DJANGO_SUPERUSER_CITY',
        password='$DJANGO_SUPERUSER_PASSWORD'
    )
else:
    # Mise à jour du superutilisateur s'il existe déjà
    user.username = '$DJANGO_SUPERUSER_USERNAME'
    user.first_name = '$DJANGO_SUPERUSER_FIRSTNAME'
    user.last_name = '$DJANGO_SUPERUSER_LASTNAME'
    user.country_code = '$DJANGO_SUPERUSER_COUNTRY_CODE'
    user.city = '$DJANGO_SUPERUSER_CITY'
    user.set_password('$DJANGO_SUPERUSER_PASSWORD')
    user.save()
END
