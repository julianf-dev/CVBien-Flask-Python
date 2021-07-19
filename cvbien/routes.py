from cvbien import app
from flask import render_template, redirect, url_for, flash 
from cvbien.forms import RegistrationForm, LoginForm
from cvbien.models import User, Post
#Importamos del paquete cvbien la app para usarlar en el  @app.
#Render_template: Renderizar los html en los metodos def.
#Flask_msqldb: Liberiria de mySQL(Base de datos) (flask_sqlalchemy)
#redirect: Redirege el html. 
#Flash se encarga de mostrar los mensajes. 
#URI:  identificador de recursos uniforme
#importamos de cvbien.forms los formularios para apregarlos a las rutas.
#importamos de cvbien.models las clases de user y post

#Creamos un diccionario de datos  almacenado en post para mostrar publicaciónes "Ficiticas" en la página de inicio.

posts = [
    {
        'author': 'Julián Franco',
        'title': 'Blog post 1',
        'content': 'First post content ',
        'data_posted': 'Mayo 06 2019'
    },
    {
        'author': 'Andrés Miranda',
        'title': 'Blog post 2',
        'content': 'Second post content ',
        'data_posted': 'Mayo 06, 2019'
    }
] 
#cada funcion será un html.
 #el (/) nos va a indicar la ruta principal para luego renderizarla con el html.
@app.route("/")
def home():
    return render_template('home.html', posts = posts ) #llamamos la variable posts 
                                                        #declarada anteriormente para usarla en el html

#el (/about) nos va a idicar la ruta para luego renderizarla con el html.
@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register', methods = ['GET','POST'] ) #Registramos el metodo porque estamos enviando un POST en el formulario.
def register():
    #instanciamos nuestro objeto
    form = RegistrationForm()
    if form.validate_on_submit(): #Se valida el formulario    
        flash(f'Cuenta creada para {form.username.data}!', 'success') #muestra un mensaje de exito al momento de crear un nuevo usuario
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Registro', form=form)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'pass':
            flash('Has iniciado sesión', 'success')
            return redirect(url_for('home')) ## retorna a la ruta después de que el log in es exitoso
        else: 
            flash('Ingreso incorrecto. Por favor verifica tu email y contraseña', 'danger') 
            #el danger es la clase de bootstrap que sirve para el que el aviso se de de color rojo
    return render_template('Login.html', title = 'Inicio de Sesión', form=form)