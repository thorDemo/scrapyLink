import scrapy
from scrapy import Selector
from scrapyLink.items import ScarpylinkItem


class DmozSpider(scrapy.Spider):
    name = "linkSpider"
    start_urls = [
        'http://www.aidshe.com',
        'http://www.aidtai.com',
        'http://www.aidtan.com',
        'http://www.aidtao.com',
        'http://www.aidwai.com',
        'http://www.aidwan.com',
        'http://www.aidwei.com',
        'http://www.aidxia.com',
        'http://www.aidxie.com',
        'http://www.aidxin.com',
        'http://www.aidyan.com',
        'http://www.aidyao.com',
        'http://www.aidyin.com',
        'http://www.aidzai.com',
        'http://www.aidzan.com',
        'http://www.aidzao.com',
        'http://www.aidzei.com',
        'http://www.aidzha.com',
        'http://www.aiebie.com',
        'http://www.aiebin.com',
        'http://www.aiechu.com',
        'http://www.aiecou.com',
        'http://www.aienan.com',
        'http://www.aienao.com',
        'http://www.aiepan.com',
        'http://www.aiepao.com',
        'http://www.aiepei.com',
        'http://www.aiepen.com',
        'http://www.aieqia.com',
        'http://www.aieqie.com',
        'http://www.aieqin.com',
        'http://www.aieren.com',
        'http://www.aiesai.com',
        'http://www.aiesao.com',
        'http://www.aiesen.com',
        'http://www.aieshe.com',
        'http://www.aietai.com',
        'http://www.aietan.com',
        'http://www.aiewai.com',
        'http://www.aiewei.com',
        'http://www.aiexia.com',
        'http://www.aiexie.com',
        'http://www.aieyan.com',
        'http://www.aiezai.com',
        'http://www.aiezan.com',
        'http://www.aiezao.com',
        'http://www.aiezei.com',
        'http://www.aiezha.com',
        'http://www.aiezhe.com',
        'http://www.aiezhi.com',
    ]

    def parse(self, response):
        item = ScarpylinkItem()
        sell = Selector(response)
        title = sell.xpath('/html/head/title/text()').extract()[0]
        item['title'] = str(title).split(',')[0]
        item['url'] = response.url
        string = '<a href=\'%s\' title=\'%s\'>%s</a>' % (item['url'], item['title'], item['title'])
        print(string)