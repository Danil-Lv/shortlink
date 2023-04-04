from djongo import models


class Link(models.Model):
    url = models.URLField(unique=True, db_index=True)
    short_url = models.CharField(unique=True, max_length=10, db_index=True, blank=True, verbose_name='Сокращение')

    def __str__(self):
        return self.short_url

