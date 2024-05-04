from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)
    total_copies_sold = models.CharField(max_length=100, default='Unknown')
    series = models.CharField(max_length=100, default='Unknown')
    release_date =  models.CharField(max_length=100, default='Unknown')
    genre = models.CharField(max_length=100, default='Unknown')
    developer = models.CharField(max_length=100, default='Unknown')
    publisher = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'myapi'