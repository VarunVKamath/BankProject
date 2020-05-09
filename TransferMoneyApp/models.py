from django.db import models
import django.utils.timezone
# Create your models here.
class BankStatement(models.Model):

	Transaction_Date=models.DateTimeField(default=(django.utils.timezone.now))
	Sender=models.CharField(max_length=255)
	Receiver=models.CharField(max_length=255)

	Sender_acc=models.IntegerField()
	Receiver_acc=models.IntegerField()

	Transaction_Value=models.IntegerField()
	Sender_Balance=models.IntegerField()
	Receiver_Balance=models.IntegerField()
	