from datetime import date 
class empresa:
    def __init__(self,nom, ruc, tel, dir):
        self.nombre=nom
        self.ruc=ruc
        self.telefono=tel
        self.direccion=dir

    def mostrarEmpresa(self):
        print("empresa:{:17} ruc:{}".format(self.nombre,self.ruc))


from abc import ABC, abstractclassmethod
class cliente(ABC):
    def __init__(self, nom, ced, tel) :
        self.nombre=nom
        self.cedula=ced
        self.telefono=tel
     
    @abstractclassmethod 
    def getCedula(self):
        return self.cedula

    def mostrarCliente(self):   
        print(self.nombre, self.cedula, self.telefono) 

class clienteCorporativo(cliente):
    def __init__(self,nom, ced, tel, contrato):
        super().__init__( nom, ced , tel)
        self.__contrato=contrato
    
    @property
    def contrato(self) :
        return self.__contrato

    @contrato.setter
    def contrato(self, value):
        self.__contrato=value 
        if value :
            self.__contrato=value
        else:
            self.__contrato='sin contrato'      

    def    mostrarCliente(self):
        print(self.nombre,self.__contrato)    

class clientePersonal(cliente):
    def __init__(self,nom, ced, tel, promocion=True):
            super().__init__( nom, ced , tel)
            self.__promocion=promocion    

    @property
    def promocion(self) :
        return self.__promocion

    @promocion.setter
    def promocion(self, value):
        self.__promocion=value       

    def    mostrarCliente(self):
        print("Cliente: {:13} Cedula: {}".format(self.nombre, self.cedula))

    def getCedula(self):
        return super().getCedula()    

class articulo:
    secuencia=0
    iva=0.12
    def __init__(self, des, pre, sto ):
        articulo.secuencia+=1
        self.codigo=articulo.secuencia
        self.descripcion=des
        self.precio=pre
        self.stock=sto
    def    mostrarArticulo(self):
        print(self.codigo, self.descripcion)     

class DetVenta:
    linea=0
    
    def __init__(self, articulo, cantidad):
        DetVenta.linea+=1
        self.lineaDetalle=DetVenta.linea
        self.articulo=articulo
        self.precio=articulo.precio
        self.cantidad=cantidad  

class CabVenta:
    def __init__(self, fac, empresa, fecha, cliente, tot=0):
        self.empresa=empresa
        self.factura=fac 
        self.fecha=fecha 
        self.cliente=cliente 
        self.total=tot
        self.detalleVen=[]

    def agregarDetalle(self, articulo,cantidad):  
        detalle=DetVenta(articulo,cantidad)
        self.total+=detalle.precio*detalle.cantidad
        self.detalleVen.append(detalle)      

    def mostrarVenta (self, empNombre, empRuc ):
        print("empresa:{:17} Ruc:{}".format(empNombre,empRuc))
        print("Factura#:{:13} Fecha:{}".format(self.factura, self.fecha))
        self.cliente.mostrarCliente()
        print("linea articulo         precio cantidad subtotal")
        for det in self.detalleVen:
            print("{:5} {:15} {} {:6} {:7}".format(det.linea, det.articulo.descuento ))
        print("total venta:{:26} ".format(self.total))

#cli=cliente("jose","1548752365 ","025468631", "#0001")
# Empresa=empresa()
#cli1=clienteCorporativo("jose","1548752365 ","025468631","#0001")
cli1=clientePersonal("jose","1548752365 ","025468631", False)
# print(cli1.getCedula())
# cli1.mostrarCliente()
# print(cli1.nombre)
# cli1.contrato="#0002"
# print(cli1.contrato)
# art1=articulo("aceite", 2, 100)
# art1.mostrarArticulo()
# art2=articulo("coca cola", 1, 200)
# art2.mostrarArticulo()
# today=date.today()
# fecha = date (2021, 8,15)
venta= CabVenta('f001', date.today(),"darwin","0",cli1)
print (venta)
# venta.agregarDetalle(art1,3)
# venta.agregarDetalle(art2,2)
# venta.mostrarVenta(empresa.nombre, empresa.ruc)


# class interfaceSistemaPago(ABC):
#      # este proceso hace el pago del calculo de interes de la tarjeta
#     @abstractclassmethod
#     def pago(self):
#         pass
    
#     @abstractclassmethod
#     def saldo (self):
#         pass

# class PagoTarjetaImplements(interfaceSistemaPago) : 
#     def pago(self):
#         return "pago tarjeta"
#     def saldo(self):
#         return " saldo tarjeta rebajado"

# class implementsPagoContrato(interfaceSistemaPago):
#     def pago(self):
#         return "pago contrato2"

#     def saldo(self):
#         return " saldo contrato rebajado"    

# class vendedor ():
#     def __init__(self, nombre):
#         self.nombre=nombre
#     def moduloPago (self, contrato):
#         return contrato.pago()

# pagoTarjeta= PagoTarjetaImplements()
# print(pagoTarjeta.pago())

# Contrato= implementsPagoContrato()
# print(Contrato.pago())

# ven1= vendedor("daniel")
# print(ven1.moduloPago(Contrato))
