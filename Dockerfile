FROM python

WORKDIR /home/application

ENV PYTHONDONTWRITETECODE = 1

ENV PYTHONBUFFERED = 1

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./ciphers_project ciphers_project/

COPY ./entrypoint.sh .

ENTRYPOINT [ "./entrypoint.sh" ]