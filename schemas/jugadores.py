from pydantic import BaseModel
from typing import Optional
from datetime import date

class Jugador(BaseModel):
    id: Optional[int]
    nombre: str
    fecha: date
    detalles: str
    altura: int