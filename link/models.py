from djongo import models


class Link(models.Model):
    url = models.URLField()
    short_url = models.CharField(unique=True, max_length=10, db_index=True, blank=True, verbose_name='Сокращение')
    date_created = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.short_url

