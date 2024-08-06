FROM debian:latest

RUN apt-get update && \
    apt-get install -y gcc make pkg-config autoconf bsdmainutils

RUN apt-get install -y python3

COPY /src/ /app/

WORKDIR /root

COPY libnfc-libnfc-1.7.0.tar.gz .
COPY mfcuk-mfcuk-0.3.8.tar.gz .
COPY mfoc-mfoc-0.10.7.tar.gz .

RUN tar -xvf libnfc-libnfc-1.7.0.tar.gz && \
    tar -xvf mfcuk-mfcuk-0.3.8.tar.gz && \
    tar -xvf mfoc-mfoc-0.10.7.tar.gz && \
    rm *.tar.gz

RUN apt install -y libtool

WORKDIR /root/libnfc-libnfc-1.7.0

RUN autoreconf -is && ./configure --prefix=/usr --with-drivers=pn532_uart --sysconfdir=/etc && \
    make && make install && mkdir -p /etc/nfc

COPY libnfc.conf /etc/nfc/libnfc.conf

WORKDIR /root/mfcuk-mfcuk-0.3.8

RUN autoreconf -is && ./configure && make && \
    cp src/mfcuk /usr/local/bin/ && cp -r src/data /usr/local/bin/data

WORKDIR /root/mfoc-mfoc-0.10.7

RUN autoreconf -is && ./configure && make && make install

WORKDIR /root

RUN rm -rf libnfc-libnfc-1.7.0 mfcuk-mfcuk-0.3.8 mfoc-mfoc-0.10.7

ENTRYPOINT ["python3", "/app/read_card.py"]
