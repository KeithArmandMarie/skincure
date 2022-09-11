from uuid import uuid4
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, unique=True,default=uuid.uuid4, editable = False)
    
    