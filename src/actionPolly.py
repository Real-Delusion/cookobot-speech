#! /usr/bin/env python

# ----------------------------------------------------------------------------------------------------------------------------------------
# Real Delusion Robotics
# Cookobot-speech
# Autor: Alejandro Mira Abad
# ----------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------------------------------------------------------------------
import rospy

import time # contiene funciones para operar con tiempos
import actionlib # contiene la clase SimpleActionServer
from cookobot_speech.msg import AwsPollyAction, AwsPollyGoal, AwsPollyResult, AwsPollyFeedback
from polly import Polly
import os

os.chdir("..")
rutaCatkin = os.getcwd()+"/catkin_ws/src/cookobot_speech/src"
# ----------------------------------------------------------------------------------------------------------------------------------------
# Variables globales temporales
# ----------------------------------------------------------------------------------------------------------------------------------------
AWSsesion = [
    "",
    "",
    "",
]

# ----------------------------------------------------------------------------------------------------------------------------------------
# Funcion timer que se ejecuta al recibir el goal
# ----------------------------------------------------------------------------------------------------------------------------------------
def callbackAwsPolly(goal):
    try:
        # Generar audio
        if goal.funcion == 1:
            polly.generarAudio(goal.texto, goal.nombreArchivo)
        # Escuchar audio
        elif goal.funcion == 2:
            polly.reproducirAudio(goal.nombreArchivo)
        # Borrar audio
        elif goal.funcion == 3:
            polly.borrarAudio(goal.nombreArchivo)
        # Error
        else:
            print("Error: no se ha seleccionado ninguna hacion a realizar con el audio")
        
        result = AwsPollyResult() # se construye el mensaje de respuesta
        result.success = True
        server.set_succeeded(result) # se ha ennviado el goal OK
    except:
        result = AwsPollyResult() # se construye el mensaje de respuesta
        result.success = False
        server.set_succeeded(result) # se ha ennviado el goal OK


# ----------------------------------------------------------------------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------------------------------------------------------------------- 
rospy.init_node('aws_polly_action')
server = actionlib.SimpleActionServer('awsPolly', AwsPollyAction, callbackAwsPolly, False) # creamos el servidor de la accion
# Los parametros son: nombre del servidor, tipo de la accion, funcion a ejecutar y variable que posibilita el inicio atomatico del servidor
server.start() # iniciamos el servidor
rospy.loginfo("Lanzamos el servidor aws_polly_action")
polly = Polly(AWSsesion, rutaCatkin+'/audios') # Ejecutamos el contructor de polly
rospy.spin() # el server queda a la espera de recibir el goal

