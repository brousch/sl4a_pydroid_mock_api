#!/usr/bin/env python

# I had trouble getting pyttsx to work with anthing except the system Python 
# on OSX. This module implements the same basic API as pyttsx. It uses OSX's
# built-in 'say' command via subprocess.

import subprocess

class TtsEngine():
    def __init__(self):
        self.message = ""
    
    def say(self, message):
        ''' Stores the message, doesn't actually speak yet'''
        self.message = message
    
    def runAndWait(self):
        ''' Speaks the stored message'''
        subprocess.call(["say", self.message])
