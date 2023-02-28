from django.db import models


class Dataset(models.Model):
    owner = models.ForeignKey('auth.User', related_name='dataset', on_delete=models.CASCADE, blank=True, null=True)
    upload_at = models.DateTimeField(auto_now_add=True)
    expression_data_file = models.FileField(upload_to='usr-expr-datasets')
    pseudo_time_file = models.FileField(upload_to='usr-pseudo-time-datasets', null=True, blank=True)
    ref_network = models.ForeignKey('ReferenceNetwork', on_delete= models.CASCADE, blank=True, null=True)

class ReferenceNetwork(models.Model):
    owner = models.ForeignKey('auth.User', related_name='refnetwork', on_delete=models.CASCADE, blank=True, null=True)
    file = models.FileField(upload_to='usr-ref-network-datasets', null=True, blank=True)
    upload_at = models.DateTimeField(auto_now_add=True)
