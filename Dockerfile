FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y install python3-pip
RUN pip install  numpy 
RUN pip install  pandas matplotlib

COPY dataset-processor.py .

COPY wine.data .

CMD ["python3","numpy","pandas","matplotlib","-u","dataset-processor.py"]


