#¡/bin/bash

set -eu

export PYTHONUNBUFFERED=true
#curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
#python3 get-pip.py --user

#python3 -m pip install -r requirements.txt

# para detener el servicio se comenta la linea de abajo
python3 app.py