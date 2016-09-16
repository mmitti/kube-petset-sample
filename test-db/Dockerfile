FROM fedora:latest
MAINTAINER mmitti <dev@mail.mmitti.info>
RUN dnf install -y python-pip gcc redhat-rpm-config python3-devel
RUN pip3 install falcon
COPY main.py /
COPY data.py /
ENTRYPOINT python3 /main.py
