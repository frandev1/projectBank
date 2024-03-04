# Mi sistema bancario

from Banquero import crear_cajero
from Banquero import crear_usuario
from Usuario import depositar_dinero
from Usuario import retirar_dinero
from Usuario import consultar_historial_transacciones
from Usuario import consultar_saldo_usuario

#lista de usuarios válidos del sistema bancario
lista_usuarios_sistema = []
#lista de cajeros válidos del sistema bancario
lista_cajeros_sistema = []
# Nombre archivo que almacena información de los usuarios
archivo_usuarios = "lista_usuarios.txt"
# Nombre archivo que almacena información de los cajeros
archivo_cajeros = "lista_cajeros.txt"

def correr_menu_principal():
    '''
    Función principal que da la bienvenida al usuario, 
    y para seleccionar que tipo de usuario está utilizando el sistema.
    Si el usuario es cliente del banco retornar la función correr_menu_usuario.
    Si el usuario es banquero retornar la función correr_menu_banquero.
    Si el usuario ingresa un numero que no se encuentra en las opciones,
    retornar la funcion correr_menu principal.
    ''' 
    print('¡Bienvenido/a, gracias por escoger el Banco Franco!')
    elegir_tipo_usuario = (input('''
     Por favor elija su tipo de usuario, digite el número para escoger:
     1. Banquero
     2. Cliente del Banco
     '''))
    if(elegir_tipo_usuario == '1'):
        print('Usando el sistema de Banquero')
        return correr_menu_banquero()
    elif(elegir_tipo_usuario == '2'):
        print('Usando el sistema de Cliente del Banco')
        return correr_menu_usuario()
    else:
        return correr_menu_principal()

def correr_menu_banquero():
    '''
    Funcion que muestra las opciones del banquero
    Si el banquero quiere crear usuario retornar crear_usuario
    Si el banquero quiere crear cajero retornar crear_cajero
    Si el banquero no ingresa una opción válida,
    retornar la función correr_menu_banquero
    '''
    elegir_accion_banquero = (input('''
    Seleccione la acción que quiere realizar, digite un número:
    1. Crear usuario
    2. Crear cajero
    3. Actualizar billetes de cajero existente
    '''))
    if(elegir_accion_banquero == '1'):
        print('Usted eligió crear usuario') 
        return crear_usuario()
    elif(elegir_accion_banquero == '2'):
        print('Usted eligió crear cajero') 
        return crear_cajero()
    else:
        print('Opción no válida, por favor intente de nuevo') 
        return correr_menu_banquero()

def correr_menu_usuario():
    print('''
    Cajeros disponibles
    ''')
    cargar_datos_cajero(0)
    elegir_cajero()

def cargar_datos_cajero(linea_de_texto_cajero):
  archivo_cajeros_lectura = open('lista_cajeros.txt', 'r')
  lineas_cajeros = archivo_cajeros_lectura.readlines()
  archivo_cajeros_lectura.close()
  '''
  Carga los datos de un cajero al sistema
  '''
  if linea_de_texto_cajero <= (len(lineas_cajeros) -1):
    linea_cajero = lineas_cajeros[linea_de_texto_cajero]
    linea_cajero = linea_cajero.replace("'", "")
    linea_cajero = linea_cajero.replace("\n", "")
    linea_cajero = linea_cajero.replace("[", "")
    linea_cajero = linea_cajero.replace("]", "")
    lista_hileras_cajero = linea_cajero.split(",")
    diccionario_cajero = {}

    #convierte el string con la informacion del usuario en diccionario
    elemento_actual = (len(lista_hileras_cajero) -1)
    return convertir_lista_hileras_diccionario(lista_hileras_cajero, diccionario_cajero, elemento_actual, linea_de_texto_cajero)

def convertir_lista_hileras_diccionario(lista_hileras_cajero, diccionario_cajero, elemento_actual, linea_de_texto_cajero):
  global lista_cajeros_sistema
  '''
  Funcion auxiliar: Convierte una lista de hileras en un diccionario
  Parametros: lista de hileras de la informacion de los cajeros,
  el diccionario que se va a construir, elemento actual de la lista de hileras 
  return: Diccionario de la lista de hileras
  '''
  if(elemento_actual < 0):
    lista_cajeros_sistema += [diccionario_cajero]
    cajeros_disponibles = lista_cajeros_sistema[linea_de_texto_cajero]['Identificador_del_cajero']
    archivo_cajeros_disponibles_escritura = open("Cajeros.txt", "a")
    archivo_cajeros_disponibles_escritura.write(cajeros_disponibles + ",")
    archivo_cajeros_disponibles_escritura.close()
    print('Cajeros disponibles:', cajeros_disponibles)
    return cargar_datos_cajero(linea_de_texto_cajero +1)
  else:
    # se recupera la llave y valor de la lista
    llave = lista_hileras_cajero[elemento_actual -1]
    valor = lista_hileras_cajero[elemento_actual]
    # se crea nueva entrada en diccionario
    llave = llave.replace(" ", "")
    valor = valor.replace(" ", "")
    diccionario_cajero[llave] = valor
    elemento_actual -= 2
    return convertir_lista_hileras_diccionario(lista_hileras_cajero, diccionario_cajero, elemento_actual, linea_de_texto_cajero)
  archivo_usuarios.close()
  
