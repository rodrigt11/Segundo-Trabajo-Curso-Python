#Definimos la clase
class Producto:
  def __init__(self,nombre,precio,cantidad):
    while True:
      try:
        self.nombre = str(nombre)
        break
      except (NameError, TypeError):
        print("Nombre inválido")
    while True:
      try:
        if precio<=0:
          print('El precio no puede ser negativo o nulo')
        else:
          self.precio = float(precio)
          break
      except (ValueError, TypeError):
        print("Precio inválido")
    while True:
      try:
        if cantidad<=0:
          print('La cantidad no puede ser negativa o nula')
        else:
          self.cantidad = int(cantidad)
          break
      except (ValueError, TypeError):
        print("Cantidad inválida")
  
  def __str__(self):
    return f"Producto: {self.nombre}. Precio: {self.precio}. Cantidad: {self.cantidad}"
  
  def actualizar_precio(self, nuevo_precio):
    while True:
      try:
        if nuevo_precio<=0:
          print('El precio no puede ser negativo o nulo')
        else:
          self.precio = nuevo_precio
          break
      except (ValueError, TypeError):
        print("Precio inválido")
  
  def actualizar_cantidad(self, nueva_cantidad):
    while True:
      try:
        if nueva_cantidad<=0:
          print('La cantidad no puede ser negativa o nula')
        else:
          self.cantidad = nueva_cantidad
          break
      except (ValueError, TypeError):
        print("Cantidad inválida")
  
  def calcular_valor_total(self):
    valor = self.precio*self.cantidad
    return valor
  
class Inventario:
  def __init__(self):
    self.lista_productos = []

  def agregar_producto(self, producto):
    self.lista_productos.append(producto)

  def buscar_producto(self, nombre):
    nombre_productos = [producto.nombre for producto in self.lista_productos]
    if nombre in nombre_productos:
      return f"Producto encontrado"
    else:
      return f"Producto no encontrado"

  def calcular_valor_inventario(self):
    valor_productos = [producto.calcular_valor_total() for producto in self.lista_productos]
    valor_total = sum(valor_productos)
    return valor_total

  def listar_productos(self):
    lista = [{"Nombre": elemento.nombre, "Precio": elemento.precio, "Cantidad": elemento.cantidad} for elemento in self.lista_productos]
    return f"{lista}"

def menu_principal(Inventario):
  print("¿Qué desea hacer? 1 Agregar producto 2 Buscar producto 3 Calcular valor 4 Listar productos")
  decision = int(input("Seleccione el número asociado"))
  try:
    if (decision==1):
      return Inventario.agregar_producto()
    elif (decision==2):
      return Inventario.buscar_producto()
    elif (decision==3):
      return Inventario.calcular_valor_inventario()
    elif (decision==4):
      return Inventario.listar_productos()
    else:
      return f"Entrada no válida"
  except (ValueError, TypeError):
    return f"Entrada no válida"

if __name__ = "__main__":
  mi_inventario = Inventario()
  menu_principal(mi_inventario)





