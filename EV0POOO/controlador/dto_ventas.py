from modelo.venta import Venta
from modelo.libro import Libro
from dao.dao_ventas import VentasDAO
class VentasDTO:
    def prepareVentas(self):
        daoVnt = VentasDAO()
        result = daoVnt.prepareVenta()
        lista = []
        if result is not None:
            for vnt in result:
                venta = Venta(numVenta=vnt[0],libro=Libro(id=vnt[1],nombre=vnt[2]), cantidad=vnt[3], total=vnt[4])
                lista.append(venta)
        Venta().prepararVenta(lista)
    
    def syncListaVentas(self):
        Venta().clearLista()
        self.prepareVentas()

    def listarVentas(self):
        venta = Venta().getListaVenta()
        return venta
    
    def buscarVenta(self, numVenta):
        venta = Venta()
        result = venta.buscarVenta(numVenta)
        if result is None:
            return None
        else:
            return result

    def agregarVenta(self, idLibro, nombreLibro, cantidad, total):
        daoVnt = VentasDAO()
        result = daoVnt.agregarVenta(Venta(libro=Libro(id=idLibro,nombre=nombreLibro),cantidad=cantidad, total=total))
        self.syncListaVentas()
        return result

    def eliminarVenta(self, numVenta):
        daovnt = VentasDAO()
        resultado = daovnt.eliminarVenta(Venta(numVenta=numVenta))
        self.syncListaVentas()
        return resultado

    def obtenerRecaudacionPorLibro(self):
        recaudaciones = VentasDAO().RecaudacionPorLibro()
        recaudaciones_dict = {nombre_libro: recaudacion for nombre_libro, recaudacion in recaudaciones}
        return recaudaciones_dict

    def obtenerRecaudacionTotal(self):
        recaudaciones = self.obtenerRecaudacionPorLibro()
        return sum(recaudaciones.values())

    def obtenerPorcentajeVentasPorLibro(self):
        recaudaciones = self.obtenerRecaudacionPorLibro()
        total_recaudacion = self.obtenerRecaudacionTotal()
        porcentajes = {nombre_libro: (recaudacion / total_recaudacion) * 100 for nombre_libro, recaudacion in recaudaciones.items()}
        return porcentajes