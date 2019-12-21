"""This module serves as the entry point of cotizacion_mep_bot."""
import argparse

def main():
    """The actual entry point."""
    parser = argparse.ArgumentParser(description='Ejecucion del bot servicio')
    parser.add_argument('--telegram_token',  help='Telegram bot token')
    parser.add_argument('--api_url',  help='Cotizacion-MEP API location')
    parser.parse_args().token

if __name__ == '__main__':
    main()
