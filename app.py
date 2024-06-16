from flask import Flask
from controllers.webhook_controller import webhook_blueprint



app = Flask(__name__)

""" @app.route('/bienvenido', methods=['GET'])
def  bienvenido():
    return 'Hola mundo bigdateros, desde Flask'
 """

app.register_blueprint(webhook_blueprint)



    


if __name__ == '__main__':
    app.run()