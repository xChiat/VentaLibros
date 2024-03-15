from modelo.libro import Libro
from modelo.venta import Venta
from dao.dao_libro import LibroDAO
from dao.dao_ventas import VentasDAO

class LibroDTO:
    def prepareLibro(self):
        daoLib = LibroDAO()
        result = daoLib.prepareLibro()
        lista = []
        if result is not None:
            for lib in result:
                libro = Libro(id=lib[0], nombre=lib[1], precio=lib[2], stock=lib[3]) 
                lista.append(libro)
        Libro().prepararLibros(lista)
    
    #Limpia la lista Libros y la carga nuevamente. 
    def syncListaLibros(self):
        Libro().clearLista()
        self.prepareLibro()
        
    #Buscar todos los Libros
    def listarLibros(self):
        libro = Libro().getLista()
        return libro
    
    #Busca un Libro en la lista de clase
    def buscarLibro(self, id):
        libro = Libro()
        result = libro.buscarLibro(id)
        if result is None:
            return None
        else:
            return result
    
    def obtenerRecaudacionPorLibro(self):
        venta_dao = VentasDAO()
        result = venta_dao.RecaudacionPorLibro()
        return result

    def obtenerLibroMasVendido(self):
        venta_dao = VentasDAO()
        result = venta_dao.LibroMasVendido()
        if result:
            libro_id, total_ventas = result
            libro = self.buscarLibro(libro_id)
            if libro:
                return libro, total_ventas
        return None, 0