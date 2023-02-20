FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install cmake
RUN pip install dlib
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver"]
