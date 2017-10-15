# -*- coding utf-8 -*-

import scrapy


class JobcrawlerItem(scrapy.Item):
    """Define the basic information provided by 51Job about a job.

    Use Scrapy field to store data

    Attributes
        ``title`` is the name of the job.
        ``city`` is the city of that job.
        ``salary_min`` is the lower bound of the salary.
        ``salary_max`` is the upper bound of the salary.
        ``salary_period`` is the time units, like per month or per year.
        ``company_name`` is the name of the company which provides the job.
        ``company_type`` is the type of a company like a joint venture
        ``company_size`` is the number of workers in a company
        ``company_attr`` is the attribute of the company like an Internet company
        ``company_info`` is a text that describes basic information about a company
        ``require_experience`` is the required years of job experience before
        ``require_degree`` is the required degree like a master
        ``require_num`` is the number of workers that the company wants to employs
        ``require_skills`` is the list of other skills that the company requires
        ``publish_date`` is the date that this information was published
        ``job_tags`` is the tags of a job like 'flexible working time'
        ``job_description`` is the text that describe the detailed information about this job
        ``job_type`` is a list that describe the type of this job like 'software engineer'
        ``job_keywords`` is a list of keywords about a job
        ``job_location`` is the location of the workplace
        ``department`` is the department of a job
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
