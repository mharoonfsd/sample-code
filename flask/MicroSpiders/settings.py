"""Settings for the Microspiders."""

from decouple import config

DEBUG = config('DEBUG', cast=bool)

SERVER = {
    "host": config('SERVER_HOST', cast=str),
    "port": config('SERVER_PORT', cast=int)    
}

