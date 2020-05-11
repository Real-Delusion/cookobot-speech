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
    "ASIA5U2MF2VW7DKFHD43",
    "sgdG+S3NEW+Vm+SM77J//yGxPe1zaUPxXNYHXNvD",
    "FwoGZXIvYXdzEPP//////////wEaDMvy/43PX6ewqTLDlSLCAUtpvPifrCOG1QUk+RqOCgrSIlKwCc6MZIHCqNeG74SsXkenbmQkeYnj0ykyZC4Tk04LkghudFDjdPo1waAvusg5/WYW2QALNzsSJ2Fx/z6TyUm+nHaDxwTudfdvZYsMfB7lf1CyfmN9xW4D9rkmOsimneWiDo78SskPCo5KRbc4iuVcWMdXIrU/ykMtTjfiC6PywBYcI/0DjXBic5avzurYyuX8Pu+rzh6idmnz/wXCk7lvSu76LJKHdYxla3mMORFIKL6y5PUFMi1Ig5rHEMZeM71hiTA8xpFxUnoDmWSKRWRlHixPHacCK733oUPb8DnpdKeA47A=",
]

# ----------------------------------------------------------------------------------------------------------------------------------------
# Funcion timer que se ejecuta al recibir el goal
# ----------------------------------------------------------------------------------------------------------------------------------------
def callbackAwsPolly(goal):
    polly = Polly(AWSsesion, rutaCatkin+'/audios')
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
        print("Error: no se ha seleccionado ninguna hación a realizar con el audio")


# ----------------------------------------------------------------------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------------------------------------------------------------------- 
rospy.init_node('aws_polly_action')
server = actionlib.SimpleActionServer('awsPolly', AwsPollyAction, callbackAwsPolly, False) # creamos el servidor de la accion
# Los parametros son: nombre del servidor, tipo de la accion, funcion a ejecutar y variable que posibilita el inicio atomatico del servidor
server.start() # iniciamos el servidor
rospy.loginfo("Lanzamos el servidor aws_polly_action")
rospy.spin() # el server queda a la espera de recibir el goal

