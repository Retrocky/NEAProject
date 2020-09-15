# importing packages
from pulp import *
import pandas as pd
slots = []

def createSlot(teacher,student):
    slots.append((teacher+" : "+student))


# formatting csv data for the parent timings into a manipulable form with pandas
parent_timings_csv = 'NEAdata.csv'
parent_timings = pd.read_csv(parent_timings_csv)
print(parent_timings)
parent_timings.reset_index(inplace=True)
# The number of appointemnts available per time-slot
numofteachers = 25
# The number of time slots in the evening e.g(7:00,7:05 = 2, 12 slots in an hour)
numoftimeslots = 48
# The total number of meetings that will take place throughout the evening is numofteachers * numoftimeslots

# setting up optimisation problem - registered as a maximisation problem
problem = LpProblem('parents_evening', sense=LpMaximize)
print(problem)

# LOOPING THROUGH EACH TIME SLOT
for i in range(numoftimeslots):
    print("SLOT",i)
    # Making sure the slots generate the correct subject choices

    # Making sure each time slot has less than or the same as the max number of appointments per time slot
    maxappointments = LpVariable('appointments', lowBound=0, upBound=5, cat='Integer')
    maxavailableappointments = numofteachers
    problem += (maxappointments == maxavailableappointments)

    for j in range(numofteachers):
        print("Slot",i,"Appointment",j)
        createSlot('Mr.Will','Will')
        print(slots)
    # Making sure there are no clashes


print(LpStatus[problem.status])

'''
# setting up decision variables
decision_variables = []
for rownum, row in parent_timings.iterrows():
    variable = str('x' + str(row['index']))
    variable = pulp.LpVariable(str(variable), lowBound=0, upBound=1, cat='Integer')
    decision_variables.append(variable)

print('Num of decision vars: ' + str(len(decision_variables)))
'''