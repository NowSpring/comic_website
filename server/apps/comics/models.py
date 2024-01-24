import os
from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class Comic(models.Model):
    
    ERA_TYPES = (
        ("1980", "1980"),
        ("1990", "1990"),
        ("2000", "2000"),
        ("2010", "2010"),
    )
    
    PUBLISHER_TYPES = (
        ("エニックス", "エニックス"),
        ("学習研究科", "学習研究科"),
        ("小学館", "小学館"),
        ("少年画報社", "少年画報社"),
        ("徳間書店", "徳間書店"),
        ("朝日ソラノマ", "朝日ソラノマ"),
        ("東京三世社", "東京三世社"),
        ("白泉社", "白泉社"),
        ("秋田書店", "秋田書店"),
        ("竹書房", "竹書房"),
        ("芳文社", "芳文社"),
        ("角川書店", "角川書店"),
        ("講談社", "講談社"),
        ("集英社", "集英社"),
    )
    
    TARGET_TYPES = (
        ("少女", "少女"),
        ("少年", "少年"),
        ("女性", "女性"),
        ("男性", "男性"),
    )
    
    GENRE_TYPES = (
        ("4コマ", "4コマ"),
        ("SF", "SF"),
        ("ギャグ", "ギャグ"),
        ("サスペンス", "サスペンス"),
        ("スポーツ", "スポーツ"),
        ("バトル", "バトル"),
        ("ファンタジー", "ファンタジー"),
        ("ホラー", "ホラー"),
        ("ラブコメ", "ラブコメ"),
        ("動物", "動物"),
        ("恋愛", "恋愛"),
        ("時代劇", "時代劇"),
    )
    
    title = models.CharField(verbose_name = "タイトル", max_length = 100)
    author = models.CharField(verbose_name = "作者", max_length = 100)
    era = models.CharField(verbose_name = "年代", max_length = 100, choices = ERA_TYPES)
    publisher = models.CharField(verbose_name = "出版社", max_length = 100, choices = PUBLISHER_TYPES)
    target = models.CharField(verbose_name = "対象", max_length = 100, choices = TARGET_TYPES)
    genre = models.CharField(verbose_name = "ジャンル", max_length = 100, choices = GENRE_TYPES)
    cover = models.ImageField(upload_to = "cover/", null = False, blank = True)
    pdf = models.FileField(upload_to = "pdf/", validators = [FileExtensionValidator(['pdf'])])
    
    def __str__(self):
        
        return self.title