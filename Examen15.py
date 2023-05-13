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
    a1 = request.form["clase"]
    a2 = request.form["titulo"]
    a3 = request.form["autor"]
 # Insertar el código aquí
    if a1 == "Novela":
        a4 = request.form["genero"]
        libro_ingresado = Novelas(a1, a2, a3, a4)

    elif a1 == "Ensayo":
        a4 = request.form["tema"]
        libro_ingresado = Ensayo(a1, a2, a3, a4)

    elif a1 == "Poesia":
        a4 = request.form["poesia"]
        libro_ingresado = Poesia(a1, a2, a3, a4)
        
 # Renderizar la página de libros con la libro seleccionado
    return render_template("libros.html", libro=libro_ingresado)


if __name__ == '__main__':
   app.run(debug=True)

