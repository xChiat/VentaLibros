from modelo.libro import Libro
class Venta:
    __listaVentas = []
    def __init__(self, numVenta=0, libro=Libro(), cantidad= 0,total = 0):
        self.__numVenta = numVenta
        self.__libro = libro
        self.__cantidad = cantidad
        self.__total = total
    
    def __str__(self):
        return f"Num. de Venta: {self.__numVenta} Libro: {self.__libro} cantidad: {self.__cantidad} Total: {self.getTotal}"
    
    def getNumVenta(self):
        return self.__numVenta
    
    def getOBJLibro(self):
        return self.__libro
    
    def getLibro(self):
        return self.__libro.getId()
    
    def getNomLibro(self):
        return self.__libro.getNombre()
    
    def setCantidad(self,cantidad):
        self.__cantidad = cantidad
    
    def getCantidad(self):
        return self.__cantidad
    
    def setTotal(self,total):
        self.__total = self.__libro.getPrecio() * self.__cantidad
        
    def getTotal(self):
        return self.__total
    
    def getListaVenta(self):
        return self.__listaVentas
    
    def prepararVenta(self,lista):
        for vnt in lista:
            self.__listaVentas.append(vnt)
            
    def buscarVenta(self,numventa):
        for vnt in self.getLista():
            if vnt.getNumVenta() == numventa:
                return vnt
        return None
    
    def clearLista(self):
        self.__listaVentas.clear()