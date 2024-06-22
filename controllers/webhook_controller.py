from flask import Flask, request, Blueprint
import config 
import services.all as services
import requests
from utils.extract_nested_values import extract_nested_values
import json


webhook_blueprint = Blueprint('webhook', __name__)


@webhook_blueprint.route('/webhook', methods=['POST'])
def recibir_mensajes():
    try:

        
        body = request.get_json()
        
        messages = extract_nested_values(body,['entry','changes','value','messages'])
        message= messages[0]
        text = services.obtener_Mensaje_whatsapp(message)
        number = services.replace_start(message['from'])
        messageId = message['id']
        
        name = extract_nested_values(body,['entry','changes','value','contacts','profile','name'])
        services.administrar_chatbot(text, number,messageId,name)

        return 'enviado'

    except Exception as e:
        return 'no enviado ' + str(e)
    
@webhook_blueprint.route('/webhook', methods=['GET'])
def verificar_token():
    try:
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if token == config.token and challenge != None:
            return challenge
        else:
            return 'token incorrecto', 403
    except Exception as e:
        return e,403

