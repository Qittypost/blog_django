from re import sub
from datetime import timedelta
from django.db import models
from django.utils import timezone


# def define(text: str):
#     def wrap(cls):
#         def __str__(self):
#             return sub(
#                 r"<\s*(\w+)\s*>",
#                 lambda match: getattr(self, match.group(1)),
#                 text
#             )
#
#         cls.__str__ = __str__
#         return cls
#     return wrap


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, default=None, related_name='post')

    def published_recently(self):
        return timezone.now() - timedelta(days=7) < self.publish_date

    def __str__(self):
        return f'{self.title}, {self.publish_date}'
