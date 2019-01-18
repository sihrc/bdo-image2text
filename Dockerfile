FROM jitesoft/tesseract-ocr

LABEL author="Chris Lee"
LABEL email="sihrc.c.lee@gmail.com"

ENV PYTHONIOENCODING=utf-8
COPY requirements.txt /requirements.txt
RUN apt-get update && \
    apt-get install -y python3 python3-dev python3-pip libpng-dev libjpeg-dev && \
    pip3 install opencv-python-headless && \
    pip3 install -r requirements.txt

COPY . /bdo
WORKDIR bdo

RUN python3 setup.py develop

CMD ["bash"]