from django.db import models

class EventType(models.Model):
    title = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.title

class Event(models.Model):
    event_name = models.CharField(max_length=254, null=False, default='')
    event_date = models.CharField(max_length=100, null=False)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE, null=True)
    certificate_file = models.ImageField(upload_to="certificates", null=True)

    def __str__(self):
        return self.event_name
    
class Certificate(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant_name = models.CharField(max_length=100, null=False)
    participant_mail = models.EmailField(max_length=254, null=False)

    def __str__(self) -> str:
        return str(self.id)