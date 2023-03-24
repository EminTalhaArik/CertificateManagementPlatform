from django.db import models

class Participant(models.Model):
    participant_name = models.CharField(max_length=200, null=False)
    participant_mail = models.EmailField(max_length=254, null=False, unique=True)
    
    def save(self, force_insert=False, force_update=False):
        self.participant_mail = self.participant_mail.lower()
    
    def __str__(self):
        return self.participant_name

class EventType(models.Model):
    title = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.title

class Event(models.Model):
    event_name = models.CharField(max_length=254, null=False, default='')
    event_date = models.CharField(max_length=100, null=False)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE, null=True)
    event_participants = models.ManyToManyField(Participant)

    def __str__(self):
        return self.event_name
