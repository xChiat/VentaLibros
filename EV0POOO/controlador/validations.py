from controlador.dto_libro import LibroDTO
from controlador.dto_ventas import VentasDTO

#
def cargaInicial():
    LibroDTO().prepareLibro()
    VentasDTO().prepareVentas()
    
#-------- VALIDAR INT Y STR -----------
def validaInt(txt):
    while True:
        try:
            opc = int(input(f"Ingresa {txt}: "))
            return opc
        except:
            print("Error de Ingreso, solo puedes ingresar números.")
            
def validaStr(txt):
    while True:
        valor = input(f"Ingrese {txt}: ").strip()
        if valor:
            return valor
        else:
            print("Campo incorrecto, no debe estar vacío.")

# ---------- LIBROS ----------
def validateFindAllLibros():
    print("\n--------------------")
    print(" Listado de Libros. ")
    print("--------------------\n")
    libros = LibroDTO().listarLibros()
    if libros:
        for libro in libros:
            print(f"Id: {libro.getId()} Nombre: {libro.getNombre()} Precio: {libro.getPrecio()} Stock: {libro.getStock()}")
    else:
        print("No hay libros registrados.")
   
def validateBuscarLibro(id):
    result = LibroDTO().buscarLibro(id)
    if result is None:
        return None
    else:
        return result
    
#---------- VENTAS -----------
def validateFindAllVentas():
    print("\n----------------------")
    print("Listado de Ventas.")
    print("----------------------\n")
    result = VentasDTO().listarVentas()
    if len(result) > 0:
        for vnt in result:
            libro = vnt.getOBJLibro()
            print(f"Num. de Venta: {vnt.getNumVenta()} Libro Id: {libro.getId()} Nombre: {libro.getNombre()} cantidad: {vnt.getCantidad()} Total: {vnt.getTotal()}")
    else:
        print("No hay ventas registradas.")



def validateBuscarVenta(numventa):
    result = VentasDTO().buscarVenta(numventa)
    if result is None:
        return None
    else:
        return result 

def validateEliminarVenta():
    print("\n--------------------")
    print("  Eliminar Venta. ")
    print("--------------------\n")
    numVenta = validaInt(" el numero de venta")
    val = validateBuscarVenta(numVenta)
    if val is None:
        return print("La Venta no existe, no se puede Cancelar.")
    else:
        print("¿Estas seguro que deseas Cancelar la Venta?")
        confirm = input("Presiona Y/y para Confirmar o N/n para Cancelar:")
        confirm = confirm.upper()
        if confirm == "Y":
            result = VentasDTO().eliminarVenta(numVenta)
            return print(result)
        elif confirm == "N":
            return print("Operación Cancelada.")
        else:
            print("Opción invalida, intentalo nuevamente.")
            return validateEliminarVenta()


def validateAgregarVenta():
    print("\n--------------------")
    print("  Agregar Venta.  ")
    print("--------------------\n")
    idLibro = validaInt("Id del Libro")
    libro_existente = validateBuscarLibro(idLibro)
    if libro_existente is None:
        return print("El Libro no existe. Operación Cancelada.")
    
    nombreLibro = libro_existente.getNombre()
    precio = libro_existente.getPrecio()
    stock = libro_existente.getStock()
    
    cantidad = validaInt("Cantidad de ejemplares")
    if not cantidad or cantidad > stock:
        return print("Es necesario agregar una cantidad válida. Operación Cancelada.")
    
    total = cantidad * precio
    
    result = VentasDTO().agregarVenta(idLibro, nombreLibro, cantidad, total)
    print(result)

#-------- OPCIONES Y MENUS -------------
def validaOpc(num):
    while True:
        try:
            opc = int(input("Ingrese una opción: "))
            if opc < 1 or opc > num:
                print(f"Debe ingresar una opción entre 1 y {num}.")
            else:
                return opc
        except:
            print("Solo puedes ingresar números. Por favor reintente.")

def menu():
    print("\n=================================")
    print("======= Venta De Libros =======")
    print("=================================\n")
    print("1. INFO LIBROS")
    print("2. CRUD VENTAS")
    print("3. Salir del Sistema")

def menuCliente():
    print("\n*******************")
    print("*** INFO LIBROS ***")
    print("*******************\n")
    print("1. Lista de Libros")
    print("2. Libro mas vendido")
    print("3. Recaudacion")
    print("4. Porcentaje")
    print("5. Volver al Menu Principal")

def menuMascota():
    print("\n*******************")
    print("*** CRUD Ventas ***")
    print("*******************\n")
    print("1. Agregar Venta")
    print("2. Cancelar Venta")
    print("3. Mostrar todas las Ventas")
    print("4. Volver al Menu Principal")


#---------- INICIALISAR -----------
def inicial():
    cargaInicial()
    while True:
        menu()
        opc = validaOpc(5)
        if opc == 1:
            while True:
                menuCliente()
                opc = validaOpc(5)
                if opc == 1:
                    validateFindAllLibros()
                elif opc == 2:
                    LibroDTO().obtenerLibroMasVendido() 
                elif opc == 3:
                    LibroDTO().calcularRecaudacionLibros() 
                elif opc == 4:
                    VentasDTO().calcularPorcentajeVentasDeCadaLibro() 
                else:
                    break    
        elif opc == 2:
            while True:
                    menuMascota()
                    opc = validaOpc(4)
                    if opc == 1:
                        validateAgregarVenta()
                    elif opc == 2:
                        validateEliminarVenta()
                    elif opc == 3:
                        validateFindAllVentas()
                    else:
                        break  
        else:
            print("Programa Finalizado.")
            break