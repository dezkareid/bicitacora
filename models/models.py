from google.appengine.ext import db
from google.appengine.api import users

class Ciclista(db.Model):
	"""Entidad para administrar a los Ciclistas que usen la aplicacion"""
	nombre = db.StringProperty(required=True)
	facebook = db.LinkProperty(required=True)
	twitter = db.StringProperty(required=True)
	es_hombre = db.BooleanProperty(default=True)
	fecha_nacimiento = db.DateProperty()
	fecha_registro = db.DateProperty(auto_now_add=True)
	usuario = db.UserProperty()

class Ruta(db.Model):
	"""Entidad para guardar una Ruta"""
	nombre = db.StringProperty(required=True)
	puntos = db.ListProperty(db.GeoPt,default=[])
	inicio = db.DateTimeProperty(required=True,auto_now_add=True)
	termino = db.DateTimeProperty(required=True,auto_now_add=True)
	ciclista = db.ReferenceProperty(Ciclista)

class Tipo_Lugar(db.Model):
	"""Entidad para guardar los tipos de lugares"""
	tipo = db.StringProperty(required=True)

class Lugar(db.Model):
	"""Entidad para guardar lugares de interes para los ciclistas: talleres, biciestacionamientos,etc."""
	nombre = db.StringProperty(required=True)
	tipo = db.ReferenceProperty(Tipo_Lugar)
	descripcion = db.TextProperty(required=True)
	direccion = db.StringProperty(required=True)
	alta = db.DateProperty(auto_now_add=True)
	ubicacion = db.GeoPtProperty()

class Tipo_Suceso(db.Model):
	"""Entidad que identifica a los tipos de sucesos: Manifestaciones, bloqueos, composturas de calle"""
	tipo = db.StringProperty(required=True)
	duracion = db.IntegerProperty(required=True)

class Suceso(db.Model):
	"""Entidad para reportar los tipos de sucesos que pueden haber en la ruta del ciclista"""
	tipo = db.ReferenceProperty(Tipo_Suceso)
	descripcion = db.TextProperty(required=True)
	alta = db.DateTimeProperty(auto_now_add=True)
	ubicacion = db.GeoPtProperty()	