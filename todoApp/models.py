from django.db import models
import uuid
from django.contrib.auth.models import User

class CustomTodo(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150,null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title



