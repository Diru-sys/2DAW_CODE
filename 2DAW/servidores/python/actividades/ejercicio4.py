producto = str(input("Introduce  el nombre  del  producto: "))
#Se  pide  el nombre del  producto en  String

precio_unitario = float(input("Introduce el precio  unitario (€): "))
#Se pide el precio del producto

cantidad = int(input("Introduce la cantidad: "))
#Se pide la cantidad de productos

porcentaje_descuento = float(input("Introduce el porcentaje  de descuento: "))
#Se pide el numero que se va a usar como porcentaje para aplicarlo

#Aquí vamos a realizar todos los calculos
precioCantidad = precio_unitario * cantidad
importe_descuento = precioCantidad * (porcentaje_descuento / 100)
base_descuento = precioCantidad - importe_descuento
iva = base_descuento * 0.21 #El IVA siempre se escribe  como 0.21 ya que es el 21%
total = base_descuento + iva

#TICKET FINAL
print("\n----------- TICKET -----------")
print("Producto:",producto)
print("Cantidad del producto:",cantidad)
print("Precio Unitario:",precio_unitario,"€")
print("Subtotal:",precioCantidad,"€")
print("Descuento:",base_descuento,"€")
print("IVA:",iva,"€")
print("TOTAL:",total,"€")
print("-------------------------------")