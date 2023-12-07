datos={}
def database():
  print(f"Los datos ingresados hasta el momento son: {datos} ")

def user_registro():
  nombre=input("Escoja un nombre de usuario: ")
  while nombre in datos:
    print("El nombre ya existe")
    nombre=input("Escoja un nombre de usuario")

  contra=input("Ingrese su contraseña: ")
  print("Usuario registrado con éxito")
  datos[nombre] = contra
  return nombre, contra



def user_login():
  nombrelogin=input("Ingrese su nombre de usuario: ")
  contralogin=input("Ingrese su contraseña: ")
  if nombrelogin in datos and contralogin==datos[nombrelogin]:
    print("Usuario reconocido, inicio de sesión exitoso.")
  elif nombrelogin in datos and contralogin != datos[nombrelogin]:
    print("Contraseña incorrecta.")
  else:
    print("Usuario no reconocido.")

def menu():
  registro=input("Para iniciar sesión pulse la tecla i. Para registrarse pulse la tecla r:  ")
  if registro =="i":
    user_login()
  else:
    user_registro()
  datosingresados=input("Si desea ver los datos de los usuarios registrados, pulse la tecla s:  ")
  if datosingresados=="s":
    database()
  menu()

menu()
