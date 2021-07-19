from datetime import datetime
from cvbien import db #importamos la conexión a base de datos de nuestro modelo

#Importamos el modelo de la BD para el usuario y la class sera nuestra tabla de la BD

#Tabla usuario
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)#columna, valor atributo, clave.
    username = db.Column(db.String(20), unique=True, nullable=False) #columna, valor atributo, Valor.
    email = db.Column(db.String(120), unique=True, nullable=False)
    #vamos crear una imagén para el perfil de usuario, hash(20 caracteres) y una imagén por defecto
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False) # se ponen 60 por el algoritmo hashing
    posts = db.relationship('Post', backref='author', lazy=True) # lo que haces es una consulta para traer los post de la clase "Post" mediante una relación
    #creamos un metodo validado por el modulo __repr___ para presentar la salida de un programa o datos
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# Tabla de las publicaciones

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False) #titulo de la publicación
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) #Muestra la fecha y hora de la publiación.
    #datetime.utcnow nos trae la hora actual para mostrar en la publicación..
    content = db.Column(db.Text, nullable=False)#contenido de la publicación
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__ (self):
        return f"Post('{self.title}', '{self.date_posted}')"



