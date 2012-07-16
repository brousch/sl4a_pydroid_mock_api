#!/usr/bin/env python

# I had trouble getting pyttsx to work with anthing except the system Python 
# on OSX. This module implements the same basic API as pyttsx. It uses OSX's
# built-in 'say' command via subprocess.

import subprocess

class TtsEngine():
    def __init__(self):
        self.phrase = ""
    
    def say(self, phrase):
        ''' Stores the phrase, doesn't actually speak yet'''
        self.phrase = phrase
    
    def runAndWait(self):
        ''' Speaks the stored phrase'''
        subprocess.call(["say", self.phrase])
