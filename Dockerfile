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



#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #
# ssh root@188.166.101.169
# sudo curl   -sSL   -o /usr/bin/docker-volume-plugin-dostorage   https://github.com/omallo/docker-volume-plugin-dostorage/releases/download/v0.4.0/docker-volume-plugin-dostorage_linux_amd64
# sudo chmod +x /usr/bin/docker-volume-plugin-dostorage
# sudo docker-volume-plugin-dostorage --access-token=TOKEN_FROM_DIGITAL_OCEAN &
# sudo service docker restart
# sudo mkfs.ext4 /dev/disk/by-id/scsi-0DO_Volume_reval-volume
# docker volume create --driver dostorage --name reval-volume
# git clone https://github.com/deenr/reval-equip.git app
# cd app
# docker image build -t reval-build .
# docker run -v reval-volume:/reval-equip/database -p 5000:5000 -d reval-build
# docker ps
# docker volume inspect reval-volume
#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #