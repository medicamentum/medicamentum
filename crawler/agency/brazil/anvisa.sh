#!/bin/sh
mkdir -p output

for i in `seq 2 $1`
do
   curl -X POST 'http://www.anvisa.gov.br/datavisa/fila_bula/frmResultado.asp' -H 'Connection: keep-alive' -H 'Cache-Control: max-age=0' -H 'Origin: http://www.anvisa.gov.br' -H 'Upgrade-Insecure-Requests: 1' -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' -H 'Referer: http://www.anvisa.gov.br/datavisa/fila_bula/frmResultado.asp' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7' -H 'Cookie: _ga=GA1.3.848461410.1526129495; _gid=GA1.3.1470584546.1526129495; ASPSESSIONIDCAATBTDC=ODEOFMDDMLMLLLFBCEAHJMDP' --data 'txtMedicamento=&txtEmpresa=&txtNuExpediente=&txtDataPublicacaoI=&txtDataPublicacaoF=&hddLetra=&hddOrderBy=medicamento&hddSortBy=asc&hddPageSize=10&hddPageAbsolute='$i'' --compressed -o /mnt/output/${i}.html
done

