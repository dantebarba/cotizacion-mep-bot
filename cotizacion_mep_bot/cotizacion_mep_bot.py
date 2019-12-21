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
        ''' devuelve el mep '''
        content = requests.get(self.api_url()).content
        bot.send_message(chat_id=update.message.chat_id,text=content)

    def start_pooling(self):
        self._updater.start_polling()
        self._updater.idle()

    def error_handler(self, bot, error):
        bot.send_message(text='Ha ocurrido un error inesperado.')

    def api_url(self):
        return self._url + "/api/mepvalue"