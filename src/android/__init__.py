import random
import time
import sys
from collections import namedtuple

import toast

# Initialize tts engine
if sys.platform == "darwin":
    import tts_osx
    tts_engine = tts_osx.TtsEngine()
else:
    try:
        import pyttsx
        tts_engine = pyttsx.init()
    except ImportError:
        class _FakeTTSEngine(object):
            def say(self, message):
                print 'FakeTTS: %s' % message
            
            def runAndWait(self):
                pause_for_realism()
            
        tts_engine = _FakeTTSEngine()
    
try:
    import androidhelper
    """androidhelper is a modified copy from
    https://groups.google.com/forum/?fromgroups#!topic/python-for-android/a26ponFlgho
    or http://code.google.com/p/python-for-android/downloads/detail?name=androidhelper.py
    
    This provides doc strings from SL4A. androidhelper has been modified via:
    
        in_filename = 'androidhelper_r6.py'
        out_filename = 'androidhelper.py'

        fin = open(in_filename)
        fout = open(out_filename, 'w')
        for line in fin:
            if line.startswith('import'):
                line = '# ' + line
            if line.startswith('class Android(android.Android):'):
                line = line.replace('class Android(android.Android):', 'class Android:  # class Android(android.Android):')
            '''
            if line.startswith('class Android(android.Android):'):
                line = line.replace('(android.Android)', '')
            '''
            if 'return' in line:
                line = line.replace('return', 'raise NotImplementedError()  # return')
            fout.write(line)
        fout.close()
        fin.close()
    """
except ImportError:
    androidhelper = None


# Pause for a little while for a more realistic experience from some methods
DEFAULT_PAUSE_TIME = 2
def pause_for_realism(secs=DEFAULT_PAUSE_TIME):
    time.sleep(secs)
    

# A fake Result such as many Android API calls return
Result = namedtuple('Result', 'id, result, error')


def static_var(varname, value):
    ''' Decorator to add a static var to a function'''
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate


@static_var("last_id", 0)
def get_id():
    get_id.last_id += 1
    return get_id.last_id


def copydoc(cls):
    # From https://groups.google.com/forum/?fromgroups#!topic/comp.lang.python/HkB1uhDcvdk
     def _fn(fn):
         if fn.__name__ in cls.__dict__:
             fn.__doc__ = cls.__dict__[fn.__name__].__doc__
         return fn
     return _fn

if androidhelper is None:
    parent_class = object
else:
    parent_class = androidhelper.Android

class Android(parent_class):
    
    @copydoc(parent_class)
    def makeToast(self, message):
        ''' Pops up a Tkinter window with the message for 5 seconds'''
        toast.show_toast(message)
        
    
    @copydoc(parent_class)
    def ttsIsSpeaking(self):
        still_speaking = random.choice((False, True))
        if still_speaking:
            print "\n*** THE DEVICE IS STILL SPEAKING ***"
        else:
            print "\n*** THE DEVICE IS DONE SPEAKING ***"
        return (get_id(), still_speaking)
        
        
    @copydoc(parent_class)
    def ttsSpeak(self, message):
        tts_engine.say(message)
        tts_engine.runAndWait()
    
    
    @copydoc(parent_class)
    def recognizeSpeech(self, prompt="", language="English", 
                        languageModel="web_Search"):
        print "\n*** TOTALLY FAKE ATTEMPT AT RECOGNIZING SPEECH ***"
        recognized_speech = raw_input('Enter what you think I heard: ')
        pause_for_realism()
        result = Result(id=get_id(),
                        result=recognized_speech,
                        error=None)
        return result
    
    