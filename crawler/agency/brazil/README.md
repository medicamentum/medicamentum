# How to run

Just follow the commands bellow:

- Run Docker:

`docker run -v /tmp:/mnt/output --net=host -it crawler sh`

- ANVISA crawler has two steps. The first one catch-all pages and store them as HTML. Our second step retrieves all PDF's, reading each HTML recovered from the first step.  So, run

`/opt/agency/brazil/anvisa.sh`

Then, run `service apache2 start` and

`scrapy runspider /opt/agency/brazil/anvisa.py`
