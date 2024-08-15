import json

def abrirarchivo():
    miJson=[]
    with open("menu.json", encoding="utf-8") as openfile:
        miJson=json.load(openfile)
        return miJson
def guardararchivo(datos):
    with open("menu.json", "w") as outfile:
        json.dump(datos,outfile)
info=abrirarchivo()


def abrir():
    mijson=[]
    with open("pagos.json", encoding="utf-8") as openfile:
        mijson=json.load(openfile)
        return mijson
def guardar(misdatos):
    with open("pagos.json", "w") as outfile:
        json.dump(misdatos, outfile)

def archivo():
    misjson=[]
    with open("pedidos.json", encoding="utf-8") as openfile:
        misjson=json.load(openfile)
        return misjson
def miarchivo(dato):
    with open("pedidos.json", "w")as outfile:
        json.dump(dato, outfile)

class pedidos:
    def __init__(self, categoria, nombre, precio):
        self.categoria=categoria
        self.nombre=nombre
        self.precio=precio
        self.pedido=[]
        print(pedidos)

class categoria:
    def __init__(self, entrada, plato_fuerte, bebida):
        self.entrada=entrada
        self.plato_fuerte=plato_fuerte
        self.bebida=bebida
        self.categoria=[]
        print(categoria)

class pagos:
    def __init__(self, cliente, total, fecha_pago):
        self.cliente=cliente
        self.total=total
        self.fecha_pago=fecha_pago
        self.pagos=[]
class MoliPollito():
    def __init__(self, nombre):
        self.nombre=nombre
    def estadopedido(self, categoria):
        print(f"Estado del pedido: ")
        for pedido in pedidos:
            print(f"Categoria: {pedido.categoria}-estado: {pedido.estado}")
    
    def estadocategoria(self, entrada, plato_fuerte, bebida):
        print(f"EStado de la categoria: ")
        for categorias in categoria:
            print(f"Entrada: {categorias.entrada}{categorias.plato_fuerte}{categorias.bebida}-estado: {categorias.estado}")

    def estadopagos(self, cliente, total, fecha_pago):
        print(f"Estado de los pagos: ")
        for pago in pagos:
            print(f"Cliente: {pago.cliente}{pago.total}{pago.fecha_pago}-estado: {pago.estado}")

    def eliminarpedido(self, listapedido):
        categoriapedido=input("Por favor puede ingresar la categoria del pedido: ")
        for pedido in categoriapedido:
            if pedido.categoria == categoriapedido:
                categoriapedido.remove(pedido)
                print("El pedido fue eliminado exitosamente")
                return
            print("No se encontro ningún pedido con esa categoria")

    def eliminarcategoria(self, listacategoria):
        numerocategoria=input("Por favor puede ingrsar: ")
        for categoria in listacategoria:
            if categoria.categoria == numerocategoria:
                numerocategoria.remove(categoria)
                print("La categoria fue eliminada exitosamente")
                return
            print("No se encontro ninguna categoria")
class reportar():
    def __init__(self):
        self.pedidos=[]
        self.categoria=[]
        self.pagos=[]
        self.MoliPollito=MoliPollito("Yessica")
    def pedidonuevo(self, pedido):
        self.pedidos.append(pedido)
    def categorianueva(self, categoria):
        categorianueva=categoria(entrada, plato_fuerte, bebida)
        self.categoria.append(categoria)
        for categorias in self.categoria:
            if categoria.agregarcategoria(categoria):
                return True
            else:
                return False
    print("----- MENU -----")
    print("1. pedios")
    print("2. categoria")
    print("3. MoliPollito")
    print("4. salir")
opc=input("Por favor elija una de las opciones: ")
if opc == "1":
    print("----- MENU PEDIDOS -----")
    print("1. Revisar información")
    print("2. salir")
    x=int(input("Elije una de las opciones: "))
    if x == 1:
        info=abrirarchivo()
        for i in info[0]["pedidos"]:
            print("---------------------")
            print("Categoria:",i["categoria"])
            print("Nombre:",i["nombre"])
            print("Precio",i["precio"])
    elif x == 2:
        print("Hasta luego, vuelve pronto")
elif opc =="2":
    info=abrirarchivo()
    print("----- MENU CATEGORIA -----")
    print("Estado de las categorias")
    print("2. salir")
    x=int(input("Por favor elije una de las opciones: "))
    if x==1:
        print("1. estado")
        estado=int(input("Elije la opción estado por favor"))
        info=abrirarchivo()
        if estado==1:
            print("Este es el estado de las categoria: ")
            for categoria in info[0]["categorias"]:
                if categoria["estado"]=="1":
                    print(f"Entrada: {categoria["entrada"]}, estado:{categoria["estado"]}")
        elif x==2:
            print("Hasta luego, vuelve pronto")
    elif opc=="3":
        print("----- MENU MOLIPOLLITO -----") 
        print("1. Registrar pedidos")
        print("2. Actualizar los pedidos")
        print("3. Eliminar pedidos")
        print("4. Eliminar categoria") 
        print("5. Salir del programa:")
        x=int(input("Por favor elije una de las opciones: "))