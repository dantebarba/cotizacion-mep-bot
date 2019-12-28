FROM python:2.7-slim
MAINTAINER dantebarba.alerts@gmail.com

COPY . .

RUN ["python", "setup.py", "install"]

ENV API_KEY=''
ENV API_URL=''
ENV TELEGRAM_TOKEN=''

CMD ["sh", "-c", "python -u -m cotizacion_mep_bot --telegram_token $TELEGRAM_TOKEN --api_url $API_URL"]