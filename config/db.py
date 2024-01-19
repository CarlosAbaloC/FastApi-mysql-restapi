#Con sqlalchemy puedeshacer que todas las bbdd funcionen igual
from sqlalchemy import create_engine, MetaData 

engine = create_engine("mysql+pymysql://carlosabalo:carlosabalo@db4free.net/carlosabalodaw")
#engine = create_engine("mysql+pymysql://eloycn:palomeras@db4free.net/gestionjugador")

meta = MetaData()

conn = engine.connect()