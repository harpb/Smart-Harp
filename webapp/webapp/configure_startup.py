import os, settings, sys

def set_prod():
    settings.DEBUG = False
    settings.TEMPLATE_DEBUG = False
    pass

def set_test():
    settings.DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
        
def set_local():
    pass
    
#===============================================================================
# CONFIGURE environment
#===============================================================================
#from pprint import pprint
#pprint( os.environ.items() )
settings.SERVER_ENVIRONMENT = os.environ.get('SERVER_ENVIRONMENT', 'LOCAL')
for arg in sys.argv:
    if 'test' in arg or 'nose' in arg:
        settings.SERVER_ENVIRONMENT = 'TEST'
        break
    
def configure(environment_type):
    settings.SERVER_ENVIRONMENT = environment_type.upper()
#    print r"settings.SERVER_ENVIRONMENT: '%s'" % settings.SERVER_ENVIRONMENT
    if 'PROD' in settings.SERVER_ENVIRONMENT:
        set_prod()
    elif 'TEST' in settings.SERVER_ENVIRONMENT:
        set_test()
    else:
        set_local()
configure(settings.SERVER_ENVIRONMENT)
