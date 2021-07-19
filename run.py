from cvbien import app # de la ruta app importe la variable app.
# La iniciación de la app siempre debe ir al final para que todo corra adicional a esto si se deja dentro de la ruta principal.-
# se le agrega el debug= True para que el server funcione de manera corrida. 
if __name__ == "__main__":
    app.run(port=3000, debug=True)

    #este archivo se crea indepediente fuera del paquete para que unicamente sea correr este archivo y corrar toda la appy llamda __main___