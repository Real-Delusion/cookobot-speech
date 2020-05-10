#! /usr/bin/env python

# ----------------------------------------------------------------------------------------------------------------------------------------
# Clases ROS
# Ejercicio action
# Alejandro Mira Abad
# ----------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------------------------------------------------------------------
import rospy

import time # contiene funciones para operar con tiempos
import actionlib # contiene la clase SimpleActionServer
from cookobot_speech.msg import AwsPollyAction, TimerGoal, TimerResult, TimerFeedback

# ----------------------------------------------------------------------------------------------------------------------------------------
# Funcion timer que se ejecuta al recibir el goal
# ----------------------------------------------------------------------------------------------------------------------------------------
def callbackAwsPolly(goal):
    pass


# ----------------------------------------------------------------------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------------------------------------------------------------------- 
rospy.init_node('aws_polly_action')
server = actionlib.SimpleActionServer('timer', AwsPollyAction, callbackAwsPolly, False) # creamos el servidor de la accion
# Los parametros son: nombre del servidor, tipo de la accion, funcion a ejecutar y variable que posibilita el inicio atomatico del servidor
server.start() # iniciamos el servidor
rospy.loginfo("Lanzamos el servidor aws_polly_action")
rospy.spin() # el server queda a la espera de recibir el goal

