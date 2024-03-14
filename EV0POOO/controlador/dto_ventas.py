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

    def calcularPorcentajeVentasDeCadaLibro(self):
        ventas = Venta().getListaVenta()
        total_ventas = sum(venta.getCantidad() for venta in ventas)
        for venta in ventas:
            porcentaje = (venta.getCantidad() / total_ventas) * 100
            print(f"Nombre: {venta.getNomLibro()} || Cantidad Ejemplares Vendidos: {venta.getCantidad()} || Porcentaje: {porcentaje}%")