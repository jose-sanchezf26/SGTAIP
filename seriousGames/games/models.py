from django.db import models

# Create your models here.
# games/models.py

from django.db import models

class GameMessage(models.Model):
    user = models.CharField(max_length=100)
    session_id = models.CharField(max_length=100)
    game_id = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    time = models.DateTimeField()
    data = models.JSONField()

    def __str__(self):
        return f"{self.user} - {self.game_id} - {self.event_type}"
