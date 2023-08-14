import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import requests  # Importa la librería requests

# Incluir el pin del relé
relay = 26

# Incluir el pin del buzzer
buzzer_pin = 24

# Incluir los pines para los LEDs rojo y verde
led_rojo_pin = 21
led_verde_pin = 16

# Obtiene los IDs y nombres de las tarjetas desde la API
response = requests.get('http://127.0.0.1:5000/tarjetas')
tag_data = response.json()

# Extrae los IDs y nombres de las tarjetas y almacénalos en Tag_IDs y Tag_Nombres
Tag_IDs = [entry['id'] for entry in tag_data]
#Tag_id_user = [entry['user_id'] for entry in tag_data]
#Tag_Nombres = [entry['nombre_usuario'] for entry in tag_data]
#Tag_Id_usuario = [entry['id_usuario'] for entry in tag_data]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(relay, GPIO.OUT)
GPIO.setup(led_rojo_pin, GPIO.OUT)
GPIO.setup(led_verde_pin, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)

# Crear objeto lector
reader = SimpleMFRC522()

def close_door():
    GPIO.output(relay, GPIO.LOW)
    
def encender_led_rojo():
    GPIO.output(led_rojo_pin, GPIO.HIGH)
    GPIO.output(led_verde_pin, GPIO.LOW)

def encender_led_verde():
    GPIO.output(led_verde_pin, GPIO.HIGH)
    GPIO.output(led_rojo_pin, GPIO.LOW)

def apagar_leds():
    GPIO.output(led_rojo_pin, GPIO.LOW)
    GPIO.output(led_verde_pin, GPIO.LOW)

def encender_buzzer():
    GPIO.output(buzzer_pin, GPIO.HIGH)

def apagar_buzzer():
    GPIO.output(buzzer_pin, GPIO.LOW)

door_open = False

try:
    while True:
        time.sleep(0.5)
        # Leer tarjeta -> id(ns) text (almacena)
        id, tag = reader.read_no_block()
        id = str(id).strip() 
        
        if id != "None":
            index = Tag_IDs.index(id) if id in Tag_IDs else -1
        
            if index != -1 and not door_open:
                #nombre_usuario = Tag_Nombres[index]
                #user_id = Tag_id_user[index]
                assoc_id = Tag_IDs [index]
                print("Bienvenido")
                print("ID:", id)
                
                
                # Crea el registro en la base de datos usando la API
                registro_data = {
                "assoc_id": assoc_id,  #  ID del usuario
                #"created_at": time.strftime('%Y-%m-%d %H:%M:%S')
                }
                
                registro_response = requests.post('http://127.0.0.1:5000/registro_acceso', json=registro_data)
                try:
                    print(registro_response.json())  # Intenta imprimir la respuesta de la API
                except Exception as json_err:
                    print("Error al decodificar la respuesta JSON:", json_err)

                
                encender_led_verde()
                encender_buzzer()
                GPIO.output(relay, GPIO.HIGH)
                print("Puerta abierta")
                door_open = True
                # Esperar 2 segundos y luego cerrar la puerta
                time.sleep(2)
                close_door()
                door_open = False
                apagar_buzzer()
                print("Puerta cerrada")
                apagar_leds()
                
            else:
                print("Tarjeta no reconocida")
                encender_led_rojo()
                time.sleep(2)  # tiempo de encendido del led rojo
                apagar_leds()
                
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
finally:
    GPIO.cleanup()
