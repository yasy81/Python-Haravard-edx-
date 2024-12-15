#students = ["Harmonie", "Ron", "Harry"]

#1
"""
#indexes
print(students[0])
print(students[1])
print(students[2])
"""
#2
"""
for students in students:
    print(students)
"""
#3
"""
for i in range(len(students)):
    print(i+1 ,students[i])

"""

#dict: a data structure that allows you to associate one value with another.

"""students = {"Harmonie":"Gryffindor",
            "Ron":"Gryffindor", 
            "Harry":"Gryffindor",
            "Draco":"Slytherin"}

print(students["Harmonie"])
print(students["Ron"])
print(students["Harry"])
print(students["Draco"])

#this will just show us the keys.
for student in students:
    print(student)

#this will show the value of the key
for each in students:
    print(each, students[each], sep = ",")"""

#how to store more data

teenwolf = [
    {"ch": "Scott", "identity": "Werewolf", "mother": "Mellisa", "father":None},  #this is a dictionary
    {"ch": "Alisson", "identity": "hunter", "mother": "Victoria", "father":"Cristoff"},
    {"ch": "Stiles", "identity": "Robinhood", "mother": None, "father":"Noah"},
    {"ch": "Lydia", "identity": "Banshee", "mother": "Natalie", "father":"Mr.martin"}
]

for each in teenwolf:
    print(each["ch"], each["identity"],each["mother"],each["father"], sep = ", ")