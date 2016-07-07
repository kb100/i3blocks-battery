i3blocks-battery is an i3blocks blocklet script to output the current status of your battery.

Dependencies: fonts-font-awesome, acpi, python3

Suggested: i3 ( >= 4.3 ), i3blocks ( >= 1.4 )

It looks like this:

![](https://raw.githubusercontent.com/kb100/i3blocks-battery/master/images/1.png)

To use with i3blocks, copy the blocklet configuration in the given `i3blocks.conf` into your i3blocks configuration file, the recommended config is

```INI
[battery]
command=$SCRIPT_DIR/battery.py
markup=pango
interval=30
```
