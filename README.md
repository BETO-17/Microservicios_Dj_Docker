# Sala-24-BK-F-Docker-GIT

#  Laboratorio de Microservicios (Django + React)

##  Día 1 — Fundamentos + Entorno Docker / Git

###  Objetivo
Comprender qué es una arquitectura de microservicios y preparar el entorno de trabajo para los siguientes días.  
El objetivo es terminar con una base funcional usando Docker Compose, donde cada servicio se pueda levantar de forma independiente.

---

##  Arquitectura inicial

```
microservices-lab/
│
├── auth-service/       # Servicio de autenticación (JWT)
├── blog-service/       # Gestión de publicaciones, autores y categorías
├── email-service/      # Envío de correos y formularios
├── frontend/           # Interfaz de usuario en React
├── reverse-proxy/      # Proxy inverso y gateway local
├── docker-compose.yml  # Orquestador de contenedores
├── .env.example        # Variables de entorno base
└── README.md           # Documentación del proyecto
```
---
# Crear estructura base del proyecto
```
mkdir microservices-lab
cd microservices-lab
mkdir auth-service blog-service email-service frontend reverse-proxy

# Crear README.md en cada carpeta de servicio
touch auth-service/README.md blog-service/README.md email-service/README.md frontend/README.md reverse-proxy/README.md
```
---
Inicializar Git y subir al repositorio
```
git init
git branch -M main  o  git checkout -b "tu rama"
git add .  o   por archivo    git add "nombre"
git commit -m "Estructura inicial del laboratorio de microservicios"

# Enlazar con el repositorio remoto
git remote add origin https://github.com/camananick-a11y/Sala-24-BK-F-Docker-GIT.git
git push -u origin main
```
---
Crear docker-compose.yml
```
version: "3.9"
services:
  postgres:
    image: postgres:15
    container_name: db_postgres
    restart: always
    environment:
      POSTGRES_USER: devuser
      POSTGRES_PASSWORD: devpass
      POSTGRES_DB: main_db
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7
    container_name: cache_redis
    restart: always
    ports:
      - "6379:6379"

volumes:
  pgdata:
```
---
Crear archivo .env.example
```
POSTGRES_USER=devuser
POSTGRES_PASSWORD=devpass
POSTGRES_DB=main_db
REDIS_HOST=redis
REDIS_PORT=6379
```
---
```
Verificación del entorno
Ejecutar los contenedores:

docker compose up -d
docker ps
```
