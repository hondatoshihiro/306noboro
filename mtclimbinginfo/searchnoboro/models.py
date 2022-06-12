from django.db import models
from setuptools import SetuptoolsDeprecationWarning

# Create your models here.

class Noboro(models.Model):
    #巻番号
    volno = models.IntegerField()
    #年
    year = models.IntegerField()
    #季刊
    season = models.CharField(max_length=8)

    def __str__(self):
        return '<Noboro:id=' + str(self.id) + ', ' + str(self.volno) + '>'

class NoboroContent(models.Model):
    #記事タイトル
    title = models.CharField(max_length=1024, null=False)
    #記事サブタイトル
    subtitle = models.CharField(max_length=1024, null=True)
    #ページ
    pageno = models.IntegerField(default=0)
    #内容
    content = models.CharField(max_length=2048, null=True)
    #外部キー(Noboro:1-NoboroContent:n)
    noboro = models.ForeignKey(Noboro, on_delete=models.CASCADE)

    def __str__(self):
        return '<NoboroContent=' + str(self.id) + ', ' + self.title + ':' + self.subtitle + '>'
