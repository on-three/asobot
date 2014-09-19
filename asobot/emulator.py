# vim: set ts=2 expandtab:
# -*- coding: utf-8 -*-
"""

Module: Emulator.py
Desc: pass keypresses to a game emultor or something.
Author: on_three
Email: on.three.email@gmail.com
DATE: Thursday, Jan 16th 2014
  
"""
import string
import re
from twisted.python import log

from controls import Key

class Emulator(object):
  '''
  pass commands to a game emulator of some sort.
  '''
  COMMAND_REGEX = ur'^(?P<command>:)(?P<commands>.+)$'

  def __init__(self, parent, emulator_window_name):
    '''
    constructor
    '''
    self._parent = parent
    self._window_name = emulator_window_name

  def is_msg_of_interest(self, user, channel, msg):
    '''
    PLUGIN API REQUIRED
    Is the rx'd irc message of interest to this plugin?
    '''
    m = re.match(Emulator.COMMAND_REGEX, msg)
    if m:
      log.msg('Message of interest...')
      return True
    else:
      return False

  def handle_msg(self, user, channel, msg):
    '''
    PLUGIN API REQUIRED
    Handle message and return nothing
    '''
    log.msg('{channel} : {msg}'.format(channel=channel, msg=msg))
    m = re.match(Emulator.COMMAND_REGEX, msg)
    if not m:
      return
    #got a command along with the .c or .channel statement
    commands = m.groupdict()['commands']
    self.keypresses_to_emulator(commands, channel)

  def keypresses_to_emulator(self, keys, channel):
    '''
    Split commands by spaces. Each non spaced group represents
    a series of buttons (or joystick directions) pressed TOGETHER
    '''
    presses = [x.strip() for x in keys.split(u' ')]
    for p in presses:
      Key.press(p, self._window_name)


