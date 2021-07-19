from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email,  EqualTo

#flask_wtf: Libreria para la creación de formularios.
#Valida los datos para que no esten vacios ni sobrepaseen el N de espacios, también valida si es un email valido
#Equalto valida si las contrseñas coinciden
#Estas libreriria son usadas para la creación de formularios nos permiten procesarlo más rapido que en html
#vamos a crear nuestras clases y Objetos que  que luego se convertiran en html

#Declaramos la clase para el registro de usuario
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                                validators = [DataRequired(), Length (min = 2, max = 20)] ) 
    #usaremos el objeto y la variable de de Datarequired para realizar la validación  y length para validar longitud
    email = StringField('Email',     
                                validators = [DataRequired(), Email()])    
    password = PasswordField('Password',
                                validators = [DataRequired()])  
    confirm_password = PasswordField('Confirm password',
                                validators = [DataRequired(), EqualTo('password')])          
    submit =  SubmitField('Registrarse')

#Declaramos la clase del Login.
class LoginForm(FlaskForm):
    email = StringField('Email',     
                                validators = [DataRequired(), Email()])    
    password = PasswordField('Password',
                                validators = [DataRequired()])  
    # Creamos una variable booleana que recuerde el login mediante una cookie segura.
    remember = BooleanField('Remember Me')  
    submit =  SubmitField('Ingresar')

                                                                               




