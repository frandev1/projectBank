#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 23:11:39 2022

@author: franco
"""

# Crear cajero

def crear_usuario():
  nombre_usuario_crear = input('Digite el nombre del usuario que desea crear')
  if(verificar_longitud(nombre_usuario_crear)):
    print('El nombre usuario ha sido creado exitosamente')
  else:
    print('El nombre de usuario no es válido')

# Verificar si el nombre cumple con la expresion regular

def verificar_longitud(nombre_usuario_crear):
  '''
  Funcion para verificar si el nombre cumple con la longitud requerida
  '''
  if(len(nombre_usuario_crear) >= 6): #El nombre tiene que tener minimo 6 caracteres
    return convertir_nombre_unicode(nombre_usuario_crear, 0, [])
  else:
    print('El nombre de usuario no cumple con la longitud minima requerida')
    return False
  
def convertir_nombre_unicode(nombre_usuario_crear, recorrer_nombre, lista_unicode_nombre):
  '''
  Función aux: para convertir el nombre en valores unicode.
  Parámetros: nombre de usuario a crear, posición inicial al recorrer el nombre, lista unicode vacía
  Return: se devuelve la lista con los valores unicode del nombre, y despues
  verificar si se cumple con la expresión regular.
  '''
  largo_nombre_crear = len(nombre_usuario_crear)
  if(recorrer_nombre < largo_nombre_crear):
    # se recorre el nombre, convirtiendo los valores a unicode y guardandolos en lista
    valor_unicode_nombre = list([ord(nombre_usuario_crear[recorrer_nombre])])
    # se suma la lista de los valores unicode a la lista
    lista_unicode_nombre += valor_unicode_nombre
    # se le suma un uno a recorrer_nombre para que siga con el siguiente carácter
    recorrer_nombre += 1
    return convertir_nombre_unicode(nombre_usuario_crear, recorrer_nombre, lista_unicode_nombre)
  # se define la condición de parada
  elif(recorrer_nombre == largo_nombre_crear):
      return verificar_unicode_nombre(nombre_usuario_crear, lista_unicode_nombre, 0)

def verificar_unicode_nombre(nombre_usuario_crear, lista_unicode_nombre, recorrer_lista):
  '''
  Funcion auxiliar: Para verificar si el nombre cumple con la expresion regular
  Parametros: nombre de usuario a crear, posición inicial al recorrer el nombre, lista unicode vacía
  Return: si cumple se llama a una funcion para verificar que el nombre sea unico
  '''
  letras_minusculas = range(97, 123)
  letras_mayusculas = range(65, 91)
  # Rango de los numeros base 10 en unicode
  numeros_rango = range(48, 58)
  # Valor unicode de los simbolos especiales
  simbolo_rango = (33, 35, 36, 38, 63)
  
  longitud_lista = len(lista_unicode_nombre)
  # la posicion del simbolo sera siempre el ultimo
  simbolo_posicion = longitud_lista - 1 # Calculo para ver posicion simbolo
  # la posicion de los numeros siempre seran los ultimos 4 antes del simbolo
  numeros_posicion_nombre = longitud_lista - 5 #Calculos para ver en qué posición están los numeros
  
  # Se utiliza la posicion del primer numero de referencia
  if(recorrer_lista < numeros_posicion_nombre):
    if(lista_unicode_nombre[recorrer_lista] in letras_minusculas) or (lista_unicode_nombre[recorrer_lista] in letras_mayusculas):
      recorrer_lista += 1
      return verificar_unicode_nombre(nombre_usuario_crear, lista_unicode_nombre, recorrer_lista)
  
  elif(recorrer_lista >= numeros_posicion_nombre) and (recorrer_lista < simbolo_posicion):
    if(lista_unicode_nombre[recorrer_lista] in numeros_rango):
      recorrer_lista += 1
      return verificar_unicode_nombre(nombre_usuario_crear, lista_unicode_nombre, recorrer_lista)
  
  elif(recorrer_lista == simbolo_posicion):
    if(lista_unicode_nombre[recorrer_lista] in simbolo_rango):
      return revisar_nombre(nombre_usuario_crear)
  
  else: 
    print('El nombre de usuario no cumple con la expresión regular')
    return False

def revisar_nombre(nombre_usuario_crear):
  '''
  Función auxiliar: Comprueba si existe el nombre de usuario está en uso
  Parametro: Nombre de usuario a verificar
  Return: Si el nombre no está en uso se crea el pin
  '''
  archivo_usuario = open("lista_usuarios.txt", "a")
  archivo_usuario_lectura = open("lista_usuarios.txt", "r") # se lee el archivo
  lineas_usuario = archivo_usuario_lectura.read()
  if nombre_usuario_crear in lineas_usuario:
    print('Este nombre ya está en uso')
    return False

  else:
    archivo_usuario.close()
    return generar_pin(nombre_usuario_crear)

# Pin de 4 digitos del usuario
from random import randrange
def generar_pin(nombre_usuario_crear):
  '''
  Funcion auxiliar: Generar un pin aleatorio para el usuario
  Parametros: El nombre del usuario del pin
  Return: El pin generado y se llama la funcion guardar usuario
  '''
  pin = (randrange(1000, 9999))
  print('Este es el pin del usuario:', pin)
  return guardar_usuarios(nombre_usuario_crear, pin)

# Guardar el nombre y el pin
def guardar_usuarios(nombre_usuario_crear, pin):
  '''
  Funcion auxiliar: Para guardar el usuario en una archivo .txt
  Parametros: nombre de usuario a crear y su pin
  Return: True para confirmar que se guardó
  '''
  if(isinstance(pin, int)):
    datos_usuario = ['Nombre_usuario', nombre_usuario_crear, 'Pin', pin, 'Saldo', 0, 'Historial Transacciones', '']
    # se abre el archivo
    archivo = open("lista_usuarios.txt", "a")
    # se convierte el diccionario en hilera
    diccionario_hilera = str(datos_usuario)
    #se escribe la linea en el archivo
    archivo.write(diccionario_hilera + '\n')
    # se cierra el archivo
    archivo.close()
    return True

# Crear cajero

def crear_cajero():
  id_cajero = input('Ingrese el nombre del cajero a crear:')
  if(verificar_cajero(id_cajero) == True):
    print('El cajero se creó exitosamente')
  else:
    print('El cajero no pudo crearse de forma exitosa')

# Verificar si el cajero cumple con la expresión regular
def verificar_cajero(id_cajero):
  '''
  Función princial: Verificar si el id cumple con la longitud minima requerida
  Parámetro: Id cajero
  Return: Si cumple con la longitud requerida se llama a la función para verificar
  los caracteres unicode
  '''
  #El nombre del cajero debe ser al menos de 4 caracteres
  if(len(id_cajero) >= 4):
    return convertir_id_unicode(id_cajero, 0, [])
  else:
    print('El usuario no cumple con la longitud necesaria requerida')

def convertir_id_unicode(id_cajero, recorrer_id, lista_unicode_id):
  '''
  Funcion auxiliar: Convertir los caracteres unicode del id y guardarlos en una lista
  Parametros: Id del cajero, la posicion del caracter a recorrer, lista vacia
  Return: Se retorna los valores unicode del id del cajero
  '''
  largo_id = len(id_cajero)
  if(recorrer_id < largo_id):
    valor_unicode_id = list([ord(id_cajero[recorrer_id])])
    lista_unicode_id += valor_unicode_id
    recorrer_id += 1
    return convertir_id_unicode(id_cajero, recorrer_id, lista_unicode_id)
  # se define condicion de parada
  elif(recorrer_id == largo_id):
    return verificar_id_unicode(id_cajero, lista_unicode_id, 0)

def verificar_id_unicode(id_cajero, lista_unicode_id, recorrer_id):
  '''
  Funcion auxiliar: Verificar si el id cumple con los caracteres permitidos usando unicode
  Parametros: id cajero, lista con el id en unicode y el numero de la posición de la lista a recorrer
  Return: Se retorna otra funcion para comprobar que el id sea unico
  '''
  # Rango de las letras mayusculas en unicode
  letras_mayusculas = range(65,91)
  # Rango de los numeros base 10 en unicode
  numeros = range(48,58)

  longitud_id = len(lista_unicode_id)
  # Se usa la posicion del primer numero como referencia segun la expresion requerida
  numeros_posicion_id = 3 

  if(recorrer_id < numeros_posicion_id):
    if(lista_unicode_id[recorrer_id] in letras_mayusculas):
      recorrer_id += 1
      return verificar_id_unicode(id_cajero, lista_unicode_id, recorrer_id)
  
  elif (recorrer_id >= numeros_posicion_id) and (recorrer_id < longitud_id):
    if(lista_unicode_id[recorrer_id] in numeros):
      recorrer_id += 1
      return verificar_id_unicode(id_cajero, lista_unicode_id, recorrer_id)

  elif (recorrer_id == longitud_id):
    return revisar_id(id_cajero)
  
  else:
    print('El identificador del cajero no cumple con la expresion regular')
    return False

def revisar_id(id_cajero):
  '''
  Funcion auxiliar: Verifica si el id del cajero es unico
  Parametro: Id del cajero a verificar
  Return: True or False
  '''
  #se crea el archivo si no existia
  archivo_cajero = open("lista_cajeros.txt", "a")
  #se lee el archivo
  archivo_cajero_lectura = open("lista_cajeros.txt", "r")
  lineas_cajero = archivo_cajero_lectura.read()
  if id_cajero in lineas_cajero:
    print("Este id de cajero ya está en uso")
    return False
  else:
    agregar_billetes_cajero_nuevo(id_cajero)
    return True
  #se cierra el archivo
  archivo_cajero.close()

# Agregar billetes al cajero creado
def agregar_billetes_cajero_nuevo(id_cajero):
  print('Ingrese la cantidad de billetes por cada denominación que desee:')
  billetes_100_cajero_nuevo = input('Introduzca los billetes de 100 que desee')
  billetes_100_cajero_nuevo = int(billetes_100_cajero_nuevo)

  billetes_50_cajero_nuevo = input('Introduzca los billetes de 50 que desee')
  billetes_50_cajero_nuevo = int(billetes_50_cajero_nuevo)

  billetes_20_cajero_nuevo = input('Introduzca los billetes de 20 que desee')
  billetes_20_cajero_nuevo = int(billetes_20_cajero_nuevo)

  billetes_10_cajero_nuevo = input('Introduzca los billetes de 10 que desee')
  billetes_10_cajero_nuevo = int(billetes_10_cajero_nuevo)

  billetes_5_cajero_nuevo = input('Introduzca los billetes de 5 que desee')
  billetes_5_cajero_nuevo = int(billetes_5_cajero_nuevo)

  billetes_2_cajero_nuevo = input('Introduzca los billetes de 2 que desee')
  billetes_2_cajero_nuevo = int(billetes_2_cajero_nuevo)

  billetes_1_cajero_nuevo = input('Introduzca los billetes de 1 que desee')
  billetes_1_cajero_nuevo = int(billetes_1_cajero_nuevo)

  guardar_datos_cajero(id_cajero, billetes_100_cajero_nuevo, billetes_50_cajero_nuevo, 
                           billetes_20_cajero_nuevo, billetes_10_cajero_nuevo, billetes_5_cajero_nuevo,
                           billetes_2_cajero_nuevo, billetes_1_cajero_nuevo)

# Se agrega la información del cajero al archivo
def guardar_datos_cajero(id_cajero, billetes_100, billetes_50, billetes_20, billetes_10, billetes_5, billetes_2, billetes_1):
  '''
  Funcion auxiliar: Se encargar de guardar la información del cajero en el archivo txt
  Parametros: el identificador y la cantidad de billetes por cada denominacion ingresado
  Return: el id y la cantidad de billetes por denominacion guardados correctamente
  '''
  lista_cajero_diccionario = ['Identificador_del_cajero', id_cajero, 'Billetes_de_100', billetes_100, 'Billetes_de_50', billetes_50,
                              'Billetes_de_20', billetes_20, 'Billetes_de_10', billetes_10, 'Billetes_de_5', billetes_5, "Billetes_de_2", billetes_2,
                              'Billetes_de_1', billetes_1]
  archivo = open("lista_cajeros.txt", "a")
  diccionario_hilera = str(lista_cajero_diccionario) + "\n"
  # escribe linea de archivo
  archivo.write(diccionario_hilera)
  archivo.close()

