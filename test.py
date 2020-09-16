slots = []
teacherlist = ['Mr.Walter','Mr.Jeff','Ms.Gary','Ms.Onion']
Students = {'Will':'Mr.Walter,Ms.Gary','Bob':'Mr.Jeff,Ms.Onion'}
StartTime = 7
EndTIme = 8.5
TotalSlots = int((EndTIme - StartTime)*12)
print(TotalSlots)

def createSlot(teacher,student):
    slots.append((teacher+" : "+student))

for i in range(TotalSlots):
    slots.append('NEW SLOT')
    for teacher in teacherlist:
        verified = False
        while verified == False:
            for student in Students.keys():
                if teacher in Students[student]:
                    print('VERIFIED')
                    createSlot(teacher,student)
                    verified = True

print(slots)

print(Students.values())
print(Students.keys())
print(Students['Will'])