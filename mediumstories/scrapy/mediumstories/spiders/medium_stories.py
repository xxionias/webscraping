# -*- coding: utf-8 -*-
import scrapy

class MediumStoriesSpider(scrapy.Spider):
    name = 'medium_stories'
    #allowed_domains = ['https://towardsdatascience.com/archive/2017/09']
    start_urls = [
        'https://towardsdatascience.com/archive/2016/02'
        'https://towardsdatascience.com/archive/2016/03',
        'https://towardsdatascience.com/archive/2016/04',
        'https://towardsdatascience.com/archive/2016/05',
        'https://towardsdatascience.com/archive/2016/06',
        'https://towardsdatascience.com/archive/2016/07',
        'https://towardsdatascience.com/archive/2016/08',
        'https://towardsdatascience.com/archive/2016/09',
        'https://towardsdatascience.com/archive/2016/10',
        'https://towardsdatascience.com/archive/2016/11',
        'https://towardsdatascience.com/archive/2016/12',
        'https://towardsdatascience.com/archive/2017/01',
        'https://towardsdatascience.com/archive/2017/02',
        'https://towardsdatascience.com/archive/2017/03',
        'https://towardsdatascience.com/archive/2017/04',
        'https://towardsdatascience.com/archive/2017/05',
        'https://towardsdatascience.com/archive/2017/06',
        'https://towardsdatascience.com/archive/2017/07',
        'https://towardsdatascience.com/archive/2017/08',
        'https://towardsdatascience.com/archive/2017/09',
        'https://towardsdatascience.com/archive/2017/10',
        'https://towardsdatascience.com/archive/2017/11',
        'https://towardsdatascience.com/archive/2017/12',
        'https://towardsdatascience.com/archive/2018/01',
        'https://towardsdatascience.com/archive/2018/02',
        'https://towardsdatascience.com/archive/2018/03',
        'https://towardsdatascience.com/archive/2018/04',
        'https://towardsdatascience.com/archive/2018/05',
        'https://towardsdatascience.com/archive/2018/06',
        'https://towardsdatascience.com/archive/2018/07',
        'https://towardsdatascience.com/archive/2018/08',
        'https://towardsdatascience.com/archive/2018/09',
        'https://towardsdatascience.com/archive/2018/10',
        'https://towardsdatascience.com/archive/2018/11',
        'https://towardsdatascience.com/archive/2018/12',
        'https://towardsdatascience.com/archive/2019/01',
        'https://towardsdatascience.com/archive/2019/02',
        'https://towardsdatascience.com/archive/2019/03',
        'https://towardsdatascience.com/archive/2019/04',
        'https://towardsdatascience.com/archive/2019/05',
        'https://towardsdatascience.com/archive/2019/06',
        'https://towardsdatascience.com/archive/2019/07',
        'https://towardsdatascience.com/archive/2019/08',
        'https://towardsdatascience.com/archive/2019/09',
        'https://towardsdatascience.com/archive/2019/10',
        'https://towardsdatascience.com/archive/2019/11',
        'https://towardsdatascience.com/archive/2019/12',
        'https://towardsdatascience.com/archive/2020/01',
        'https://towardsdatascience.com/archive/2020/02',
        'https://towardsdatascience.com/archive/2020/03',
        'https://towardsdatascience.com/archive/2020/04',
        'https://towardsdatascience.com/archive/2020/05',
        'https://towardsdatascience.com/archive/2020/06',
        'https://towardsdatascience.com/archive/2020/07',
        'https://towardsdatascience.com/archive/2020/08',
        'https://towardsdatascience.com/archive/2020/09',
        'https://towardsdatascience.com/archive/2020/10',
        'https://towardsdatascience.com/archive/2020/11',
        'https://towardsdatascience.com/archive/2020/12',
        'https://towardsdatascience.com/archive/2021/01',
        'https://towardsdatascience.com/archive/2021/02',
        'https://towardsdatascience.com/archive/2021/03',
        'https://towardsdatascience.com/archive/2021/04',
        'https://towardsdatascience.com/archive/2021/05'
    ]


    def parse(self, response):
        stories_by_date_links = response.xpath("//div[@class='col u-inlineBlock u-width265 u-verticalAlignTop u-lineHeight35 u-paddingRight0']/descendant::div[@class='timebucket u-inlineBlock u-width35']/a/@href")
        for link in stories_by_date_links:
            yield scrapy.Request(link.get(), callback=self.parse_by_date)

    def parse_by_date(self, response):
        for story in response.xpath("//div[@class='streamItem streamItem--postPreview js-streamItem']"):
            yield {
                'author': story.xpath(".//descendant::div[@class='postMetaInline postMetaInline-authorLockup ui-captionStrong u-flex1 u-noWrapWithEllipsis']/a[@class='ds-link ds-link--styleSubtle link link--darken link--accent u-accentColor--textNormal u-accentColor--textDarken']/text()").get(),
                'linkOfAuthorProfile': story.xpath(".//descendant::div[@class='postMetaInline postMetaInline-authorLockup ui-captionStrong u-flex1 u-noWrapWithEllipsis']/a[@class='ds-link ds-link--styleSubtle link link--darken link--accent u-accentColor--textNormal u-accentColor--textDarken']/@href").get(),
                'articleTitle': story.xpath(".//descendant::div[@class='section-inner sectionLayout--insetColumn']/h3[1]/text()").get(),
                'articleLink': story.xpath(".//descendant::div[@class='ui-caption u-fontSize12 u-baseColor--textNormal u-textColorNormal js-postMetaInlineSupplemental']/a/@data-action-value").get(),
                'postingTime': story.xpath(".//descendant::div[@class='ui-caption u-fontSize12 u-baseColor--textNormal u-textColorNormal js-postMetaInlineSupplemental']/a/time/text()").get(),
                'minToRead': story.xpath(".//descendant::div[@class='ui-caption u-fontSize12 u-baseColor--textNormal u-textColorNormal js-postMetaInlineSupplemental']/span[2]/@title").get(),
                'recommendations': story.xpath(".//descendant::span[@class='u-relative u-background js-actionMultirecommendCount u-marginLeft5']/button/text()").get(),
                'responses': story.xpath(".//descendant::div[@class='buttonSet u-floatRight']/a/text()").get()
            }
