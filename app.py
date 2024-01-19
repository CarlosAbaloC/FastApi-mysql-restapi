from fastapi import FastAPI
from rutas.jugadores import jugador
#Iniciar un servidor
app = FastAPI(
    openapi_tags=[{
        "name": "jugadores",
        "description": "rutas jugadores"
    }]
)

#Para que la app incluya las rutas que le envias desde jugador
app.include_router(jugador)