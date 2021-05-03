FROM python:3.8


WORKDIR /reval-equip
COPY . /reval-equip

# INSTALL FLASK
RUN pip install Flask==0.12
RUN pip install flask_login==0.4.1
RUN pip install flask_sqlalchemy==2.5.1

VOLUME /go/src/beginnerapp/local-db

CMD ["python", "app.py"]

# docker image build -t reval-test .
# docker run -v C:\Coding\reval-database:/reval-equip/database -p 5000:5000 -d reval-test