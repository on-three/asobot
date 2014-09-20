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
import time
import re

keymap = {
	u'u' : u'w',
	u'd' : u's',
	u'l' : u'a',
	u'r' : u'd',
	u'a' : u'shift',
	u'b' : u'ctrl',
	u's' : u'Return',
	#u'x' : u'x',
	u'1' : u'x',#"hidari" for left shoulder button
	u'3' : u'c',#"migi" for right shoulder button
	u'z' : u'z',#N64 z button
	u'5' : u'z',#N64 z button
	u'U' : u'i',#yellow up
	u'D' : u'k',#yellow down
	u'L' : u'j',#yellow left
	u'R' : u'l',#yellow right
	u'8' : u'Up', #joystick up
	u'2' : u'Down',
	u'4' : u'Left',
	u'6' : u'Right',
	u'x' : u'F9',#reset emulator (standard mupen64plus key)
	u'p' : u'p', #emulator pause (not pause betwen issuing comands! note!)
}

PAUSE_REGEX = ur't(?P<pause>[\d+])'

class Key(object):
	@staticmethod
	def press(key, windowname, delay=50):
		'''Make a simple system call to press buttons on windows.
		The input "key" can be a group of keys that are all pressed together.
		In other words, if the key is "lu" we will first press l, then u, wait
		the given keypress period, then release both.
		this allows diagonal moves as well as "press x while y" type presses
		such as are used in Pokemon Stadium.
		'''
		#first, does the key entered match the pause regex?(i.e. of the form "p1000" for
		#a one second delay)
		#the pause implemented here is blocking. which is a pretty dumb thing to do
		#but i'll have to build some sort of message queue to implement it better.
		if re.match(key, PAUSE_REGEX):
			pause = re.match(key, PAUSE_REGEX).groupdict()['pause']
			time.sleep(float(delay)/1000.0)
			return
		keys = [k for k in list(key)]
		#If the sequence contains "+" it's keydown only
		#if the sequence contains "-" it's keyup only
		keydown_only = False
		if u'+' in keys:
			keydown_only = True
		keyup_only = False
		if u'-' in keys:
			keyup_only = True
 		for k in keys:
 			if keyup_only: break
			if k not in keymap:
				continue
			button = keymap[k]
			os_call = u'HWID=`xwininfo -name "{windowname}" | grep "Window id" | cut -d" " -f4`; \
				DWID=$(($HWID)); \
				xdotool windowfocus $DWID; \
				xdotool  keydown {button}'.format(
				windowname=windowname,
				button=button)
			os.system(os_call.encode('utf-8'))
			#wait n milliseconds
		time.sleep(float(delay)/1000.0)
		for k in keys:
			if keydown_only: break
			if k not in keymap:
				continue
			button = keymap[k]
			os_call = u'HWID=`xwininfo -name "{windowname}" | grep "Window id" | cut -d" " -f4`; \
				DWID=$(($HWID)); \
				xdotool windowfocus $DWID; \
				xdotool keyup {button}'.format(
				windowname=windowname,
				button=button)
			os.system(os_call.encode('utf-8'))



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
