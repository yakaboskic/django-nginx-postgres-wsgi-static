from django.db import models

ALGORITHM_CHOICES = [(1, 'JUMP3')]

class AlgorithmResult(models.Model):
    #TODO: Eventually make database entry for each algorithm, passing hyperparams into request
    created = models.DateTimeField(auto_now_add=True)
    algorithm = models.CharField(choices=ALGORITHM_CHOICES, default='JUMP3', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='algorithm_result', on_delete=models.CASCADE)
    dataset = models.FilePathField()
    class Meta:
        ordering = ['created', 'algorithm', 'owner', 'dataset']
