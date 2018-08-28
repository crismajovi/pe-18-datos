import scrapy
import codecs


class QuotesSpider(scrapy.Spider):
    name = "mundial"

    def start_requests(self):
        """
        urls = [
            'https://es.fifa.com/worldcup/teams/',
        ]
        """
        archivo = open("data/url.csv", "r")
        archivo = archivo.readlines()
        archivo = [a.strip() for a in archivo]
        for url in archivo:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
            @reroes
        """
        filename = "data/paises.csv"
        with codecs.open(filename, 'a', encoding='utf-8') as f:
            #lista = response.xpath('//div[@class="fi-teams-list"]/div/a[@class="fi-team-card fi-team-card__team"]')
            lista=response.xpath('//div[@class="fi-team__members"]/a/div[@class="fi-p"]')
            for l in lista:
                pais = l.xpath('//div[@class="fi-t__n"]/span/text()').extract()[0]
                posi = l.xpath('div[@class="fi-p__info"]/div[@class="fi-p__info--role"]/text()').extract()[0].strip()
                edad = l.xpath('div[@class="fi-p__info"]/div[@class="fi-p__info--age"]/span[@class="fi-p__info--ageNum"]/text()').extract()[0].strip()
                nomb = l.xpath('div[@class="fi-p__info"]/div[@class="fi-p__n"]/a/span/text()').extract()[0].strip()
                numj = l.xpath('div[@class="fi-p__info"]/div[@class="fi-p__jerseyNum "]/span[@class="fi-p__num"]/text()').extract()[0].strip()
                f.write(u"%s,%s,%s,%s,%s\n" % (pais,nomb,edad,posi,numj))
        self.log('Saved file %s' % filename)
