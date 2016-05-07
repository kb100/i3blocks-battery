## i3blocks-battery

Is an i3blocks blocklet script to output the current status of your battery.

### Dependencies
* fonts-font-awesome
* acpi
* python3
* notify-send

### Suggested
* i3 ( >= 4.3 )
* i3blocks ( >= 1.4 )

### Appearance

![](https://raw.githubusercontent.com/p-hash/i3blocks-battery/master/images/1.png)

### Usage
To use with i3blocks, copy the blocklet configuration in the given `i3blocks.conf` into your i3blocks configuration file, the recommended config is

```INI
[battery]
command=$SCRIPT_DIR/battery.py
markup=pango
interval=30
```
