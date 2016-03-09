#!/usr/local/bin/python3

'''
Author: Edgar S. Hurtado (http://edgarsh.es) 2016.

This script sends all the spanish subtitles by email founded in the current
working directory.

Feel free to edit and use it.
'''

import os
from subprocess import call, Popen, PIPE

'''
Obtain a list with the subtitles files names.
Change the regExp in the cmd string for a different subs name format
'''

cmd = "ls | grep 'es[0-9]*\.srt'"
p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
output, err = p.communicate()
output = output.decode("utf-8").split()
print (output)  # For feedback

# Prepare attachment string
if len(output) > 0:  # In case there are no subtitles found

    attachmentString = "(uuencode " + output[0] + " " + output[0]
    for i in range(1, len(output)):
        attachmentString += ";uuencode " + output[i] + " " + output[i]
    attachmentString += ")"

    # --Mail settings--
    subject = os.getcwd()  # The name of the current folder as subject
    # email set in an outter file for
    to = open("email.txt").readline()

    # Send mail
    call(attachmentString + " | mailx -s '" + subject + "' " + to, shell=True)

else:
    print ("No subtitles found")
