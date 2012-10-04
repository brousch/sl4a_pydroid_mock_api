# Find some kind of TTS functionality and assign it to ttsSpeak
# On OSX, we use the built-in TTS feature
# On Linux, we look for:
#     Flite, which is small and widely available
#            http://www.speech.cs.cmu.edu/flite/
#     <Add other TTS engines here as they are implemented>
# On Windows, we use notts, which just echoes the message to the console


import subprocess
import sys

from utils import whereis_exe


def ttsSpeak_flite(message):
    ''' Speaks the message using flite '''
    subprocess.call(["flite", "-t", message, "play"])
    

def ttsSpeak_notts(message):
    ''' Echoes the message to the console '''
    print 'FakeTTS: %s' % message


def ttsSpeak_osx(message):
    ''' Speaks the message using built-in OSX TTS '''
    subprocess.call(["say", message])


# Default to notts
ttsSpeak = ttsSpeak_notts

# Platform-specific searches
if sys.platform == "darwin":
    ttsSpeak = ttsSpeak_osx
    
elif sys.platform.startswith('linux'):
    #Check for flite
    if whereis_exe('flite'):
        ttsSpeak = ttsSpeak_flite
        
elif sys.platform == "win32":
    pass
