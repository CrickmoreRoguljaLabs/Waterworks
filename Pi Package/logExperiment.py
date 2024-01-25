import picamera
import os
import datetime
import argparse
import shutil

class Experiment(object):
	# This creates an "Experiment" object and tracks everything about the experiment in a .log file
	def __init__(self, video_name=str(datetime.datetime.now())):
		# name the file
		self.name_of_video = video_name
		# put it in the proper directory
		today = datetime.date.today()
		date = "%s-%s-%s" %(today.year, today.month, today.day)
		directory = "/home/pi/log/%s" %(date)
		self.log_dir = directory
		name_of_log = "%s/%s.xpt" %(directory,self.name_of_video)
		if not os.path.exists(directory):
			os.makedirs(directory)
			print("made directory %s" %directory)
		self.name_of_log = name_of_log
		log_file = open(self.name_of_log,"r+")
		log_file.write()

	def change_name(self,name):
		# changes the name of the log file
		shutil.copyfile(self.name_of_log, "%s/%s"(self.log_dir, name))

	def note_change(self, command):
		# easy access to the experiment's log
		# enter the time, then enter the command
		log_file = open(self.name_of_log,"a")
		time_of_command = str(datetime.datetime.now())
		log_file.write("%s:\t %s" (time_of_command,command))
		log_file.close()