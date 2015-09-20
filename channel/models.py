from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=128,null=True,blank=True)
    def save(self, *args, **kwargs):
        super(user,self).save()
        ## this needs to not say 'bank, or paypal, or something'
        output(user=self,name='bank, or paypal, or something').save()

class output(models.Model):
    "represents a destination to which money can be directed."
    user = models.ForeignKey(user,null=True,blank=True)
    name = models.CharField(max_length=128,null=True,blank=True)
    amount = models.FloatField(default=0)#the amount getting donated to here
    origins = models.ManyToManyField('input')

class channel(models.Model):
    name = models.CharField(max_length=128,null=True,blank=True)
    amount = models.FloatField(default=0)#the amount channeling through
    channels = models.ManyToManyField('channel')
    outputs = models.ManyToManyField(output)

class input(models.Model):
    "represents a source by which money comes into the system."
    user = models.ForeignKey(user,null=True,blank=True)
    name = models.CharField(max_length=128,null=True,blank=True)
    amount = models.FloatField(default=10)
    target = models.ForeignKey(channel)
    destinations = models.ManyToManyField(output)