def elegir_cajero():      
  archivo_cajeros_lectura = open('lista_cajeros.txt', 'r')
  lineas_cajeros = archivo_cajeros_lectura.readlines()
  archivo_cajeros_disponibles_lectura = open('Cajeros.txt', 'r')
  lineas_archivo_cajeros_disponibles = archivo_cajeros_disponibles_lectura.read()
  cajero_seleccionado = input('Por favor seleccione el cajero que desea utilizar')
  return revisar_cajero(cajero_seleccionado, 0, lineas_archivo_cajeros_disponibles)

def revisar_cajero(cajero_seleccionado, revisar_linea, lineas_archivo_cajeros_disponibles):
  archivo_cajeros_lectura = open('lista_cajeros.txt', 'r')
  lineas_cajeros = archivo_cajeros_lectura.readlines()
  if revisar_linea <= (len(lineas_cajeros) -1):
    lineas = lineas_cajeros[revisar_linea]
    lineas = lineas.replace("'", "")
    lineas = lineas.replace("\n", "")
    lineas = lineas.replace("[", "")
    lineas = lineas.replace("]", "")
    lista_hileras_cajero_1 = lineas.split(",")
    elemento_actual_1 = (len(lista_hileras_cajero_1) -1)
    if cajero_seleccionado in lineas_archivo_cajeros_disponibles:
      return correr_menu_usuario_aux(cajero_seleccionado)
    else:
      revisar_linea += 1
      return revisar_cajero(cajero_seleccionado, revisar_linea, lineas_archivo_cajeros_disponibles)
  else:
    print('Por favor seleccione un cajero que esté disponible')
    return elegir_cajero(lineas_archivo_cajeros_disponibles)
  archivo_cajeros_lectura.close()


def correr_menu_usuario_aux(cajero_seleccionado):
  '''
  Funcion que inicia el menu del usuario del banco
  El usuario ingresa su usuario y su pin
  '''
  usuario_ingresando = input('Por favor digite su nombre de usuario:')
  leer_lista_usuarios = open("lista_usuarios.txt", 'r') #se abre el archivo para leer
  lectura_usuarios = leer_lista_usuarios.read()
  if usuario_ingresando in lectura_usuarios:
    pin_usuario = input('Por favor digite su pin:')
    if pin_usuario in lectura_usuarios:
      return acciones_usuario(cajero_seleccionado, usuario_ingresando)
    else:
      print('Pin incorrecto, intente de nuevo por favor')
      return correr_menu_usuario()
  else:
    print('Nombre de usuario no existente, intente de nuevo por favor')
    return correr_menu_usuario()

def acciones_usuario(cajero_seleccionado, usuario_ingresando):
  '''
  Función recursiva para mostrar las acciones de usuario
  Si elige retirar dinero, retornar funcion retirar dinero
  Si elige depositar dinero, retornar funcion depositar dinero
  Si elige consultar saldo, retornar funcion consultar saldo
  Si elige consultar historial, retornar funcion consultar historial
  '''
  accion_usuario = (input('''
  Seleccione la acción que quiere realizar, digite un numero:
  1. Retirar dinero
  2. Depositar dinero
  3. Consultar saldo disponible
  4. Consultar historial de transacciones de la cuenta
  '''))
  if(accion_usuario == "1"):
    print('Usted elegió retirar dinero')
    return retirar_dinero(cajero_seleccionado, usuario_ingresando)
  elif(accion_usuario == "2"):
    print('Usted eligió depositar dinero')
    return depositar_dinero(cajero_seleccionado, usuario_ingresando)
  elif(accion_usuario == "3"):
    print('Usted eligió consultar saldo disponible')
    return consultar_saldo_usuario(usuario_ingresando, 0)
  elif(accion_usuario == "4"):
    print('Usted eligió consultar historial de transacciones')
    return consultar_historial_transacciones(usuario_ingresando, 0)
    print('Opción no válida, por favor intente de nuevo')
    return acciones_usuario(cajero_seleccionado, usuario_ingresando)

correr_menu_principal()

    
 