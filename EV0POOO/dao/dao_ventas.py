from conex import conn
import traceback

class VentasDAO():

    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "1234", "ventaslibros")
        except Exception as ex:
            print(ex)
    

    def getConex(self):
        return self.conn
    

    def prepareVenta(self):
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select NUMVENTA, VENTAS.IDLIBRO, LIBRO.NOMBRELIBRO , CANTIDAD, TOTAL from VENTAS INNER JOIN LIBRO ON LIBRO.IDLIBRO = VENTAS.IDLIBRO")
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return result
    
    def LibroMasVendido(self):
        sql = "SELECT IDLIBRO, SUM(TOTAL) AS TotalVentas FROM VENTAS GROUP BY IDLIBRO ORDER BY TotalVentas DESC LIMIT 1;"
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return result
    
    def RecaudacionPorLibro(self):
        sql = "SELECT Ventas.libro AS NombreLibro , SUM(TOTAL) AS Recaudacion FROM VENTAS GROUP BY IDLIBRO ORDER BY Recaudacion;"
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return result
    
    def agregarVenta(self,venta):
        sql = "insert into VENTAS (NUMVENTA, IDLIBRO, LIBRO, CANTIDAD, TOTAL) values (null,%s,%s,%s,%s)"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (venta.getLibro(),venta.getNomLibro(),venta.getCantidad(),venta.getTotal()))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos agregados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje
    
    def eliminarVenta(self, venta):
        sql = "delete from VENTAS where NUMVENTA = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (venta.getNumVenta(),))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos eliminados satisfactoriamente"
            else:
                mensaje="No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje