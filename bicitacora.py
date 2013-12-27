import cgi
import os

from google.appengine.ext.webapp import template

from google.appengine.api import users
from google.appengine.ext import db

import webapp2
from models.models import *

class MainPage(webapp2.RequestHandler):
  def get(self):
  	template_values = {'titulo': 'Taller app engine','encabezado': 'Hola :3'}
  	path = os.path.join(os.path.dirname(__file__), 'templates','index.html')
  	self.response.out.write(template.render(path, template_values))
#    rutas = Ruta.all()

app = webapp2.WSGIApplication([('/', MainPage)])

class Estadisticas(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('Hello, Estadisticas World!')

est = webapp2.WSGIApplication([('/estadisticas', Estadisticas)])