# Run with:
#    podman run -it --publish 8080:8080 --volume kanban.db:kanban.db <image-id>
#
FROM ubuntu:latest

RUN apt update -y && \
    apt install python3 python3-pip --no-install-recommends -y && \
    apt clean
WORKDIR /python-kanban
copy requirements.txt .
RUN pip3 install -r requirements.txt waitress

copy *.py .
copy static ./static
EXPOSE 8080

CMD waitress-serve --call 'main:create_app'
