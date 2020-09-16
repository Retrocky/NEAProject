slots = []
teacherlist = ['Mr.Walter','Mr.Jeff','Ms.Gary','Ms.Onion']
Students = {'Will':'Mr.Walter,Ms.Gary','Bob':'Mr.Jeff,Ms.Onion'}
StartTime = 7
EndTIme = 8.5
TotalSlots = int((EndTIme - StartTime)*12)
print(TotalSlots)

# Outputs slots
def outputSlots():
    print('='*100)
    for item in slots:
        if 'Slot :' in item:
            print("")
            print(item)
        else:
            print(item)
    print('='*100)

# Creates slots
def createSlot(teacher,student):
    slots.append((teacher+" : "+student))

# Loops through each slot with each teacher and matches students to their teachers needed
def slotSorter(TotalSlots,teacherlist,Students):
    for i in range(TotalSlots):
        slots.append('Slot :'+str(i))
        for teacher in teacherlist:
            verified = False
            while verified == False:
                for student in Students.keys():
                    if teacher in Students[student]:
                        createSlot(teacher,student)
                        verified = True

slotSorter(TotalSlots,teacherlist,Students)
outputSlots()
print(Students.values())
print(Students.keys())
print(Students['Will'])