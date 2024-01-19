from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date, BLOB
from config.db import meta, engine

#La tabla tiene tres elementos, el nombre de la tabla
#La propiedad meta, para que sqlalchemy pueda saber mas datos de la tabla
#Define la tabla jugadores
jugadores = Table("jugadores", meta, 
                    Column("id", Integer, primary_key = True, autoincrement= True),
                    Column("nombre", String(40) ),
                    Column("fecha", Date ),
                    Column("detalles", String(100) ),
                    Column("altura", Integer )
                  )
meta.create_all(engine)
