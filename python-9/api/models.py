from django.db import models
from django.core import validators

class User(models.Model):
    name = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    password = models.CharField(max_length=50,
        validators=[validators.MinValueValidator(8)])


class Agent(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField()
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    address = models.GenericIPAddressField(protocol='IPV4')


class Level(models.TextChoices):
    CRITICAL = 'CRITICAL', 'CRITICAL'
    DEBUG = 'DEBUG', 'DEBUG'
    ERROR = 'ERROR', 'ERROR'
    WARNING = 'WARNING', 'WARNING'
    INFO = 'INFO', 'INFO'


class Event(models.Model):

    level = models.CharField(max_length=20,
        choices=Level.choices, default=Level.INFO)
    data = models.TextField()
    arquivado = models.BooleanField()
    date = models.DateField(auto_now_add=True)
    agent = models.ForeignKey(Agent,
        on_delete=models.CASCADE)
    user = models.ForeignKey(User,
        on_delete=models.DO_NOTHING)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(level__in=Level.values),
                name='%(app_label)s_%(class)s_level_valid'
            )
        ]


class Group(models.Model):
    name = models.CharField(max_length=50)


class GroupUser(models.Model):
    group = models.ForeignKey(Group,
        on_delete=models.DO_NOTHING)

    user = models.ForeignKey(User,
        on_delete=models.DO_NOTHING)
