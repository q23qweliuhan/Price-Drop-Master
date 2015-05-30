import requests
from lxml import html
from gluon import current

class Scraper:

    def __init__(self, link):
        self.link = str(link)

    def scrap(self):
        page = requests.get(self.link)
        tree = html.fromstring(page.text)
        if('esprit' in self.link):
            name = str(tree.xpath('//h1[@class="singleproductview-details-title font-lucida"]/text()'))
            price = str(tree.xpath('//span[@class="price_output"]/text()')[0])
            return price
        else:
            db = current.db
            db(db.subscription.link == self.link).delete()
            return 'not available'
