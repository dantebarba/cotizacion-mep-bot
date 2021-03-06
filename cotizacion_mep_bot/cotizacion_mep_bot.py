import requests
import urllib2
import json
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
        self.mep_all_handler = CommandHandler('mep_all', self.mep_all)
        self._dispatcher.add_handler(self.start_handler)
        self._dispatcher.add_handler(self.mep_value_handler)
        self._dispatcher.add_handler(self.mep_all_handler)
        self._dispatcher.add_error_handler(self.error_handler)

    def start(self, bot, update):
        ''' Mensaje inicial del bot '''
        bot.send_message(chat_id=update.message.chat_id, text='''Bienvenido a Cotizacion_MEP, el bot que recupera el precio del dolar MEP. 
Ingrese /mep para obtener la cotizacoin del dia. Ingrese /mep_all para visualizar todas las cotizaciones ordenadas''')

    def mep(self, bot, update):
        ''' devuelve el mep 
        Ejemplo: {"bond_ars": 
        {"currency": "ARS", "price": 2880.0, "code": "AY24", "last_update": "2019-12-20T17:00:17.4961053-03:00"}, 
        "mep_value": 71.09355714638362, "bond_usd": 
        {"currency": "USD", "price": 40.51, "code": "AY24D", "last_update": "2019-12-20T17:00:40.9959802-03:00"}, 
        "last_update": "2019-12-21T19:00:09.651982"}
        '''
        response = requests.get(self.api_url("0", "1"))
        if (response.status_code is not 200):
            self.error_handler(bot, update, None)
        else:
            self._process_response(response.json(), bot, update)

    def mep_all(self, bot, update):
        response = requests.get(self.api_url())
        if (response.status_code is not 200):
            self.error_handler(bot, update, None)
        else:
            self._process_response(response.json(), bot, update)

    def _process_response(self, response, bot, update):
        for json_element in response:
            bot.send_message(chat_id=update.message.chat_id, text=u'''
Valor MEP: {0}
Bono ARS: {1}
Valor Bono: {2}
Monto operado: {3}
Bono USD: {4}
Valor Bono: {5}
Monto operado: {6}
Ultima act: {7}
        '''.format(json_element["mep_value"],
                   json_element["bond_ars"]["code"],
                   json_element["bond_ars"]["price"],
                   json_element["bond_ars"]["volume"],
                   json_element["bond_usd"]["code"],
                   json_element["bond_usd"]["price"],
                   json_element["bond_usd"]["volume"],
                   json_element["last_update"]))

    def start_pooling(self):
        self._updater.start_polling()
        self._updater.idle()

    def error_handler(self, bot, update, error):
        bot.send_message(chat_id=update.message.chat_id,
                         text='Ha ocurrido un error inesperado.')

    def api_url(self, start="0", end="100"):
        return self._url + "/api/v1/mepvalue?from="+start+"&to="+end
