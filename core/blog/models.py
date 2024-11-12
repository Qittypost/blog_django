from re import sub
from django.db import models


def define(text: str):
    def wrap(cls):
        def __str__(self):
            return sub(
                r"<\s*(\w+)\s*>",
                lambda match: getattr(self, match.group(1)),
                text
            )

        cls.__str__ = __str__
        return cls
    return wrap


@define('Post: <title>')
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)

