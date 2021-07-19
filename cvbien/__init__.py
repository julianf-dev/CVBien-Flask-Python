from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

#flask: Microframerwork

#Iniciar la app en una variable variable para importar en el run 
app = Flask(__name__)
#creamos nuestra clave secreta 
app.config['SECRET_KEY'] = '4daec0cd600bc07b8320d21d8a82c75b'
#configuraremos la ruta y el archivo donde se va a guardar la base de datos.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
#Instanciamos nuestra BD
db = SQLAlchemy(app)


#importamos nuestras rutas después de iniciar la pepe para no hacer un circulo de importación(llamar dos veces)
from cvbien import routes