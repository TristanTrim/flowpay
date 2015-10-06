from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=128,null=True,blank=True)
    recievingChannel = models.OneToOneField('channel',related_name='recieving_user')
    givingChannel = models.OneToOneField('channel',related_name='giving_user')
    def save(self,*args,**kwargs):
        recievingChannel = channel(name="{}'s recieving channel".format(self.name))
        recievingChannel.save()
        self.recievingChannel = recievingChannel
        givingChannel = channel(name="{}'s giving channel".format(self.name))
        givingChannel.save()
        self.givingChannel = givingChannel
        super(user,self).save(*args,**kwargs)
    def addGivingAccount(self,accountInfo):
        # it's a funny joke, 'accountInfo' is a string right now.
        source(user=self,name=accountInfo,target=self.givingChannel).save()
    def addRecievingAccount(self,accountInfo):
        # it's still a funny joke, 'accountInfo' is a string right now.
        destination(user=self,name=accountInfo).save()
    def __unicode__(self):
        return(self.name)
    def __str__(self):
        return(unicode(self).encode('utf-8'))

class destination(models.Model):
    "represents a destination to which money can be directed."
    user = models.ForeignKey(user,null=True,blank=True)
    name = models.CharField(max_length=128,null=True,blank=True)
    amount = models.FloatField(default=0)#the amount getting donated to here
    sources = models.ManyToManyField('source')
    def __unicode__(self):
        return("{0}'s account: {1}".format(self.user,self.name))
    def __str__(self):
        return(unicode(self).encode('utf-8'))

class channel(models.Model):
    name = models.CharField(max_length=128,null=True,blank=True)
    amount = models.FloatField(default=0)#the amount channeling through
    channels = models.ManyToManyField('channel')
    sources = models.ManyToManyField('source')
    destinations = models.ManyToManyField(destination)
    def __unicode__(self):
        return(self.name)
    def __str__(self):
        return(unicode(self).encode('utf-8'))

class source(models.Model):
    "represents a source by which money comes into the system."
    user = models.ForeignKey(user,null=True,blank=True)
    name = models.CharField(max_length=128,null=True,blank=True)
    amount = models.FloatField(default=0)
    # this will always be the users giving channel.
    target = models.ForeignKey(channel)
    destinations = models.ManyToManyField(destination)
    def __unicode__(self):
        return("{0}'s account: {1}".format(self.user,self.name))
    def __str__(self):
        return(unicode(self).encode('utf-8'))



