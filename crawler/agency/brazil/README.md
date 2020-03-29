# How to run

Just follow the commands bellow:

- Build the image:

`docker build -t crawler -f Docker.crawler .`

- Run Docker:

`docker run -v /tmp:/mnt/output -v /tmp:/var/www/html --net=host -it crawler sh`

- ANVISA crawler has two steps. The first one catch-all pages and store them as HTML. Our second step retrieves all PDF's, reading each HTML recovered from the first step.  So, run

`/opt/agency/brazil/anvisa.sh 1013`

Then, run `service apache2 start` and

`mkdir -p /mnt/output/pdfs && cd /mnt/output/pdfs && scrapy runspider /opt/agency/brazil/anvisa.py -a last_page=1013`


# Distribution and copyrights 

![ANVISA](https://raw.githubusercontent.com/sandroacoelho/drugs/master/crawler/agency/brazil/ANVISA_AUTORIZACAO.png)

