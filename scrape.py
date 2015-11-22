import scrapy
from urlparse import urljoin
from scrapy.utils.response import get_base_url

class CFSpider(scrapy.Spider):
    name = 'cf'
    start_urls = ['http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html']
    allowed_domains = ['docs.aws.amazon.com']

    def parse(self, response):
        for r_url in response.xpath('//div[@class="highlights"]/ul/li/a/@href').extract():
            abs_url = urljoin(get_base_url(response), r_url)
            yield scrapy.Request(abs_url, callback=self.parse_properties)

    def parse_properties(self, response):
        def pairwise(it):
            it = iter(it)
            while True:
                yield next(it), next(it)

        res_name = response.xpath('//h1[@class="topictitle"]/text()').extract()[0]

        dl = response.css('.variablelist dl')

        if len(dl) > 0:
            for dt, dd in pairwise(dl[0].xpath('./dt | ./dd')):

                p_name = dt.xpath('span/code/text()').extract()[0]

                links = dd.css('a.link::attr(href)')
                uris = links.re('using-cfn-updating-stacks.html#.*')

                yield { 'resource': res_name, 'property': p_name, 'update': uris }
