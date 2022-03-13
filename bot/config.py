from os import getenv

# TELEGRAM
OWNER = int(getenv('OWNER'))
if OWNER is None:
    raise Exception("Por favor configura tu Telegram User ID") 

API_ID = int(getenv('API_ID'))
if API_ID is None:
    raise Exception("Por favor configura el API_ID del Bot") 

API_HASH = getenv('API_HASH')
if API_HASH is None:
    raise Exception("Por favor configura el API_HASH del Bot") 

TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN')
if TELEGRAM_TOKEN is None:
    raise Exception("Por favor configura el TOKEN del Bot") 

# DATOS DEL MOODLE
HOST = getenv('HOST')
if HOST is None:
    raise Exception("Por favor configura la URL del Moodle") 

ACCOUNT = getenv('ACCOUNT')
if ACCOUNT is None:
    raise Exception("Por favor configura tu nombre de usuario del Moodle") 

PASSWORD = getenv('PASSWORD')
if PASSWORD is None:
    raise Exception("Por favor configura tu contraseña del Moodle") 

# CUENTA DE MEGA
PASS_MEGA = getenv('PASS_MEGA')
if PASS_MEGA is None:
    raise Exception("Por favor configura tu contraseña de GMAIL") 

GMAIL_MEGA = getenv('GMAIL_MEGA')
if GMAIL_MEGA is None:
    raise Exception("Por favor configura tu correo de GMAIL") 

# ARCHIVOS
MEGABYTES = int(getenv('MEGABYTES'))
if MEGABYTES is None:
    raise Exception("Por favor configura los MEGABYTES a los que se dividirán los archivos") 