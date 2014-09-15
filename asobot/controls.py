#!/usr/bin/env python 
# vim: set ts=2 expandtab:
# -*- coding: utf-8 -*-
"""

Module: control.py
Desc: send kepresses to an XWINDOWS window by name
Author: on_three
Email: on.three.email@gmail.com
DATE: Sunday, Sept 9th 2014
  
"""

import argparse
import os

keys = [
	u'Up',
	u'Down',
	u'Left',
	u'Right',
	u'Return',
	u'space',
	u'a',
	u'b',
	u's',
]

class Key(object):
	@staticmethod
	def press(key, windowname, delay=150):
		'''Make a simple system call to press a button on a window
		'''
		if key not in keys:
			return
		os_call = u'HWID=`xwininfo -name "{windowname}" | grep "Window id" | cut -d" " -f4`; \
			DWID=$(($HWID)); \
			xdotool windowfocus $DWID; \
			xdotool  keydown --delay {delay} {key} keyup {key}'.format(
			#xdotool  key --window "$DWID" {key}'.format(
				windowname=windowname,
				key=key,
				delay=unicode(delay))
		retvalue = os.system(os_call.encode('utf-8'))


def main():
  parser = argparse.ArgumentParser(description='Send keypresses to windows by name.')
  parser.add_argument('windowname', help='Target window name.', type=str)
  parser.add_argument('key', help='Key press to pass to window.', type=str)
  args = parser.parse_args()

  windowname = args.windowname.decode('utf-8')
  key = args.key.decode('utf-8')
  Key.press(key, windowname)

if __name__ == "__main__":
  main()
