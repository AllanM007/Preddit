FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /
WORKDIR /
ADD requirements.txt /
RUN pip install -r requirements.txt
ADD . /