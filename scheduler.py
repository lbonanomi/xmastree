#!/bin/python

"""xmastree scheduler. Stick me into cron 1 minute before your job starts"""

import json
import time
import os
import sys
from datetime import datetime, timedelta


my_date = datetime.now() + timedelta(minutes=1)                           # Not
holder = str(my_date).split('.')[0].split(':')                            # proud
better = holder[0] + ':' + holder[1]                                      # of 
                                                                          # this
start_time = int(time.mktime(time.strptime(better, '%Y-%m-%d %H:%M')))    # at 
stop_time  = int(start_time + 61)                                         # all.
                                      
this_instance_rotation_number = 1	# Actually harvest this from hostname
maximum_rotations = 3

# Load JSON data into memory
#

pipe = {}
actioned = []

file = sys.argv.pop()

print "Crunching " + file

with open(file) as xmastree_data:
	xmastree_json = json.load(xmastree_data)

for timestamp in xmastree_json:
	for commands in xmastree_json[timestamp]:

		if int(timestamp) >= int(start_time):

			if int(timestamp) <= int(stop_time):
				pipe[timestamp] = xmastree_json[timestamp][commands]


# For the next 75 seconds: 
# 	every .1 seconds get the time
#	If the integer time now is the start time:
#		execute associated commands
#		pop that command off the pipe


print "It is now " + str(int(time.time())) + ". I start at " + str(start_time) + ". I will run for 75 seconds on rotator " + str(this_instance_rotation_number)

now = time.time()

while now <= stop_time:
	time.sleep(1/10.0)
	now = int(time.time())

	for key, value in pipe.iteritems():
		if int(key) == int(now) and key not in actioned:
				actioned.append(key)

				rotator = 0

				for command in value:
					rotator += 1

					if rotator > maximum_rotations:
						rotator = 0

					if rotator == this_instance_rotation_number:
						print "This command is 1/" + str(maximum_rotations) + " of traffic for " + str(time.time())

						pid = os.fork()

						if pid == 0:
							os.system(command)
							print "PID " + str(os.getpid()) + " RUNS " + str(command) + " AT " + str(now) + " FOR TIMESTAMP " + str(time.time())
							os._exit(0)  

