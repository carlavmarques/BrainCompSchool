FROM python:3.12.2-slim-bullseye
LABEL labase.author="juliabarbosa@poli.ufrj.br"
LABEL version="24.03a"
LABEL description="Arvora - Brain Computational School"
COPY ./requirements.txt /src
RUN python3 -m pip install --upgrade pip
RUN pip install tornado
RUN mkdir -p /var/www/arvora
ADD . /var/www/src/arvora

RUN adduser --system arvorauser
USER arvorauser

WORKDIR /var/www/src/arvora
#ENTRYPOINT ["top", "-b"]
ENTRYPOINT ["python", "wsgi.py", "--port=8888", "--debug=True"]
