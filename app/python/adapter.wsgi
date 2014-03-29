import sys, os, bottle

sys.path = ['C:\\Users\\geoimages\\angular-seed\\app\\python\\'] + sys.path
os.chdir(os.path.dirname(__file__))
import Bottle500 # This loads your application
application = bottle.default_app()