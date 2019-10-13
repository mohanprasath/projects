'''
Author: Mohan Prasath Chinnasamy
Date: September 14 2019
'''

import os
import datetime, time

class TasksTracker:

    def __init__(self, csv_file_path=None):

        if csv_file_path is not None and os.path.isfile(csv_file_path) :
            self.csv_file_path = csv_file_path
        else:
            self.csv_file_path = os.getcwd() + "/tasks_tracker.csv"
            if not os.path.isfile(self.csv_file_path):
                self.add_tasks_to_csv("DateTime;TasksDone")

    def add_tasks_to_csv(self, data_to_add):
        '''
        ToDo: efficient csv writing in python
        '''
        with open(self.csv_file_path, 'a') as outfile:
            outfile.write(data_to_add)

def main():
    my_tasks_tracker = TasksTracker()
    # Program Starts here
    user_choice = input("Choose (1) ADD_TASK (2) END_PROGRAM :\n")
    while user_choice != 2:
        try:
            user_task_detail = \
            input("Please neter the task you want to do for next 30 min:\n")
            current_time = datetime.datetime.now()
            self.add_tasks_to_csv(";".join([str(current_time), \
                user_task_detail]))
        except: 
            break
        user_choice = int(input("Choose (1) ADD_TASK (2) END_PROGRAM :\n"))
    print("PROGRAM ENDED. GOOD BYE!")


if __name__ == "__main__":
    main()

