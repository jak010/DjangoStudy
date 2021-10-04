from django.shortcuts import render

from django.dispatch import receiver
from .signals import signal_test


# Create your views here.


@receiver(signal_test)
class SignalHandler:

    def __init__(self, **kwargs):
        self.kwargs = kwargs

        self.run()

    def run(self):
        print("Hello")
