from flask import Flask, request, render_template
from clases.classes import Libros
from clases.classes import Novelas
from clases.classes import Ensayo
from clases.classes import Poesia

app = Flask(__name__,template_folder='html')

@app.route("/")
def libros():
    return render_template("start_libros.html")

@app.route("/libros", methods=['POST'])
def mostrar_libros():
 # Obtener la clase de libro seleccionada por el usuario

 # Insertar el código aquí
        
 # Renderizar la página de libros con la libro seleccionado
 return render_template("libros.html")#, libro=libro_ingresado)


if __name__ == '__main__':
   app.run(debug=True)

