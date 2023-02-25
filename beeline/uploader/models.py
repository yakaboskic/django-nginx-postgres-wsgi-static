from django.db import models


class Dataset(models.Model):
    owner = models.ForeignKey('auth.User', related_name='dataset', on_delete=models.CASCADE)
    file = models.FileField(upload_to='usr-datasets')
    upload_at = models.DateTimeField(auto_now_add=True)
