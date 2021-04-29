FROM python:3.8

# PULL FROM REPOSITORY
WORKDIR /reval-equip
COPY . /reval-equip

# INSTALL FLASK
RUN pip install Flask==0.12
RUN pip install flask_login==0.4.1
RUN pip install flask_sqlalchemy==2.5.1

CMD ["python", "app.py"] 