FROM nginx:stable

COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY uwsgi_params /etc/nginx/uwsgi_params

USER root

RUN apt-get update
RUN apt-get install -y --no-install-recommends certbot python3-certbot-nginx
RUN mkdir -p /app/staticfiles
RUN mkdir -p /app/mediafiles
RUN chmod 755 /app/staticfiles
RUN chmod 755 /app/mediafiles