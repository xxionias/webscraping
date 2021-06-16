# -*- coding: utf-8 -*-
import scrapy
import json
    
# read file
with open('spiders/stories.json', 'r') as f:
    data=f.read()

# parse file
data = json.loads(data)

profile_urls = []
for e in data:
    profile_urls.append(e['linkOfAuthorProfile'])

class ProfileSpider(scrapy.Spider):
    name = 'profile'

    start_urls = profile_urls

    def parse(self, response):
        href = response.xpath("//a[@aria-label='Author Homepage']/@href").get()
        url = 'https://medium.com' + href + '/about'
        print(url)
        yield scrapy.Request(url, callback=self.parse_profile)

    def parse_profile(self, response):
        for profile in response.xpath("//body"):
            yield {
                'user_name': profile.xpath(".//descendant::h2/text()[2]").get(),
                'desc': profile.xpath(".//h2//following::div[1]/p/text()").get(),
                'followers': profile.xpath(".//descendant::div[@class='n t']/descendant::div[@class='dp dq t']/a[@class='dr ds by bz ca cb cc cd ce bk dt du cf dv dw']/text()").get()
            }