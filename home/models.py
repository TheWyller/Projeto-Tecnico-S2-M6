from django.db import models


class Home(models.Model):
    file = models.FileField(upload_to='infos')
