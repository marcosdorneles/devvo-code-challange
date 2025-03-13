from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Anel(models.Model):
    ELFOS = 'Elfos'
    ANOES = 'Anões'
    HOMENS = 'Homens'
    SAURON = 'Sauron'

    OPCOES_FORJADOR = [
        (ELFOS, 'Elfos'),
        (ANOES, 'Anões'),
        (HOMENS, 'Homens'),
        (SAURON, 'Sauron'),
    ]

    nome = models.CharField(max_length=100)
    poder = models.CharField(max_length=100)
    portador = models.CharField(max_length=100)
    forjadoPor = models.CharField(max_length=100, choices=OPCOES_FORJADOR)
    imagem = models.URLField(max_length=200)

    def clean(self):
        if self.forjadoPor == self.ELFOS and Anel.objects.filter(forjadoPor=self.ELFOS).count() >= 3:
            raise ValidationError(
                'Os Elfos só podem forjar no máximo 3 anéis.')
        elif self.forjadoPor == self.ANOES and Anel.objects.filter(forjadoPor=self.ANOES).count() >= 7:
            raise ValidationError(
                'Os Anões só podem forjar no máximo 7 anéis.')
        elif self.forjadoPor == self.HOMENS and Anel.objects.filter(forjadoPor=self.HOMENS).count() >= 9:
            raise ValidationError(
                'Os Homens só podem forjar no máximo 9 anéis.')
        elif self.forjadoPor == self.SAURON and Anel.objects.filter(forjadoPor=self.SAURON).count() >= 1:
            raise ValidationError('Sauron só pode forjar 1 anel.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome
