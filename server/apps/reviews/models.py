from django.db import models
from django.conf import settings
from comics.models import Comic
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    # Userモデルへの参照。DjangoのデフォルトUserモデルを使用
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    # Comicモデルへの参照
    comic = models.ForeignKey(
        Comic,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    isfavorite = models.BooleanField(default=False)
    score_1 = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    score_2 = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    score_3 = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    score_4 = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    score_5 = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    comment = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return f"Review by {self.user.username} on {self.comic.title}"

