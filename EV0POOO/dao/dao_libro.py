from conex import conn
import traceback

class LibroDAO():
    #Constructor
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "1234", "ventaslibros")
        except Exception as ex:
            print(ex)
    
    #Conexion a la BD
    def getConex(self):
        return self.conn
    
    #Trae tabla Cliente completa
    def prepareLibro(self):
        c = self.getConex()
        result = None
        try:
            cursor = c.getConex().cursor()
            cursor.execute("select IDLIBRO, NOMBRELIBRO, PRECIO, STOCK from LIBRO")
            result = cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return result