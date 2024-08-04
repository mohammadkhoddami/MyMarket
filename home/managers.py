from django.db import models


class ActiveCommentManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super(ActiveCommentManager, self).get_queryset().filter(status=True)
