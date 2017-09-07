activate_this = '/path/to/instrumentgarage/venv/bin/activate_this.py' 
execfile(activate_this, dict(__file__=activate_this))
import sys
sys.path.insert(0,"/path/to/instrumentgarage/")
from catalog import app as application
