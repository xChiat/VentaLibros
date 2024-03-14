from modelo.libro import Libro
from modelo.venta import Venta
from dao.dao_libro import LibroDAO

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
    
    def calcularRecaudacionLibros(self):
        libros = Libro().getLista()
        for libro in libros:
            recaudacion = libro.getPrecio() * libro.getStock()
            print(f"Nombre: {libro.getNombre()} || Recaudacion: {recaudacion}")

    def obtenerLibroMasVendido(self):
        ventas = Venta().getListaVenta()
        libros_vendidos = {}
        
        for venta in ventas:
            libro = venta.getOBJLibro()
            recaudacion = venta.getTotal()
            
            if libro in libros_vendidos:
                libros_vendidos[libro] += recaudacion
            else:
                libros_vendidos[libro] = recaudacion
        
        if libros_vendidos:
            libro_mas_vendido = max(libros_vendidos, key=libros_vendidos.get)
            recaudacion_mas_vendida = libros_vendidos[libro_mas_vendido]
            
            print(f"Nombre: {libro_mas_vendido.getNombre()} || Precio Unitario: {libro_mas_vendido.getPrecio()} || Recaudacion: {recaudacion_mas_vendida}")
        else:
            print("No hay ventas registradas.")