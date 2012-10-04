A Mock API for SL4A's Python Android API
========================================

This project provides an API to mimic the Python API provided by the `Scripting
Language for Android`_ project. The SL4A Android API can only be run on an
actual Android device, which can make development cumbersome. This project
provides an API very similar to the one on Android, but it is designed for use
on a desktop operating system such as Linux, OSX, and Windows.

The SL4A Android API is very large and allows you to interact with almost
every part of the Android operating system. For each of these features I have
to find a similar desktop feature and hook into it. Sometimes there is nothing
similar available. Because of this, this project will likely never be able to 
emulate every piece of the API.

I am building this project as I come across SL4A Python API features that I
need to use. At the present time, I am not attempting to simulate the entire 
API. If you need a feature that hasn't yet been implemented, please fork this 
project, code it up, and make a pull request. Your contributions will be 
welcomed. 

.. _`Scripting Language for Android`: http://code.google.com/p/android-scripting/

Installation
------------

From your SL4A project's virtualenv: *pip install sl4a_pydroid_api*

This creates an *android* module which you can import just like a regular
SL4A project.

Further Instructions for Text To Speech (ttsSpeak)
--------------------------------------------------

On OSX, it uses the built-in 'say' program. No other action is necessary. If 
for some strange reason 'say' is missing, you can also install and use 
`espeak`_.

On Linux, you can install and use `espeak`_ or `flite`_.

On Windows, you can install and use `espeak`_.

If no TTS program can be found, it will default to printing the message to the
console.

Special thanks to
-------

- `androidhelper`_
- `modern-package-template`_

.. _espeak: http://espeak.sourceforge.net/
.. _flite: http://www.speech.cs.cmu.edu/flite/
.. _androidhelper: https://groups.google.com/forum/?fromgroups#!topic/python-for-android/a26ponFlgho
.. _`modern-package-template`: http://pypi.python.org/pypi/modern-package-template

