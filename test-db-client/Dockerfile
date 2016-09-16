FROM fedora:latest
MAINTAINER mmitti <dev@mail.mmitti.info>
RUN dnf install -y python-pip gcc redhat-rpm-config python3-devel
RUN pip3 install Flask requests
COPY test-client.py /
COPY templates/ templates/
ENTRYPOINT python3 /test-client.py
