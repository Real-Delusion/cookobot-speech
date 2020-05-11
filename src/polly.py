import boto3
import pygame
import time


class Polly:

    def __init__(self, awsSession, rutaFicheroPistas):
        self.awsSession = awsSession
        # Propiedades configurables del servicio
        # Ruta donde se guardaran las pistas
        self.rutaFicheroPistas = rutaFicheroPistas 
        
        # Voz que se usara por defecto 
        self.vozId = 'Conchita'
        # Formato en el que se genera la pista de audio pr defecto
        self.outputFormat = "ogg_vorbis"
        
        # Creamos la sesion de AWS
        session = boto3.Session( 
                        aws_access_key_id= self.awsSession[0], 
                        aws_secret_access_key= self.awsSession[1],
                        aws_session_token= self.awsSession[2],
                        region_name='us-east-1')

        # Accedemos al servicio Polly
        self.polly_client = session.client('polly')
    
    
    def configurarVoz(self, vozId, outputFormat):
        self.vozId = vozId
        self.outputFormat = outputFormat
        
    # Metodo que genera una pista de audio a partir de un texto
    def generarAudio(self, texto, nombreArchivo):
        response = self.polly_client.synthesize_speech(
                VoiceId=self.vozId,
                # Engine="neural",
                OutputFormat=self.outputFormat, 
                Text = texto)

        archivo = self.rutaFicheroPistas+"/"+nombreArchivo
        
        print(archivo)
        file = open(archivo, 'wb')
        file.write(response['AudioStream'].read())
        file.close()
        
        # self.pistasDeAudio[nombreArchivo] = response['AudioStream']
    
    # Metodo que reproduce la pista
    def reproducirAudio(self,nombreArchivo):
        archivo = self.rutaFicheroPistas+"/"+nombreArchivo
        
        print(archivo)
        
        print("Play Sound")
        pygame.init()
        sound = pygame.mixer.Sound(archivo)
        clock = pygame.time.Clock()
        sound.play()
        time.sleep(sound.get_length() + 0.5)
        pygame.quit()


# Exmaple
# polly = Polly(AWSsesion, './../audios')
# polly.generarAudio("Hola, me ha generado la clase Polly", "clase.mp3")
# polly.reproducirAudio("clase.mp3")