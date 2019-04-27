FROM ubuntu:latest

MAINTAINER wanghaifei

ADD ./answer_django /home/src/answer_django
WORKDIR /home/src/answer_django


ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "0.0.0.0:8099"]
