#!/usr/bin/env python3
#
# A battery indicator blocklet script for i3blocks

from subprocess import check_output, Popen
import os

def color(percent):
    if percent < 5:
        return "#FFFFFF"
    if percent < 10:
        return "#FF0000"
    if percent < 20:
        return "#FF3300"
    if percent < 30:
        return "#FF6600"
    if percent < 40:
        return "#FF9900"
    if percent < 50:
        return "#FFCC00"
    if percent < 60:
        return "#FFFF00"
    if percent < 70:
        return "#99FF00"
    if percent < 80:
        return "#66FF00"
    return "#33FF00"

status = check_output(['acpi'], universal_newlines=True)
state = status.split(": ")[1].split(", ")[0]
commasplitstatus = status.split(", ")
percentleft = int(commasplitstatus[1].rstrip("%\n"))

FA_CHR = "<span font='FontAwesome'>\uf077</span>"
FA_DIS = "<span font='FontAwesome'>\uf078</span>"
FA_FULL = "<span font='FontAwesome'>\uf139</span>"
FA_LIGHTNING = "<span font='FontAwesome'>\uf0e7</span>"

fulltext = "<span color='yellow'>{}</span>".format(FA_LIGHTNING)
timeleft = state + ", time left:"
time = commasplitstatus[-1].split()[0]
time = ":".join(time.split(":")[0:2])
timeleft += " {}".format(time)

if state == "Discharging":
    form = ' <span color="{}">{}</span>'
    fulltext += form.format(color(percentleft), FA_DIS)
elif state == "Charging":
    fulltext += " " + FA_CHR
else:
    fulltext += " " + FA_FULL

if percentleft != 100:
    fulltext += ' '
if percentleft < 10:
    fulltext += ' '
form =  '<span color="{}">{}%</span>'
fulltext += form.format(color(percentleft), percentleft)

if os.environ.get('BLOCK_BUTTON'):
    Popen(['notify-send', timeleft])

print(fulltext)
print(fulltext)
if percentleft < 5:
    exit(33)
