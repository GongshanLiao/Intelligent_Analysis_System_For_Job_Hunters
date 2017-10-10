import scrapy
import re
from functools import reduce
from JobCrawler.items import JobcrawlerItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import json

f = open('job.json', 'w', encoding='utf-8')
idx = 79758800


class Job51Spider(CrawlSpider):
    name = "51Job"
    allowed_domains = ['51job.com']
    start_urls = ['http://jobs.51job.com/beijing/79758800.html?s=01&t=0']

    @staticmethod
    def filter(url):
        return not(
            not re.match(r'.*51job\.com.*', url)
            or not re.match(r'http.*', url)
            or re.match(r'http://big5.*', url)
            or re.match(r'https://login.*', url)
            or re.match(r'http://www\.51job\.com/+default-e\.php.*', url)
            or re.match(r'http://ehire.*', url)
            or re.match(r'http://i\..*', url)
            or re.match(r'http://my\..*', url)
            or re.match(r'http://app\..*', url)
        )

    def parse(self, response):
        def concat(x, y):
            return x.strip() + y.strip()

        try:
            if re.match(r'.*jobs\.51job\.com/.*/\d*\.html.*', response.url):
                item = JobcrawlerItem()
                item['title'] = response.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/h1/text()').extract_first(
                    default='未知')
                item['city'] = response.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/span/text()').extract_first(
                    default='未知')

                salary = response.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/strong/text()').extract_first(
                    default='未知')
                match = re.match(r'(\d*(\.\d*)?)-(\d*(\.\d*)?)(.*)/(.*)', salary, re.U)
                if match is None:
                    item['salary_min'] = '未知'
                    item['salary_max'] = '未知'
                    item['salary_period'] = '未知'
                else:
                    if match.group(5) is '万':
                        item['salary_min'] = str(int(match.group(1)) * 10000)
                        item['salary_max'] = str(int(match.group(3)) * 10000)
                    elif match.group(5) is '千':
                        item['salary_min'] = str(int(match.group(1)) * 1000)
                        item['salary_max'] = str(int(match.group(3)) * 1000)
                    else:
                        item['salary_min'] = match.group(1) + match.group(5)
                        item['salary_max'] = match.group(3) + match.group(5)
                    item['salary_period'] = match.group(6)

                item['company_name'] = response.xpath(
                    '/html/body/div[2]/div[2]/div[2]/div/div[1]/p[1]/a/text()').extract_first(default='未知')

                info = response.xpath('/html/body/div[2]/div[2]/div[2]/div/div[1]/p[2]/text()').extract_first(
                    default='未知')
                if info is not '未知':
                    info = info.split('|')
                    item['company_type'] = info[0].strip()
                    item['company_size'] = info[1].strip()
                    item['company_attr'] = info[2].strip()

                item['company_info'] = reduce(
                    concat,
                    response.xpath(
                        '/html/body/div[2]/div[2]/div[3]/div/div[contains(@class,"tmsg inbox")]/text()').extract(),
                    '')

                item['require_experience'] = '未知'
                item['require_degree'] = '未知'
                item['require_num'] = '未知'
                item['require_skills'] = []
                item['publish_date'] = '未知'

                info = response.css(
                    'body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div.tBorderTop_box.bt > div > div > span::text').extract()
                for i in info:
                    if re.match(r'.*(\d*)人.*', i.strip(), re.U):
                        try:
                            item['require_num'] = re.search(r'\d+', i.strip(), re.U).group()
                        except AttributeError:
                            item['require_num'] = '若干'
                        continue
                    if re.match(r'(\d+-\d+)发布.*', i.strip(), re.U):
                        item['publish_date'] = re.match(r'(\d+-\d+)发布.*', i.strip(), re.U).group(1)
                        continue
                    if re.match(r'(.*)经验', i.strip(), re.U):
                        item['require_experience'] = re.match(r'(.*)经验', i.strip(), re.U).group(1)
                        continue
                    if i in ['小学', '中学', '初中', '高中', '中专', '大专', '本科', '硕士', '博士', '博士后']:
                        item['require_degree'] = i
                        continue
                    item['require_skills'].append(i.strip())

                item['job_tags'] = response.css(
                    'body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div.tBorderTop_box.bt > div > p > span::text').extract()
                item['job_description'] = reduce(
                    concat,
                    response.css(
                        'body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-child(4) > div::text').extract(),
                    '')
                item['job_type'] = response.css(
                    'body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-child(4) > div > div.mt10 > p:nth-child(1) > span.el::text').extract()
                item['job_keywords'] = response.css(
                    'body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-child(4) > div > div.mt10 > p:nth-child(2) > span.el::text').extract()
                item['job_location'] = reduce(
                    concat,
                    response.css(
                        'body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-child(5) > div > p::text').extract(),
                    '')
                item['department'] = reduce(
                    concat,
                    response.css(
                        'body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-child(6) > div[class*="bmsg inbox"]::text').extract(),
                    '')
                f.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
                f.flush()
                # yield item
        except:
            print(response.url)

        global idx
        if idx > 79758800:
            print('####')
            return
        else:
            while idx < 79768800:
                print(idx)
                idx += 1
                yield scrapy.Request('http://jobs.51job.com/beijing/' + str(idx) + '.html?s=01&t=0',
                                     callback=self.parse)

        '''
        for url in filter(self.filter, response.xpath('//a/@href').extract()):
            yield scrapy.Request(url, callback=self.parse)
        '''
