asobot
======

IRC bot that can pass commands to a game emulator.

#Description
Asobot is a simple and hacked way to pass keypresses generated by IRC chat commands to game emulators (or basically any aplication in an UNIX xwindows environment).
A better method would be some kind of python plugin or using a network interface, but this was quicker.
The package provides an IRC bot (asobot.py) that listens for commands. If the correct commands are heard, it passes them as key presses to a known game emulator.

#Commands and Syntax
Commands must begin with a colon(:) and may contain the following:
* u = Up (note lower case 'u')
* d = Down
* l = Left
* r = Right
* a = primary "a" button
* b = primary "b" button
* U = N64 yellow directional up (note UPPER CASE)
* D = N64 yellow directional down
* L = N64 yellow directional left
* R = N64 yellow directional right
* z = N64 central Z button
* 1 = left shoulder button
* 3 = right shoulder button
* 8, 2, 4, 6: secondary joystick (u, d, l, r)
* + = keydown only
* - = Keyup only
* t1000 = a pause of 1 second (1000 milliseconds) carried out between commands
* p = pause or unpause the emulator itself

Note that the shoulder and joystick directions can be more easily remembered if one looks at eh numer keypad.


##examples:
Pressing Up, Up, Left, Left, Right, Right and "A" buttons in series:
```
:u u l l r r a
```
To press two or more buttons at the same time, remove the space between the commands. So the following are the 4 non cardinal directions (upper left, upper right, etc..):
```
: ul ur dl dr
```
which is equivalent to:
```
:lu ru ld rd
```
You can also mix in the `+` and `-` symbols to emulate pressing a key and HOLDING it or RELEASING it.
So the following presses right shoulder button and holds it
```
:3+
```
Following this, the same key could then be released (and SHOULD BE) by the following:
```
: 3-
```
The location of the `+` and `-` symbols do not matter. They are applied to the group they're in.

Additionally key pauses can be inserted between other commands. These must be expressed in milliseconds and in the formt "t<number of milliseconds>". So "t1000" is a 1 second pause. This is ueseful for making sure certain keypresses do not overlap or interfere with others. For example the following:
```
:u 3+ t1000 D 3-
```
This presses "up", holds down the right shoulder (3+) waits one second and then presses yellow down (D) before releasing the right shoulder button (3-). Pause commands can't be combined with others. They must be separated by spaces from other commands.


#TODO:
This is pretty clunky. What's needed is the following:
* A better way to queue commands to the emulator in a generic and nonblocking manner.
* A better api to pass keys (or network commands) to the emulator.
