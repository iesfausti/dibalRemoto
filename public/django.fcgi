#!/home/febal/.virtualenvs/febal/bin/python
import os, sys

_PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_PROJECT_NAME = _PROJECT_DIR.split('/')[-1]

sys.path.insert(0, _PROJECT_DIR)
sys.path.insert(0, os.path.dirname(_PROJECT_DIR))

os.environ['DJANGO_SETTINGS_MODULE'] = "%s.settings" % _PROJECT_NAME

os.chdir(_PROJECT_DIR)

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
