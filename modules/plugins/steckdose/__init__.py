# -*- coding: utf-8 -*-

from modules import cbpi
from modules.core.props import Property
from modules.core.hardware import ActorBase

try:
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
except Exception as e:
    print e
    pass


@cbpi.actor
class SampleActor(ActorBase):
    #custom property 
    prop1 = Property.Text("Property1", True, "1")
    
    def on(self, power=0):
        '''
        Code to switch on the actor
        :param power: int value between 0 - 100
        :return: 
        '''
        print "SWITCH ON %s" % (self.prop1)
        
    def off(self):
        '''
        Code to switch off the actor
        :return: 
        '''
        print "SWITCH OFF"

    def set_power(self, power):
        
        '''
        Optional: Set the power of your actor
        :param power: int value between 0 - 100
        :return: 
        '''
        pass