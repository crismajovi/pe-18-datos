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
        filename = "data/alemania.csv"
        with codecs.open(filename, 'a', encoding='utf-8') as f:
            #lista = response.xpath('//div[@class="fi-teams-list"]/div/a[@class="fi-team-card fi-team-card__team"]')
            lista=response.xpath('//div[@class="fi-p__info"]')
            for l in lista:
                posi = l.xpath('div[@class="fi-p__info--role"]/text()').extract()[0].strip()
                edad = l.xpath('div[@class="fi-p__info--age"]/span[@class="fi-p__info--ageNum"]/text()').extract()[0].strip()
                numj = l.xpath('div[@class="fi-p__jerseyNum "]/span[@class="fi-p__num"]/text()').extract()[0].strip()
                nomb = l.xpath('div[@class="fi-p__n"]/a/span/text()').extract()[0].strip()
                f.write(u"%s|%s|%s|%s\n" % (nomb,edad,posi,numj))
        self.log('Saved file %s' % filename)
