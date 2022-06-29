FROM python:3.10.0-alpine

# User config
RUN mkdir -p /home/app
RUN addgroup -S app && adduser -S app -G app
ENV HOME=/home/app
ENV APP_HOME=/home/app/bekon
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles

# Python config
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install pipenv

COPY . $APP_HOME
WORKDIR $APP_HOME
RUN pipenv install --system --deploy --ignore-pipfile

# User config
RUN chown -R app:app $APP_HOME
USER app