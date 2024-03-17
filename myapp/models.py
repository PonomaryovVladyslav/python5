from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _

GENRE_CHOICES = (
    (1, _("Not selected")),
    (2, _("Comedy")),
    (3, _("Action")),
    (4, _("Beauty")),
    (5, _("Other"))
)


class Author(models.Model):
    pseudonym = models.CharField(max_length=120,
                                 blank=True,
                                 null=True)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Article(models.Model):

    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               null=True,
                               related_name='articles')
    text = models.TextField(max_length=10000,
                            null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genre = models.IntegerField(choices=GENRE_CHOICES,
                                default=1)

    def __str__(self):
        return f"Author - {self.author.name}, genre - {self.genre}, id - {self.id}"


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    article = models.ForeignKey(Article,
                                on_delete=models.DO_NOTHING)
    comment = models.ForeignKey('myapp.Comment',
                                null=True,
                                blank=True,
                                on_delete=models.DO_NOTHING,
                                related_name='comments')
    user = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.text} by {self.user.username}"


class Like(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article,
                                on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"By user {self.user.username} to article {self.article.id}"

    class Meta:
        unique_together = ['user', 'article']
