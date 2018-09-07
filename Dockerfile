FROM selenium/standalone-firefox:3.14.0

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-setuptools \
    && pip3 install selenium xvfbwrapper \
    && rm -rf /var/lib/apt/lists/* \
    && find /usr/local -depth \
        \( \
            \( -type d -a \( -name test -o -name tests \) \) \
            -o \
            \( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
        \) -exec rm -rf '{}' +

WORKDIR /usr/local/stackoverflow-enthusiast-fanatic-badges

COPY app.py ./

USER seluser

RUN sudo chown -R seluser:seluser .

# todo: redicrect application logs to stdout

CMD ["python3", "app.py"]
