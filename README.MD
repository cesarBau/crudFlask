## Crear el entorno virtual
```
py -3 -m venv venv
```
## Activar el entorno virtual
```
. venv/Scripts/activate
```
## Librerias dependientes
```
pip install Flask
pip install -U flask-cors
pip install pymongo
```
## Ejecutar
```
export FLASK_APP=main.py
export FLASK_ENV=development
export MONGO_URI='mongodb://localhost:27017/catalogdb'
flask run
```