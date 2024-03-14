class Libro():
    __lista = []
    def __init__(self, id= None,nombre="", precio=0,stock=0):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock
    
    def __str__(self):
        return f"Id: {self.getId} Nombre: {self.getNombre} Precio: {self.getPrecio} Stock: {self.getStock}"
    
    def getId(self):
        return self.__id
    
    def setNombre(self,nombre):
        self.__nombre = nombre
    
    def getNombre(self):
        return self.__nombre
    
    def setPrecio(self,precio):
        self.__precio = precio
        
    def getPrecio(self):
        return self.__precio
    
    def setStock(self,stock):
        self.__stock = stock
        
    def getStock(self):
        return self.__stock
    
    def getLista(self):
        return self.__lista
    
    def prepararLibros(self,lista):
        for lib in lista:
            self.__lista.append(lib)
            
    def buscarLibro(self,id):
        for lib in self.getLista():
            if lib.getId() == id:
                return lib
        return None
    
    def clearLista(self):
        self.__lista.clear()