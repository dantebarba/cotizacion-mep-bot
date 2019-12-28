"""This module serves as the entry point of cotizacion_mep_bot."""
import argparse
import cotizacion_mep_bot
import logging


def main():
    """The actual entry point."""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    parser = argparse.ArgumentParser(description='Ejecucion del bot servicio')
    parser.add_argument('--telegram_token',  help='Telegram bot token')
    parser.add_argument('--api_url',  help='Cotizacion-MEP API location')
    cotizacion_mep_bot.CotizacionMepBot(parser.parse_args(
    ).telegram_token, parser.parse_args().api_url).start_pooling()


if __name__ == '__main__':
    main()
