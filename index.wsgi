import sae
from haidaoteam import wsgi

application = sae.create_wsgi_app(wsgi.application)