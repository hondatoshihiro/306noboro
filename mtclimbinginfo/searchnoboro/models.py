from django.db import models
from setuptools import SetuptoolsDeprecationWarning

# Create your models here.

class Noboro(models.Model):
    #巻番号
    volno = models.IntegerField(null=False, blank=False)
    #年
    year = models.IntegerField(null=False, blank=False)
    #季刊
    season = models.CharField(max_length=8, null=False, blank=False)

    def __str__(self):
        return '<Noboro:' + str(self.volno) + ', ' + str(self.year) + ', ' + str(self.season) + '>'

class NoboroContent(models.Model):
    #記事タイトル
    title = models.CharField(max_length=1024, null=False, blank=False)
    #記事サブタイトル
    subtitle = models.CharField(max_length=1024, null=True, blank=True)
    #ページ
    pageno = models.IntegerField(default=0)
    #内容
    content = models.CharField(max_length=2048, null=True, blank=True)
    #外部キー(Noboro:1-NoboroContent:n)
    noboro = models.ForeignKey(Noboro, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '<NoboroContent:' + self.title + ', ' + self.subtitle + '>'

class Prefecture(models.Model):
    #県コード
    prefcode = models.IntegerField(default=0)
    #県名
    prefname = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return '<Prefecture:' + str(self.prefcode) + ', ' + self.prefname + '>'

class Mountain(models.Model):
    #山名
    name = models.CharField(max_length=1024, null=False, blank=False)
    #山名(読み)
    readname = models.CharField(max_length=2048, null=False, blank=False)
    #標高
    height = models.FloatField(default=0, null=False, blank=False)
    #地図URL
    mapurl = models.URLField(max_length=2048, null=True, blank=True) 
    #県(外部キー)(Mountaion:1-Prefecture:n)
    prefecture = models.ManyToManyField(Prefecture, null=True, blank=True)
    #記事(外部キー)(NoboroContent:n-Mountaion:n)
    noborocontent = models.ManyToManyField(NoboroContent, null=True, blank=True) 

    def __str__(self):
        return '<Mountain:' + self.name + ", " + str(self.height) + '>'
