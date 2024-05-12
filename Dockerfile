# Run with:
#    podman run -it --publish 8080:8080 --volume kanban.db:kanban.db <image-id>
#
FROM ubuntu:24.04

RUN apt update -y && \
    apt install python3 python3-waitress python3-flask python3-flask-sqlalchemy \
      --no-install-recommends -y && \
    apt clean
WORKDIR /python-kanban

copy *.py .
copy static ./static
EXPOSE 8080

CMD waitress-serve --call 'main:create_app'
