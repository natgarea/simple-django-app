from django.db import models
from core.models import CommonInfo


class Bar(CommonInfo):
    name = models.CharField("Name", max_length=200)
