# -----------------------------------------------------------------------------
# Nombre del Programa : Sistema de Gestión de Consultorio Médico
# Nombre del Módulo   : settings.py
# Función del Archivo : Configuración global del proyecto Django, incluyendo base de datos, apps, seguridad, rutas, etc.
# Programador         : Neyder Sebastian Orozco Villamil
# Fecha               : 22/05/2025
# Versión             : 1.0
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# IMPORTACIÓN DE MÓDULOS NECESARIOS
# -----------------------------------------------------------------------------
from pathlib import Path
import os
import mysql  # Puede omitirse si no se usa directamente en este archivo

# -----------------------------------------------------------------------------
# DEFINICIÓN DE LA RUTA BASE DEL PROYECTO
# -----------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE SEGURIDAD Y DEBUG
# -----------------------------------------------------------------------------
SECRET_KEY = 'django-insecure-2)+&c17p%b8l^al4s101pxyq=90r$f#*y0o@h*%+b_v^laoar6'
DEBUG = True
ALLOWED_HOSTS = []

# -----------------------------------------------------------------------------
# DEFINICIÓN DE LAS APLICACIONES INSTALADAS
# Incluye tanto las apps propias como las del sistema
# -----------------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Aplicaciones del sistema
    'mainpage',
    'usuarios',
    'pacientes',
    'doctores',
    'secretaria',
]

# -----------------------------------------------------------------------------
# MIDDLEWARE
# Define los componentes que procesan las solicitudes/respuestas del sistema
# -----------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE URL PRINCIPAL
# -----------------------------------------------------------------------------
ROOT_URLCONF = 'consultorio_medico.urls'

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE PLANTILLAS HTML
# -----------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Directorio para templates globales
        'APP_DIRS': True,  # Permite buscar templates en cada aplicación
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DEL WSGI
# -----------------------------------------------------------------------------
WSGI_APPLICATION = 'consultorio_medico.wsgi.application'

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE LA BASE DE DATOS
# Se utiliza MySQL como motor principal de persistencia
# -----------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'consultorio',
        'USER': 'admin',
        'PASSWORD': 'NeySeb832',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# -----------------------------------------------------------------------------
# VALIDADORES DE CONTRASEÑAS
# -----------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# -----------------------------------------------------------------------------
# CONFIGURACIÓN INTERNACIONALIZACIÓN Y ZONA HORARIA
# -----------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS
# -----------------------------------------------------------------------------
STATIC_URL = 'static/'

# -----------------------------------------------------------------------------
# TIPO DE CLAVE PRIMARIA POR DEFECTO
# -----------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE AUTENTICACIÓN Y REDIRECCIÓN
# -----------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/redirigir/'       # Redirige según el rol del usuario después del login
LOGOUT_REDIRECT_URL = 'home'             # Redirige a la página principal tras cerrar sesión
