FROM python:3.12.2-slim-bullseye
LABEL labase.author="carlo@ufrj.br"
LABEL version="24.03a"
LABEL description="Arvora - Brain Computational School"
COPY ../../requirements.txt /src
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -q -r requirements.txt
RUN mkdir -p /var/www/arvora
ADD . /var/www/arvora

RUN adduser --system arvorauser
USER arvorauser

WORKDIR /var/www/arvora
#ENTRYPOINT ["top", "-b"]
ENTRYPOINT ["python", "wsgi.py", "--port=8888", "--debug=True"]
