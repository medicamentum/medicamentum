# How to run

Just follow the commands bellow:

- Docker image creation:

` docker build -f Docker.crawler -t crawler .`

- Docker usage:

`docker run -v /tmp:/mnt/output -it crawler sh`


# Agencies

In order to extract information by agency, run the command (By country)

Brazil - /opt/agency/brazil/anvisa.sh 1000
