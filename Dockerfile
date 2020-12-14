FROM python:3.8-slim
RUN mkdir /seet-geek
WORKDIR /seet-geek
ADD requirements.txt /seet-geek
RUN pip3 install -r requirements.txt
ADD . /seet-geek
ADD wait-for-it.sh /seet-geek
RUN chmod +x /seet-geek/wait-for-it.sh
EXPOSE 8081