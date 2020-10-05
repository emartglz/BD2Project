Instrucciones:

1- $ docker-compose up
para levanar el adminer y correr el gestor de base de datos

En otra consola

2- $ python3 create_db.py
para crear la base de datos

una vez dentro de la carpeta del proyecto
3- $ python3 manage.py migrate
para correr las migraciones

4- $ python3 manage.py createsuperuser
para crear el super user

5- $python3 manage.py runserver
para levantar el servidor

TO DO:
crear los grupos de permisos dentro de la primera migración
y ya..... creo