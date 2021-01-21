from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse, reverse_lazy
# Create your models here.


class ArticleModel(models.Model):
    """ Table/model for store an article information. """
    article_writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True, blank=True)

    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail_article', kwargs={'pk':self.pk})
    
    def publish_this(self):
        self.published_date(timezone.now)
        self.save()

