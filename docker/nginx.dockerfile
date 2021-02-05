FROM nginx:latest
LABEL Maintaner="Maycon Moreira "
COPY ./docker/nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
ENTRYPOINT ["nginx"]
# Parametros extras para o entrypoint
CMD ["-g", "daemon off;"]
