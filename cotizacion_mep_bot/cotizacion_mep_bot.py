import requests
import urllib2
from telegram.ext import Updater
from telegram.ext import CommandHandler

class CotizacionMepBot():
    ''' Esta clase contiene todo lo necesario para operar el bot '''

    def __init__(self, token, api_url):
        self._updater = Updater(token=token)
        self._url = api_url
        self._dispatcher = self._updater.dispatcher
        self.start_handler = CommandHandler('start', self.start)
        self.mep_value_handler = CommandHandler('mep', self.mep)
        self._dispatcher.add_handler(self.start_handler)
        self._dispatcher.add_handler(self.voucher_handler)
        self._dispatcher.add_error_handler(self.error_handler)

    def start(self, bot, update):
        ''' Mensaje inicial del bot '''
        bot.send_message(chat_id=update.message.chat_id,text='''Bienvenido a Cotizacion_MEP, el bot que recupera el precio del dolar MEP. 
Ingrese /mep para obtener la cotizacoin del dia''')
    
    def mep(self, bot, update):
        ''' devuelve el mep 
        Ejemplo: {"bond_ars": 
        {"currency": "ARS", "price": 2880.0, "code": "AY24", "last_update": "2019-12-20T17:00:17.4961053-03:00"}, 
        "mep_value": 71.09355714638362, "bond_usd": 
        {"currency": "USD", "price": 40.51, "code": "AY24D", "last_update": "2019-12-20T17:00:40.9959802-03:00"}, 
        "last_update": "2019-12-21T19:00:09.651982"}
        '''
        response = requests.get(self.api_url())
        if (response.status_code is not 200):
            raise StandardError("No se ha podido recuperar el valor del dolar MEP en este momento, por favor intente mas tarde.")
        response = response.json()
        bot.send_message(chat_id=update.message.chat_id,text=
        '''
Valor MEP: {0}
Bono ARS: {1}
Valor Bono: {2}
Bono USD: {3}
Valor Bono: {4}
Última act: {5}
        '''.format(response["mep_value"], 
        response["bond_ars"]["code"], 
        response["bond_ars"]["price"], 
        response["bond_usd"]["code"], 
        response["bond_usd"]["price"], 
        response["last_update"]))

    def start_pooling(self):
        self._updater.start_polling()
        self._updater.idle()

    def error_handler(self, bot, error):
        bot.send_message(text='Ha ocurrido un error inesperado.')

    def api_url(self):
        return self._url + "/api/v1/mepvalue"