#! python3
# Base code for AtBS Projects

import os, time

os.chdir('C:\\Users\\182195\\OneDrive - Tokyo Electron Limited\\Network Info\\PyScripts\\Automate_the_Boring_Stuff_onlinematerials')

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit')
input()						# press Enter to begin
print('Started.')
startTime = time.time()		# get the first lap's start time
lastTime = startTime
lapNum = 1

# TODO: Start tracking the lap times.
