from fastapi import APIRouter, Response, status
from config.db import conn
#Jugadores es la tabla en la que se guardan los datos
from models.jugadores import jugadores
import base64
from schemas.jugadores import Jugador
from fastapi import HTTPException
from starlette.status import HTTP_204_NO_CONTENT

jugador = APIRouter()

#Poner la ruta donde tienes que ir para sacar a los jugadores
@jugador.get("/jugadores", response_model=list[Jugador], tags=["jugadores"])
def get_jugadores():
    #Coge todos(fetch_all) los elementos de la tabla jugadores
    return conn.execute(jugadores.select()).fetchall()


@jugador.post("/jugadores", response_model=Jugador, tags=["jugadores"])
def crearJugador(jugador: Jugador):
    nuevoJugador = {"nombre": jugador.nombre, "fecha": jugador.fecha, "detalles": jugador.detalles, 
                    "altura": jugador.altura}
    try:
        resultado = conn.execute(jugadores.insert().values(nuevoJugador))
        conn.commit() 
        nuevo_id = resultado.lastrowid
        print(f"ID del nuevo jugador: {nuevo_id}")
        # Obtener el jugador recién creado de la base de datos
        jugador_creado = conn.execute(jugadores.select().where(jugadores.c.id == nuevo_id)).fetchone()
        
        return jugador_creado
    except Exception as e:
        print(f"Error al insertar en la base de datos: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al insertar en la base de datos: {str(e)}")


@jugador.get("/jugadores/{id}", response_model=Jugador, tags=["jugadores"])
def get_jugador(id: str):
    print(id)
    # Corregir el uso del operador '/' a '.'
    result = conn.execute(jugadores.select().where(jugadores.c.id == id))
    # Obtener la fila de resultados usando fetchone()
    row = result.fetchone()
    # Devolver el objeto del modelo Jugador
    return row


@jugador.delete("/jugadores/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["jugadores"])
def delete_jugador(id: str):
    result = conn.execute(jugadores.delete().where(jugadores.c.id==id))
    conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

@jugador.put("/jugadores/{id}", response_model=Jugador, tags=["jugadores"])
def update_jugador(id: str, jugador: Jugador):
    conn.execute(jugadores.update().values(nombre=jugador.nombre, fecha=jugador.fecha, 
                                            detalles=jugador.detalles, 
                                            altura=jugador.altura).where(jugadores.c.id == id))
    conn.commit()
    # Devuelve el jugador actualizado
    return conn.execute(jugadores.select().where(jugadores.c.id == id)).fetchone()