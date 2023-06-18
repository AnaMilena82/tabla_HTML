from flask import Flask, render_template, url_for  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"


@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def index():
    users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
    return render_template("tabla.html", users = users)  


@app.route('/<path:path>') #Asegúrate de que si el usuario escribe cualquier ruta distinta a las especificadas, reciba un mensaje de error que diga "¡Lo siento! No hay respuesta. Inténtalo otra vez.”.
def error(path):
    return '¡Lo siento! No hay respuesta. Inténtalo otra vez.'

    






if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

