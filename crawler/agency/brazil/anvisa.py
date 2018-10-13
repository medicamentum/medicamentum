#!/usr/bin/env python

import scrapy
import codecs
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class AnvisaSpider(scrapy.Spider):
    name = 'anvisaspider'
    start_urls = ['http://localhost/1.html']

    def request(self, url, callback):
        request = scrapy.FormRequest(url=url, callback=callback)
        return request

    def documents(self, leaflet):
        return str(leaflet).replace('\'','').replace('[u"fVisualizarBula(', '').replace(')"]', '').split(',')

    def parse(self, response):
        for current_page in range(1, 870):
            url_anvisa = 'http://localhost/' + str(current_page) + '.html'
            yield self.request(url=url_anvisa, callback=self.parse_leaflets)     

    def parse_leaflets(self, response):
        drugs_table = response.xpath('//table[@id="tblResultado"]/tbody/tr')
        for drug in drugs_table:


            leaflet = self.documents(drug.css('td')[4].css('a::attr(onclick)').extract())
            professional_leaflet = self.documents(drug.css('td')[5].css('a::attr(onclick)').extract())

            content = "\"%s\";\"%s\";\"%s\";\"%s\";\"%s\";\"%s\"\n" % (unicode(str(drug.css('td::text')[0].extract()).strip(), 'utf-8'),
                                        unicode(str(drug.css('td::text')[1].extract()).strip(), 'utf-8'),
                                        unicode(str(drug.css('td::text')[2].extract()).strip(), 'utf-8'),
                                        unicode(str(drug.css('td::text')[3].extract()).strip(), 'utf-8'),
                                        str(leaflet[0]).strip() + '_' + str(leaflet[1]).strip() + '.pdf',
                                        str(professional_leaflet[0]).strip() + '_' + str(professional_leaflet[1]).strip() + '.pdf')

            yield self.save("drugs.csv", content)
            yield self.request('http://www.anvisa.gov.br/datavisa/fila_bula/frmVisualizarBula.asp?pNuTransacao=' + leaflet[0]  + '&pIdAnexo='  + leaflet[1] , self.save_pdf)
            yield self.request('http://www.anvisa.gov.br/datavisa/fila_bula/frmVisualizarBula.asp?pNuTransacao=' + professional_leaflet[0]  + '&pIdAnexo='  + professional_leaflet[1] , self.save_pdf)
    

    def save(self, filename, content):
        with open(filename, "a") as myfile:
            myfile.write(content)
    
    def save_pdf(self, response):
        path = response.url.split('/')[-1]
        path = str(path).replace('frmVisualizarBula.asp?pNuTransacao=', '').replace('&pIdAnexo=%', '_') + '.pdf'
        self.logger.info('Saving PDF %s', path)
        with open(path, 'wb') as f:
            f.write(response.body)
