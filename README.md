# PROJECT MOVED

This project has been merged into [i3blocks-contrib](https://github.com/vivien/i3blocks-contrib),
which I maintain.
Please send any bug reports, pull requests, or stars that way.

i3blocks-battery is an i3blocks blocklet script to output the current status of your battery.

Dependencies: fonts-font-awesome, acpi, python3

Suggested: i3 ( >= 4.3 ), i3blocks ( >= 1.4 )

It looks like this:

![](images/full.png)

![](images/charging.png)

![](images/unplugged.png)

![](images/unknown.png)

![](images/nobattery.png)

To use with i3blocks, copy the blocklet configuration in the given `i3blocks.conf` into your i3blocks configuration file, the recommended config is

```INI
[battery]
command=$SCRIPT_DIR/battery.py
markup=pango
interval=30
```
