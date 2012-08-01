#!/usr/bin/env python

# This script modifies an original version of androidhelper_r6.py to work with
# sl4a_pydroid_mock_api
#
# androidhelper is a modified copy from
# https://groups.google.com/forum/?fromgroups#!topic/python-for-android/a26ponFlgho
# or http://code.google.com/p/python-for-android/downloads/detail?name=androidhelper.py
#
# This code was provided by clach04

in_filename = 'androidhelper_r6.py'
out_filename = 'androidhelper.py'

fin = open(in_filename)
fout = open(out_filename, 'w')
for line in fin:
    if line.startswith('import'):
        line = '# ' + line
    if line.startswith('class Android(android.Android):'):
        line = line.replace('class Android(android.Android):', 
                            'class Android():  # class Android(android.Android):')
        if 'return' in line:
            line = line.replace('return',
                                'raise NotImplementedError()  # return')
    fout.write(line)
fout.close()
fin.close()