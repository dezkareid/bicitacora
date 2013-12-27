from google.appengine.ext import db
from google.appengine.api import users

class Ciclista(db.Model):
	"""Ciclista"""
	nombre = db.StringProperty(required=True)
    facebook = db.LinkProperty(required=True)
    twitter = db.LinkProperty(required=True)
    es_hombre = db.BooleanProperty(default=True)
    fecha_nacimiento = db.DateProperty()
    fecha_registro = db.DateProperty()
    usuario = db.UserProperty()

class Ruta(db.Model):
	"""docstring for Ruta"""
	nombre = db.StringProperty(required=True)
	puntos = db.ListProperty(db.GeoPt,default=[])
	inicio = db.DateTimeProperty(required=True,auto_now_add=True)
	termino = db.DateTimeProperty(required=True,auto_now_add=True)
	ciclista = db.ReferenceProperty(Ciclista)

class Tipo_Lugar(db.Model):
	"""docstring for Tipo_Lugar"""
	tipo = db.StringProperty(required=True)

class Lugar(db.Model):
	"""docstring for Lugar"""
	nombre = db.StringProperty(required=True)
	tipo = db.ReferenceProperty(Tipo_Lugar)
	descripcion = db.TextProperty()
	direccion = db.StringProperty(required=True)
	alta = db.DateProperty(auto_now_add=True)
	ubicacion = db.GeoPt()

class Tipo_Suceso(db.Model):
	"""docstring for Tipo_Lugar"""
	tipo = db.StringProperty(required=True)
	duracion = db.IntegerProperty()

class Suceso(db.Model):
	"""docstring for Suceso"""
	tipo = db.ReferenceProperty(Tipo_Suceso)
	descripcion = db.TextProperty()
	alta = db.DateTimeProperty(auto_now_add=True)
	ubicacion = db.GeoPt()	