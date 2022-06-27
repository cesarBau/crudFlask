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
pip install Flask-PyMongo
pip install "pymongo[srv]"
```
## Variables de entorno
```
export FLASK_APP=main.py
export FLASK_ENV=development
export MONGO_URI='mongodb://localhost:27017/note'
export HOST=0.0.0.0
export PORT=3000
```
## Ejecutar
```
python main.py
```