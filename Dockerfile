FROM 47.240.0.28:5000/lesoubase:v1

MAINTAINER wanghaifei

RUN mkdir -p /home/logs/

ADD ./answer_django /home/src/answer_django
WORKDIR /home/src/answer_django


ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8099"]
