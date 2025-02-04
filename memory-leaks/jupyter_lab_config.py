import getpass
from tempfile import mkdtemp

# Test if we are running in a docker
if getpass.getuser() == "jovyan":
    c.ServerApp.ip = "0.0.0.0"

c.ServerApp.port = 9999
c.ServerApp.open_browser = False

c.ServerApp.root_dir = mkdtemp(prefix='memory-leak-lab-')

c.ServerApp.token = ""
c.ServerApp.password = ""
c.ServerApp.disable_check_xsrf = True

c.LabApp.dev_mode = True
c.LabApp.extensions_in_dev_mode = True
c.LabApp.expose_app_in_browser = True
