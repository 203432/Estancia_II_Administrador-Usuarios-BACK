
# \Si se requiere instalar otra libreria, haganlo y despues ejecuten el siguiente comando:

    pip freeze > requirements.txt

    Para que no cause conflictos y se sepan que librerias estan siendo ocupadas



# Instrucciones:

1. Clonar el repositorio

2. Crear su entorno virtual:
   `virtualenv .nombre`

3. Ejecutarlo con:
   `source carpeta/Scripts/activate`

4. Instalar dependencias:
   `pip install -r requirements.txt`

5. Ejecutar el proyecto:
   `python manage.py runserver`

## Instrucciones para poder conectar la base de datos

1. Tener postgreSQL 14 o superior

2. Crear una base de datos en Postgre (Nombre recomendado para el proyecto: Tuxmapa_AdministradorUsuarios)

3. Una vez clonado el repositorio y haber instalado las dependencias, crear un archivo .env

4. En el archivo .env poner las siguientes credenciales

`ENGINE = django.db.backends.postgresql_psycopg2`

`NAME= NombreDeLaBaseDeDatos`

`USER= UsuarioDePostgre`

`PASSWORD= `

`HOST=El host a utilizar `

`PORT= puerto a ocupar (El puerto default de postgre es 5432) `

5. Hacer migraciones de la base de datos:

   `python manage.py makemigrations`

   `python manage.py migrate`

