#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 23:11:01 2022

@author: franco
"""
import time
# depositar dinero

def depositar_dinero(cajero_seleccionado, usuario_ingresando):
  '''
  Funcion principal: Depositar billetes por denominación
  Parametros: cajero seleccionado y usuario ingresando
  Return: Los billetes a depositar por denominacion
  '''
  print('Por favor inserte la cantidad de billetes que desea depositar por denominación')
  
  depositar_billetes_100 = input('Introduzca la cantidad billetes de 100 que desea depositar')
  depositar_billetes_100 = int(depositar_billetes_100)

  depositar_billetes_50 = input('Introduzca la cantidad de billetes de 50 que desea depositar')
  depositar_billetes_50 = int(depositar_billetes_50)

  depositar_billetes_20 = input('Introduzca la cantidad de billetes de 20 que desea depositar')
  depositar_billetes_20 = int(depositar_billetes_20)

  depositar_billetes_10 = input('Introduzca la cantidad de billetes de 10 que desea depositar')
  depositar_billetes_10 = int(depositar_billetes_10)

  depositar_billetes_5 = input('Introduzca la cantidad de billetes de 5 que desea depositar')
  depositar_billetes_5 = int(depositar_billetes_5)

  depositar_billetes_2 = input('Introduzca la cantidad de billetes de 2 que desea depositar')
  depositar_billetes_2 = int(depositar_billetes_2)

  depositar_billetes_1 = input('Introduzca la cantidad de billetes de 1 que desea depositar')
  depositar_billetes_1 = int(depositar_billetes_1)

  buscar_linea_en_cajero(cajero_seleccionado, 0, depositar_billetes_100, depositar_billetes_50, depositar_billetes_20,
                         depositar_billetes_10, depositar_billetes_5, depositar_billetes_2, depositar_billetes_1)
  return sumar_deposito_billetes(cajero_seleccionado, usuario_ingresando, depositar_billetes_100, depositar_billetes_50, 
                                 depositar_billetes_20, depositar_billetes_10, depositar_billetes_5, depositar_billetes_2, 
                                 depositar_billetes_1)

def buscar_linea_en_cajero(cajero_seleccionado, posicion, depositar_billetes_100, depositar_billetes_50, depositar_billetes_20,
                         depositar_billetes_10, depositar_billetes_5, depositar_billetes_2, depositar_billetes_1):
    buscar_linea_archivo = open("lista_cajeros.txt", "r+")
    buscar_linea_cajero = buscar_linea_archivo.readlines()
    buscar_linea_archivo.close()
    linea_texto = buscar_linea_cajero[posicion]
    if(cajero_seleccionado in linea_texto):
        return actualizar_billetes_denominacion(cajero_seleccionado, posicion, depositar_billetes_100, depositar_billetes_50, depositar_billetes_20,
                         depositar_billetes_10, depositar_billetes_5, depositar_billetes_2, depositar_billetes_1)
    else:
        posicion += 1
        return buscar_linea_en_cajero(cajero_seleccionado, posicion, depositar_billetes_100, depositar_billetes_50, depositar_billetes_20,
                         depositar_billetes_10, depositar_billetes_5, depositar_billetes_2, depositar_billetes_1)

def actualizar_billetes_denominacion(cajero_seleccionado, posicion, depositar_billetes_100, depositar_billetes_50, depositar_billetes_20,
                         depositar_billetes_10, depositar_billetes_5, depositar_billetes_2, depositar_billetes_1):
    actualizar_linea_cajero = open("lista_cajeros.txt", "r+")
    leer_linea_cajero = actualizar_linea_cajero.readlines()
    linea_cajero = leer_linea_cajero[posicion]
    linea_cajero = linea_cajero.replace("[", "")
    linea_cajero = linea_cajero.replace("]", "")
    linea_cajero = linea_cajero.replace("(", "")
    linea_cajero = linea_cajero.replace(")", "")
    linea_cajero = linea_cajero.replace("'", "")
    linea_cajero = linea_cajero.replace(" ", "")
    linea_cajero = linea_cajero.replace("\n", "")
    
    lista_linea_cajero = linea_cajero.split(",")
    
    
    lista_linea_cajero[3] = int(lista_linea_cajero[3])
    lista_linea_cajero[5] = int(lista_linea_cajero[5])
    lista_linea_cajero[7] = int(lista_linea_cajero[7])
    lista_linea_cajero[9] = int(lista_linea_cajero[9])
    lista_linea_cajero[11] = int(lista_linea_cajero[11])
    lista_linea_cajero[13] = int(lista_linea_cajero[13])
    lista_linea_cajero[15] = int(lista_linea_cajero[15])
    
    
    (lista_linea_cajero[3]) += int(depositar_billetes_100)
    (lista_linea_cajero[5]) += int(depositar_billetes_50)
    (lista_linea_cajero[7]) += int(depositar_billetes_20)
    (lista_linea_cajero[9]) += int(depositar_billetes_10)
    (lista_linea_cajero[11]) += int(depositar_billetes_5)
    (lista_linea_cajero[13]) += int(depositar_billetes_2)
    (lista_linea_cajero[15]) += int(depositar_billetes_1)
    
    actualizar_linea_cajero.close()
    return guardar_datos_lineas_cajero_deposito(0, '', cajero_seleccionado, lista_linea_cajero)

def guardar_datos_lineas_cajero_deposito(posicion_cajero, datos_cajero, cajero_seleccionado, lista_linea_cajero):
    reemplazar_linea_cajero = open("lista_cajeros.txt", "r")
    leer_linea_cajero1 = reemplazar_linea_cajero.readlines()
    reemplazar_linea_cajero.close()
    if posicion_cajero < len(leer_linea_cajero1):
        linea_revisar_deposito = leer_linea_cajero1[posicion_cajero]
        
        if cajero_seleccionado in linea_revisar_deposito:
            posicion_cajero += 1
            return guardar_datos_lineas_cajero_deposito(posicion_cajero, datos_cajero, cajero_seleccionado, lista_linea_cajero)
        else:
            datos_cajero_viejos = linea_revisar_deposito + '\n'
            datos_cajero += datos_cajero_viejos
            posicion_cajero += 1
            return guardar_datos_lineas_cajero_deposito(posicion_cajero, datos_cajero, cajero_seleccionado, lista_linea_cajero)
    else:
        datos_cajero += str(lista_linea_cajero)
        return actualizar_cajero_deposito(datos_cajero)
            

def actualizar_cajero_deposito(datos_cajero):
    '''
    '''
    archivo_cajeros_actualizado = open("lista_cajeros.txt", "a")
    # se utiliza truncate() para cambiar el tamaño del archivo
    # en este caso se asigna 0 para borrar todo
    archivo_cajeros_actualizado.truncate(0)
    # se escriben los datos de los cajeros actualizados
    archivo_cajeros_actualizado.write(datos_cajero)
    archivo_cajeros_actualizado.close()
   
    
def sumar_deposito_billetes(cajero_seleccionado, usuario_ingresando, depositar_billetes_100, depositar_billetes_50, 
                               depositar_billetes_20, depositar_billetes_10, depositar_billetes_5, depositar_billetes_2, 
                               depositar_billetes_1):
    '''
    '''
    monto_depositado = (int(depositar_billetes_100)*100) + (int(depositar_billetes_50)*50) + (int(depositar_billetes_20)*20) + \
    (int(depositar_billetes_10)*10) + (int(depositar_billetes_5)*5) + (int(depositar_billetes_2)*2) + (int(depositar_billetes_1)*1)
    return buscar_usuario_deposito(cajero_seleccionado, monto_depositado, usuario_ingresando, 0)

def buscar_usuario_deposito(cajero_seleccionado, monto_depositado, usuario_ingresando, posicion_usuario_linea):
    '''
    '''
    buscar_usuario_archivo = open("lista_usuarios.txt", "r+")
    leer_archivo_usuario = buscar_usuario_archivo.readlines()
    buscar_usuario_archivo.close()
    leer_usuario = leer_archivo_usuario[posicion_usuario_linea]
    if usuario_ingresando in leer_usuario:
        return guardar_deposito_usuario(monto_depositado, usuario_ingresando, posicion_usuario_linea)
    else:
        posicion_usuario_linea += 1
        return buscar_usuario_deposito(cajero_seleccionado, monto_depositado, usuario_ingresando, posicion_usuario_linea)
    
def guardar_deposito_usuario(cajero_seleccionado, monto_depositado, usuario_ingresando, posicion_usuario_linea):
    '''
    '''
    guardar_deposito_linea = open("lista_usuarios.txt", "r+")
    leer_linea_usuario_deposito = guardar_deposito_linea.readlines()
    linea_deposito_usuario = leer_linea_usuario_deposito[posicion_usuario_linea]
    linea_deposito_usuario = linea_deposito_usuario.replace("'", "")
    linea_deposito_usuario = linea_deposito_usuario.replace("[", "")
    linea_deposito_usuario = linea_deposito_usuario.replace("]", "")
    linea_deposito_usuario = linea_deposito_usuario.replace("(", "")
    linea_deposito_usuario = linea_deposito_usuario.replace(")", "")
    linea_deposito_usuario = linea_deposito_usuario.replace("\n", "")
    lista_usuario_str = linea_deposito_usuario.split(",")
    
    (lista_usuario_str[5]) = int(lista_usuario_str[5])
    (lista_usuario_str[5]) += monto_depositado
    
    monto = str(monto_depositado)
    # se concatenan para añadirlo al historial
    deposito = ' ' + '+' + monto
    hora = ' ' + time.asctime()
    cajero_deposito = ' ' + 'Acción realizada en cajero' + cajero_seleccionado
    if lista_usuario_str[7] == ' ':
        lista_usuario_str[7] = deposito 
        lista_usuario_str[7] += hora
        lista_usuario_str[7] += cajero_deposito
        print(lista_usuario_str)
    
    else:
        lista_usuario_str[7] += deposito 
        lista_usuario_str[7] += hora
        lista_usuario_str[7] += cajero_deposito 
        
    guardar_deposito_linea.close()
    return guardar_datos_usuarios(0, '', lista_usuario_str, usuario_ingresando)

def guardar_datos_usuarios(posicion_linea_usuario, datos_usuario_actualizados_deposito, lista_usuario_str, usuario_ingresando):
    guardar_lineas_usuarios = open("lista_usuarios.txt", "r")
    guardar_linea_usuario = guardar_lineas_usuarios.readlines()
    if posicion_linea_usuario < len(guardar_linea_usuario):
        linea_guardar_deposito = guardar_linea_usuario[posicion_linea_usuario]
        guardar_linea_usuario.close
        if usuario_ingresando in linea_guardar_deposito:
            posicion_linea_usuario +=1
            return guardar_datos_usuarios(posicion_linea_usuario, datos_usuario_actualizados_deposito, lista_usuario_str, usuario_ingresando)
        else:
            datos_usuario_deposito = str(linea_guardar_deposito) + '\n'
            datos_usuario_actualizados_deposito += datos_usuario_deposito
            posicion_linea_usuario += 1
            return guardar_datos_usuarios(posicion_linea_usuario, datos_usuario_actualizados_deposito, lista_usuario_str, usuario_ingresando)
    else:
        datos_usuario_actualizados_deposito += str(lista_usuario_str)
        return actualizar_usuario_deposito(datos_usuario_actualizados_deposito)

def actualizar_usuario_deposito(datos_usuario_actualizados_deposito):
    archivo_cajeros_actualizado = open("lista_usuarios.txt", "a")
    # se utiliza truncate() para cambiar el tamaño del archivo
    # en este caso se asigna 0 para borrar todo
    archivo_cajeros_actualizado.truncate(0)
    # se escriben los datos de los cajeros actualizados
    archivo_cajeros_actualizado.write(datos_usuario_actualizados_deposito)
    archivo_cajeros_actualizado.close()
    print("Querido usuario, el deposito se realizo de forma exitos")
    

#retiro de dinero

def retirar_dinero(cajero_seleccionado, usuario_ingresando):
    '''
    '''
    print('Por favor inserte la cantidad de billetes que desea retirar por denominación')
    
    retirar_billetes_100 = input('Introduzca la cantidad billetes de 100 que desea retirar')
    retirar_billetes_100 = int(retirar_billetes_100)

    retirar_billetes_50 = input('Introduzca la cantidad de billetes de 50 que desea retirar')
    retirar_billetes_50 = int(retirar_billetes_50)

    retirar_billetes_20 = input('Introduzca la cantidad de billetes de 20 que desea retirar')
    retirar_billetes_20 = int(retirar_billetes_20)

    retirar_billetes_10 = input('Introduzca la cantidad de billetes de 10 que desea retirar')
    retirar_billetes_10 = int(retirar_billetes_10)

    retirar_billetes_5 = input('Introduzca la cantidad de billetes de 5 que desea retirar')
    retirar_billetes_5 = int(retirar_billetes_5)

    retirar_billetes_2 = input('Introduzca la cantidad de billetes de 2 que desea retirar')
    retirar_billetes_2 = int(retirar_billetes_2)

    retirar_billetes_1 = input('Introduzca la cantidad de billetes de 1 que desea retirar')
    retirar_billetes_1 = int(retirar_billetes_1)

    buscar_linea_en_cajero_retiro(cajero_seleccionado, 0, retirar_billetes_100, retirar_billetes_50, retirar_billetes_20,
                           retirar_billetes_10, retirar_billetes_5, retirar_billetes_2, retirar_billetes_1)
    return sumar_retiro_billetes(cajero_seleccionado, usuario_ingresando, retirar_billetes_100, retirar_billetes_50, 
                                   retirar_billetes_20, retirar_billetes_10, retirar_billetes_5, retirar_billetes_2, 
                                   retirar_billetes_1)

def buscar_linea_en_cajero_retiro(cajero_seleccionado, posicion, retirar_billetes_100, retirar_billetes_50, retirar_billetes_20,
                         retirar_billetes_10, retirar_billetes_5, retirar_billetes_2, retirar_billetes_1):
    buscar_linea_archivo_retiro = open("lista_cajeros.txt", "r+")
    buscar_linea_cajero = buscar_linea_archivo_retiro.readlines()
    buscar_linea_archivo_retiro.close()
    linea_texto = buscar_linea_cajero[posicion]
    if(cajero_seleccionado in linea_texto):
        return actualizar_billetes_denominacion_retiro(cajero_seleccionado, posicion, retirar_billetes_100, retirar_billetes_50, retirar_billetes_20,
                         retirar_billetes_10, retirar_billetes_5, retirar_billetes_2, retirar_billetes_1)
    else:
        posicion += 1
        return buscar_linea_en_cajero_retiro(cajero_seleccionado, posicion, retirar_billetes_100, retirar_billetes_50, retirar_billetes_20,
                         retirar_billetes_10, retirar_billetes_5, retirar_billetes_2, retirar_billetes_1)

def actualizar_billetes_denominacion_retiro(cajero_seleccionado, posicion, retirar_billetes_100, retirar_billetes_50, retirar_billetes_20,
                         retirar_billetes_10, retirar_billetes_5, retirar_billetes_2, retirar_billetes_1):
    actualizar_linea_cajero = open("lista_usuarios.txt", "r+")
    leer_linea_cajero = actualizar_linea_cajero.readlines()
    linea_cajero = leer_linea_cajero[posicion]
    linea_cajero = linea_cajero.replace("[", "")
    linea_cajero = linea_cajero.replace("]", "")
    linea_cajero = linea_cajero.replace("(", "")
    linea_cajero = linea_cajero.replace(")", "")
    linea_cajero = linea_cajero.replace("'", "")
    linea_cajero = linea_cajero.replace(" ", "")
    linea_cajero = linea_cajero.replace("\n", "")
    
    lista_linea_cajero = linea_cajero.split(",")
    
    
    lista_linea_cajero[3] = int(lista_linea_cajero[3])
    lista_linea_cajero[5] = int(lista_linea_cajero[5])
    lista_linea_cajero[7] = int(lista_linea_cajero[7])
    lista_linea_cajero[9] = int(lista_linea_cajero[9])
    lista_linea_cajero[11] = int(lista_linea_cajero[11])
    lista_linea_cajero[13] = int(lista_linea_cajero[13])
    lista_linea_cajero[15] = int(lista_linea_cajero[15])
    
    
    (lista_linea_cajero[3]) -= int(retirar_billetes_100)
    (lista_linea_cajero[5]) -= int(retirar_billetes_50)
    (lista_linea_cajero[7]) -= int(retirar_billetes_20)
    (lista_linea_cajero[9]) -= int(retirar_billetes_10)
    (lista_linea_cajero[11]) -= int(retirar_billetes_5)
    (lista_linea_cajero[13]) -= int(retirar_billetes_2)
    (lista_linea_cajero[15]) -= int(retirar_billetes_1)
    
    actualizar_linea_cajero.close()
    return guardar_datos_lineas_cajero_retiro(0, '', cajero_seleccionado, lista_linea_cajero)

def guardar_datos_lineas_cajero_retiro(posicion_cajero, datos_cajero, cajero_seleccionado, lista_linea_cajero):
    reemplazar_linea_cajero_retiro = open("lista_cajeros.txt", "r")
    leer_linea_cajero1 = reemplazar_linea_cajero_retiro.readlines()
    reemplazar_linea_cajero_retiro.close()
    if posicion_cajero < len(leer_linea_cajero1):
        linea_revisar_deposito = leer_linea_cajero1[posicion_cajero]
        
        if cajero_seleccionado in linea_revisar_deposito:
            posicion_cajero += 1
            return guardar_datos_lineas_cajero_deposito(posicion_cajero, datos_cajero, cajero_seleccionado, lista_linea_cajero)
        else:
            datos_cajero_viejos = linea_revisar_deposito + '\n'
            datos_cajero += datos_cajero_viejos
            posicion_cajero += 1
            return guardar_datos_lineas_cajero_deposito(posicion_cajero, datos_cajero, cajero_seleccionado, lista_linea_cajero)
    else:
        datos_cajero += str(lista_linea_cajero)
        return actualizar_cajero_retiro(datos_cajero)
            

def actualizar_cajero_retiro(datos_cajero):
    '''
    '''
    archivo_cajeros_actualizado = open("lista_cajeros.txt", "a")
    # se utiliza truncate() para cambiar el tamaño del archivo
    # en este caso se asigna 0 para borrar todo
    archivo_cajeros_actualizado.truncate(0)
    # se escriben los datos de los cajeros actualizados
    archivo_cajeros_actualizado.write(datos_cajero)
    archivo_cajeros_actualizado.close()


def sumar_retiro_billetes(cajero_seleccionado, usuario_ingresando, retirar_billetes_100, retirar_billetes_50, 
                               retirar_billetes_20, retirar_billetes_10, retirar_billetes_5, retirar_billetes_2, 
                               retirar_billetes_1):
    '''
    '''
    monto_retirado = (int(retirar_billetes_100)*100) + (int(retirar_billetes_50)*50) + (int(retirar_billetes_20)*20) + \
    (int(retirar_billetes_10)*10) + (int(retirar_billetes_5)*5) + (int(retirar_billetes_2)*2) + (int(retirar_billetes_1)*1)
    return buscar_usuario_retiro(cajero_seleccionado, monto_retirado, usuario_ingresando, 0)

def buscar_usuario_retiro(cajero_seleccionado, monto_retirado, usuario_ingresando, posicion_usuario_linea):
    '''
    '''
    buscar_usuario_archivo_retiro = open("lista_usuarios.txt", "r+")
    leer_archivo_usuario_retiro = buscar_usuario_archivo_retiro.readlines()
    buscar_usuario_archivo_retiro.close()
    leer_usuario = leer_archivo_usuario_retiro[posicion_usuario_linea]
    if usuario_ingresando in leer_usuario:
        return guardar_retiro_usuario(monto_retirado, usuario_ingresando, cajero_seleccionado, posicion_usuario_linea)
    else:
        posicion_usuario_linea += 1
        return buscar_usuario_retiro(cajero_seleccionado, monto_retirado, usuario_ingresando, posicion_usuario_linea)
    
def guardar_retiro_usuario(monto_retirado, usuario_ingresando, cajero_seleccionado, posicion_usuario_linea):
    '''
    '''
    guardar_retiro_linea = open("lista_usuarios.txt", "r+")
    leer_linea_usuario_retiro = guardar_retiro_linea.readlines()
    linea_retiro_usuario = leer_linea_usuario_retiro[posicion_usuario_linea]
    linea_retiro_usuario = linea_retiro_usuario.replace("'", "")
    linea_retiro_usuario = linea_retiro_usuario.replace("[", "")
    linea_retiro_usuario = linea_retiro_usuario.replace("]", "")
    linea_retiro_usuario = linea_retiro_usuario.replace("(", "")
    linea_retiro_usuario = linea_retiro_usuario.replace(")", "")
    linea_retiro_usuario = linea_retiro_usuario.replace("\n", "")
    lista_usuario_hilera = linea_retiro_usuario.split(",")
    
    (lista_usuario_hilera[5]) = int(lista_usuario_hilera[5])
    (lista_usuario_hilera[5]) -= monto_retirado
    
    monto = str(monto_retirado)
    # se concatenan para añadirlo al historial
    retiro = ' ' + '-' + monto
    hora = ' ' + time.asctime()
    cajero_retiro = ' ' + 'Acción realizada en cajero' + cajero_seleccionado
    if lista_usuario_hilera[7] == ' ':
        lista_usuario_hilera[7] = retiro
        lista_usuario_hilera[7] += hora
        lista_usuario_hilera[7] += cajero_retiro
        print(lista_usuario_hilera)
    
    else:
        lista_usuario_hilera[7] += retiro 
        lista_usuario_hilera[7] += hora
        lista_usuario_hilera[7] += cajero_retiro
        
    guardar_retiro_linea.close()
    return guardar_datos_usuarios_retiro(0, '', lista_usuario_hilera, usuario_ingresando)

def guardar_datos_usuarios_retiro(posicion_linea_usuario, datos_usuario_actualizados_retiro, lista_usuario_hilera, usuario_ingresando):
    guardar_lineas_usuarios = open("lista_usuarios.txt", "r")
    guardar_linea_usuario = guardar_lineas_usuarios.readlines()
    if posicion_linea_usuario < len(guardar_linea_usuario):
        linea_guardar_retiro = guardar_linea_usuario[posicion_linea_usuario]
        guardar_linea_usuario.close
        if usuario_ingresando in linea_guardar_retiro:
            posicion_linea_usuario +=1
            return guardar_datos_usuarios_retiro(posicion_linea_usuario, datos_usuario_actualizados_retiro, lista_usuario_hilera, usuario_ingresando)
        else:
            datos_usuario_retiro = str(linea_guardar_retiro) + '\n'
            datos_usuario_actualizados_retiro += datos_usuario_retiro
            posicion_linea_usuario += 1
            return guardar_datos_usuarios(posicion_linea_usuario, datos_usuario_actualizados_retiro, lista_usuario_hilera, usuario_ingresando)
    else:
        datos_usuario_actualizados_retiro += str(lista_usuario_hilera)
        return actualizar_usuario_deposito(datos_usuario_actualizados_retiro)

def actualizar_usuario_retiro(datos_usuario_actualizados_retiro):
    archivo_cajeros_actualizado = open("lista_usuarios.txt", "a")
    # se utiliza truncate() para cambiar el tamaño del archivo
    # en este caso se asigna 0 para borrar todo
    archivo_cajeros_actualizado.truncate(0)
    # se escriben los datos de los cajeros actualizados
    archivo_cajeros_actualizado.write(datos_usuario_actualizados_retiro)
    archivo_cajeros_actualizado.close()
    print("Querido usuario, el deposito se realizo de forma exitos")
    
    
    
    
def consultar_saldo_usuario(usuario_ingresando, posicion_saldo_usuario):
    '''
    Funcion principal para mostrar historial de transacciones
    Parametros: La posicion a reccorrer las lineas y el usuario que ingresa
    Return: Saldo del usuario
    '''
    linea_saldo_usuario = open("lista_usuarios.txt", "r+")
    leer_saldo = linea_saldo_usuario.readlines()
    buscar_usuario_saldo = leer_saldo[posicion_saldo_usuario]
    buscar_usuario_saldo = buscar_usuario_saldo.replace("'", "")
    buscar_usuario_saldo = buscar_usuario_saldo.replace("[", "")
    buscar_usuario_saldo = buscar_usuario_saldo.replace("]", "")
    buscar_usuario_saldo = buscar_usuario_saldo.replace("   ", "")
    buscar_usuario_saldo = buscar_usuario_saldo.replace("  ", "")
    buscar_usuario_saldo = buscar_usuario_saldo.replace(" ", "")
    buscar_usuario_saldo = buscar_usuario_saldo.replace("\n", "")
    linea_con_saldo = buscar_usuario_saldo.split(",")
    if usuario_ingresando in linea_con_saldo:
        print("Monto de la cuenta: ", linea_con_saldo[5])
    else:
        posicion_saldo_usuario +=1
        return  consultar_saldo_usuario(usuario_ingresando, posicion_saldo_usuario)

    
def consultar_historial_transacciones(usuario_ingresando, posicion_historial_usuario):
    '''
    Funcion principal para mostrar el historial de transacciones
    Parametros: 
    Return: Historial de transacciones del usuario
    '''
    linea_historial_usuario = open("lista_usuarios.txt", "r+")
    leer_historial = linea_historial_usuario.readlines()
    buscar_usuario_historial = leer_historial[posicion_historial_usuario]
    buscar_usuario_historial = buscar_usuario_historial.replace("'", "")
    buscar_usuario_historial = buscar_usuario_historial.replace("[", "")
    buscar_usuario_historial = buscar_usuario_historial.replace("]", "")
    buscar_usuario_historial = buscar_usuario_historial.replace("   ", "")
    buscar_usuario_historial = buscar_usuario_historial.replace("  ", "")
    buscar_usuario_historial = buscar_usuario_historial.replace(" ", "")
    buscar_usuario_historial = buscar_usuario_historial.replace("\n", "")
    linea_con_historial = buscar_usuario_historial.split(",")
    if usuario_ingresando in linea_con_historial:
        print("Historial de transacciones: ", linea_con_historial[7])
    else:
        posicion_historial_usuario +=1
        return  consultar_historial_transacciones(usuario_ingresando, posicion_historial_usuario)


          