import boto3

# ----------------------------------------------------------------------------------------------------------------------------------------
# Variables globales temporales
# ----------------------------------------------------------------------------------------------------------------------------------------
# AWSsesion = [
#     "ASIA5U2MF2VW4QGB3Z7Y",
#     "drlOlr4/ikNp4WC1NLDE9/GMXPB4QClRw86VG+Sp",
#     "FwoGZXIvYXdzEOT//////////wEaDJrmxU76MHr8OavbMiLCAeZnJ/zEdGEi/p6B/9ORWV0cr58L+sxyXdSbjaP9YF/pB8mGqIe95xjwEuMY9AhxuNGMiE7z5wnAnEPTosmtDfzdcvJo+FBdXKtQ4rtrKdJKeAN5qZ1958BvP6eXxvq0nU8dP3KRHDCMWO1WtY+041PuZfPoKDF31Ms110om8PsejfLSmBKnJ1vfxlsBmhragJkYu4xHCVpFyTFEshUorPd3RD4+XRre2RUDQ7SQNxh1OdcFKF0jtRtD4OdQjKDUVaUGKLiJ4fUFMi3Tr+IMZNZgA9gIHE23wTVqF43KagxtG2qQ6lN0+z5utHJh2JuB3o6XFnT6+ww=",
# ]

class Polly():
    def __init__(self, awsSession, rutaFicheroPistas):
        self.awsSession = awsSession
        # Propiedades configurables del servicio
        # Ruta donde se guardaran las pistas
        self.rutaFicheroPistas = rutaFicheroPistas 
        # Voz que se usará por defecto 
        self.vozId = 'Conchita'
        # Formato en el que se genera la pista de audio pr defecto
        self.outputFormat = "mp3"
        
        
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
        
        file = open(archivo, 'wb')
        file.write(response['AudioStream'].read())
        file.close()
        
        self.pistasDeAudio[nombreArchivo] = response['AudioStream']
    
    # Metodo que reproduce la pista
    def reproducirAudio(self,nombreArchivo):
        archivo = self.rutaFicheroPistas+"/"+nombreArchivo
        
        print("Play Sound")


# Exmaple
# polly = Polly(AWSsesion, './../audios')
# polly.generarAudio("Hola, me ha generado la clase Polly", "clase.mp3")
# polly.reproducirAudio("clase.mp3")