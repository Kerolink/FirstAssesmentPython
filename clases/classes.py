from abc import ABC, abstractmethod

class Libros(ABC):
    def __init__(self, clase, titulo, autor):
        self.clase = clase
        self.titulo = titulo
        self.autor = autor   
    @abstractmethod
    def descripcion(self):
        pass

class Novelas(Libros):
    def __init__(self, clase, titulo, autor, genero):
        super().__init__(clase, titulo, autor)
        self.genero = genero    
    def descripcion(self):
        return f"{self.titulo} es una novela escrita por {self.autor} del género {self.genero}."

class Ensayo(Libros):
    def __init__(self, clase, titulo, autor, tema):
        super().__init__(clase, titulo, autor)
        self.tema = tema

    def descripcion(self):
        return f"{self.titulo} es un ensayo escrito por {self.autor} sobre el tema {self.tema}."

class Poesia(Libros):
    def __init__(self, clase, titulo, autor, estilo):
        super().__init__(clase, titulo, autor)
        self.estilo = estilo    
    def descripcion(self):
        return f"{self.titulo} es un libro de poesía escrito por {self.autor} en el estilo {self.estilo}."
   