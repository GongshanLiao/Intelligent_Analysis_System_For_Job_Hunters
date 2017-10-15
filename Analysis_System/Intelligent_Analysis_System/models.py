from django.db import models
from django.core.exceptions import ValidationError


class JobBasic(models.Model):
    objects = models.Manager()
    jID = models.AutoField(
        primary_key=True, verbose_name='职位编号', db_index=True
    )
    jTitle = models.CharField(
        max_length=30, verbose_name='职位名称'
    )
    jDate = models.CharField(
        max_length=8, verbose_name='发布日期'
    )
    jType = models.CharField(
        max_length=20, verbose_name='职位类型'
    )
    jKeywords = models.CharField(
        max_length=20, verbose_name='职位关键词'
    )
    jCompany = models.CharField(
        max_length=30, verbose_name='公司名'
    )

    class Meta:
        verbose_name = '工作基本信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.jTitle + ' ' + self.jCompany


class JobSalary(models.Model):
    objects = models.Manager()
    jID = models.ForeignKey(
        JobBasic, verbose_name='职位编号', db_index=True
    )
    jMin = models.IntegerField(
        verbose_name='最少年薪'
    )
    jMax = models.IntegerField(
        verbose_name='最多年薪'
    )

    class Meta:
        verbose_name = '工资信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '最少年薪' + str(self.jMin) + ' 最多年薪' + str(self.jMax)


class CompanyInfo(models.Model):
    objects = models.Manager()
    cID = models.AutoField(
        primary_key=True, verbose_name='公司编号', db_index=True
    )
    cTitle = models.CharField(
        max_length=30, verbose_name='公司名称'
    )
    cType = models.CharField(
        max_length=20, verbose_name='公司类型'
    )
    cSize = models.CharField(
        max_length=10, verbose_name='公司人数'
    )
    cAttr = models.CharField(
        max_length=20, verbose_name='公司属性'
    )
    cInfo = models.TextField(
        verbose_name='公司介绍'
    )

    class Meta:
        verbose_name = '公司信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.cTitle


class JobCompany(models.Model):
    objects = models.Manager()
    jID = models.ForeignKey(
        JobBasic, verbose_name='职位编号', db_index=True
    )
    cID = models.ForeignKey(
        CompanyInfo, verbose_name='公司编号', db_index=True
    )


class JobRequire(models.Model):
    objects = models.Manager()
    jID = models.ForeignKey(
        JobBasic, verbose_name='职位编号', db_index=True
    )
    jExperience = models.IntegerField(
        verbose_name='工作经验年数', default=0
    )
    jDegree = models.CharField(
        max_length=10, verbose_name='学历要求'
    )
    jNum = models.IntegerField(
        verbose_name='需要人数'
    )
    jSkills = models.CharField(
        max_length=30, verbose_name='需要技能'
    )

    class Meta:
        verbose_name = '工作要求技能'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.jID)


class JobInfo(models.Model):
    objects = models.Manager()
    jID = models.ForeignKey(
        JobBasic, verbose_name='职位编号', db_index=True
    )
    jTags = models.CharField(
        max_length=50, verbose_name='职位标签'
    )
    jDescription = models.TextField(
        verbose_name='职位描述'
    )

    class Meta:
        verbose_name = '职位详细信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.jID)


class JobOthers(models.Model):
    objects = models.Manager()
    jID = models.ForeignKey(
        JobBasic, verbose_name='职位编号', db_index=True
    )
    jLocation = models.CharField(
        max_length=100, verbose_name='职位地址'
    )
    jDepartment = models.CharField(
        max_length=10, verbose_name='工作部门'
    )

    class Meta:
        verbose_name = '职位其他信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.jLocation
