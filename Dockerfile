FROM python:2.7-alpine
MAINTAINER dantebarba.alerts@gmail.com

COPY . .

RUN ["python", "setup.py", "install"]

ENV API_KEY=''
ENV API_URL=''
ENV TELEGRAM_TOKEN=''

EXPOSE 5000

CMD ["sh", "-c", "python -m cotizacion_mep_bot --telegram_token $TELEGRAM_TOKEN --api_url $API_URL"]