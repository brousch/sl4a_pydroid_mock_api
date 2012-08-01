#!/usr/bin/env python

# For folks without any kind of TTS available. This echoes what would be spoken
# to the output. This module implements the same basic API as pyttsx.

class FakeTTSEngine(object):
    
    def __init__(self):
        self.message = ""
        
    def say(self, message):
        ''' Stores the message, doesn't actually speak yet'''
        self.message = message
            
    def runAndWait(self):
        ''' Echoes the stored message'''
        print 'FakeTTS: %s' % self.message
