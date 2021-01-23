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
        """ Representation of string """
        return self.title
    
    def get_absolute_url(self):
        """ Where to redirect after succesfully store the information to the model """
        return reverse('detail_article', kwargs={'pk':self.pk})
    
    def article_status(self, status):
        """ Set the status of the article by setting the value of published_date. """

        if status:
            self.published_date=timezone.now()
        else:
            self.published_date=None
        self.save()


class CommentModel(models.Model):
    """ Store the comments to article. """

    comment_writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.TextField()
    article = models.ForeignKey(ArticleModel, related_name='comments', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """ Representation of string """
        return self.comment
    
    def get_absolute_url(self):
        """ Where to redirect after succesfully store the information to the model """
        return reverse('detail_article', kwargs={'pk':self.pk})

    