from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=128,null=True,blank=True)
    inputChannel = models.OneToOneField('channel',related_name='input_user')
    outputChannel = models.OneToOneField('channel',related_name='output_user')
    def save(self,*args,**kwargs):
        inputChannel = channel(name="{}'s input".format(self.name))
        inputChannel.save()
        self.inputChannel = inputChannel
        outputChannel = channel(name="{}'s output".format(self.name))
        outputChannel.save()
        self.outputChannel = outputChannel
        super(user,self).save(*args,**kwargs)
    def __unicode__(self):
        return(self.name)
    def __str__(self):
        return(unicode(self).encode('utf-8'))

class output(models.Model):
    "represents a destination to which money can be directed."
    user = models.ForeignKey(user,null=True,blank=True)
    name = models.CharField(max_length=128,null=True,blank=True)
    amount = models.FloatField(default=0)#the amount getting donated to here
    origins = models.ManyToManyField('input')
    def __unicode__(self):
        return(self.name)
    def __str__(self):
        return(unicode(self).encode('utf-8'))

class channel(models.Model):
    name = models.CharField(max_length=128,null=True,blank=True)
    amount = models.FloatField(default=0)#the amount channeling through
    channels = models.ManyToManyField('channel')
    outputs = models.ManyToManyField(output)
    def __unicode__(self):
        return(self.name)
    def __str__(self):
        return(unicode(self).encode('utf-8'))

class input(models.Model):
    "represents a source by which money comes into the system."
    user = models.ForeignKey(user,null=True,blank=True)
    name = models.CharField(max_length=128,null=True,blank=True)
    amount = models.FloatField(default=10)
    target = models.ForeignKey(channel)
    destinations = models.ManyToManyField(output)
    def __unicode__(self):
        return(self.name)
    def __str__(self):
        return(unicode(self).encode('utf-8'))



