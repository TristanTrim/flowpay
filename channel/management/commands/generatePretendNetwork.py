
from django.core.management.base import BaseCommand, CommandError
import channel.models as cm
import names
from pymarkovchain import MarkovChain
mc = MarkovChain('markov')
from random import choice as randomChoice


class Command(BaseCommand):
    help="generates silly data for the sake of demo, or whatever."
    def add_arguments(self, parser):
        parser.add_argument('iterations', type=int)

    def handle(self, *args, **kwargs):
        doables = [genRandUser,genRandChannel]
        for i in range(0,kwargs['iterations']):
            print(i)
            randomChoice(doables)()

def genRandUser():
    newUser = cm.user(name=names.get_full_name())
    newUser.save()
    print("{} - user added".format(newUser.name))

def genRandChannel():
    while True:
        prospectiveName = mc.generateString()
        if len(prospectiveName) < 128:# I doubt this will enter an infinite loop.
            break
    newChannel = cm.channel(name=prospectiveName)
    newChannel.save()
    print("{} - channel added.".format(newChannel.name))
