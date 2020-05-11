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
    polly = Polly(AWSsesion, rutaCatkin+'/audios')
    polly.generarAudio(goal.texto, goal.nombreArchivo)
    polly.reproducirAudio(goal.nombreArchivo)


# ----------------------------------------------------------------------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------------------------------------------------------------------- 
rospy.init_node('aws_polly_action')
server = actionlib.SimpleActionServer('awsPolly', AwsPollyAction, callbackAwsPolly, False) # creamos el servidor de la accion
# Los parametros son: nombre del servidor, tipo de la accion, funcion a ejecutar y variable que posibilita el inicio atomatico del servidor
server.start() # iniciamos el servidor
rospy.loginfo("Lanzamos el servidor aws_polly_action")
rospy.spin() # el server queda a la espera de recibir el goal

