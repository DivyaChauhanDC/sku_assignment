FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
RUN apk --update add bash nano
COPY ./requirements/local.txt /home/Documents/medpay_assignement/requirements/local.txt
RUN pip install -r /home/Documents/medpay_assignement/requirements/local.txt