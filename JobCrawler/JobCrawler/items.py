# -*- coding`` utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in``
# http``//doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobcrawlerItem(scrapy.Item):
    """Define the basic information provided by 51Job about a job.

    Use Scrapy field to store data

    Attributes``
        ``title`` is the name of the job.
        ``city`` is the city of that job.
        ``salary_min`` is the lower bound of the salary.
        ``salary_max`` is the upper bound of the salary.
        ``salary_period`` is the time units, like per month or per year.
        ``company_name`` is the name of the company which provides the job.
        ``company_type`` is the type of a company like a joint venture

    """
    title = scrapy.Field()
    city = scrapy.Field()
    salary_min = scrapy.Field()
    salary_max = scrapy.Field()
    salary_period = scrapy.Field()
    company_name = scrapy.Field()
    company_type = scrapy.Field()
    company_size = scrapy.Field()
    company_attr = scrapy.Field()
    company_info = scrapy.Field()
    require_experience = scrapy.Field()
    require_degree = scrapy.Field()
    require_num = scrapy.Field()
    require_skills = scrapy.Field()
    publish_date = scrapy.Field()
    job_tags = scrapy.Field()
    job_description = scrapy.Field()
    job_type = scrapy.Field()
    job_keywords = scrapy.Field()
    job_location = scrapy.Field()
    department = scrapy.Field()
