FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev

COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
RUN pip install gunicorn

COPY . /code/
WORKDIR /code/

RUN adduser --uid 1002 --disabled-password --gecos '' --no-create-home wagtail
RUN chown -R wagtail /code
USER wagtail

EXPOSE 8000
CMD ./bin/gunicorn.sh
