'''
Author: Mohan Prasath Chinnasamy
Date: September 14 2019
'''

import os

class TasksTracker:

	def __init__(self, csv_file_path):

		if os.path.isfile(fname) :
			self.csv_file_path = csv_file_path
		else:
			self.csv_file_path = os.getcwd() + "/tasks_tracker.csv"