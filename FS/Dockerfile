FROM python:3.9

RUN apt-get update && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN groupadd -g 799 rhd9863 && \
    useradd -r -u 999 -g rhd9863 nyu

WORKDIR /app

RUN pip install Flask
RUN pip install requests
RUN pip install Flask-API

USER nyu

COPY --chown=rhd9863:nyu . .

CMD [ "python", "./fs.py" ]