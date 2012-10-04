# Find some kind of TTS functionality and assign it to ttsSpeak
# On OSX, we look for:
#     say: A TTS program included with OSX
#          http://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man1/say.1.html
#     espeak: A free TTS program for Linux, Windows and OSX
#             http://espeak.sourceforge.net/
# On Linux, we look for:
#     espeak: A free TTS program for Linux, Windows and OSX
#             http://espeak.sourceforge.net/
#     flite, A free TTS program for 
#            http://www.speech.cs.cmu.edu/flite/
# On Windows, we look for:
#     espeak: A free TTS program for Linux, Windows and OSX
#             http://espeak.sourceforge.net/
# If no TTS is found, we use notts, which just echoes the message to the console


import subprocess
import sys

from utils import whereis_exe


def ttsSpeak_espeak(message):
    ''' Speaks the message using espeak '''
    subprocess.call(["espeak", message])


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
    if whereis_exe('say'):
        ttsSpeak = ttsSpeak_osx
    elif whereis_exe('espeak'):
        ttsSpeak = ttsSpeak_espeak
    
elif sys.platform.startswith('linux'):
    if whereis_exe('espeak'):
        ttsSpeak = ttsSpeak_espeak
    elif whereis_exe('flite'):
        ttsSpeak = ttsSpeak_flite
        
elif sys.platform == "win32":
    if whereis_exe('espeak'):
        tssSpeak = ttsSpeak_espeak
