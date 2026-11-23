from datetime import date, time

######    Data Types in Python     ######


#1. Numeric Types: int, float and complex
# **int : number without decimal point.
# **float : number with decimal points.
# **complex: complex of number with imaginary part
intNumber = 12
floatNumber = 8.34
complexNumber = 2 + 25j

print(f''' int number type: {intNumber} , float number type: {floatNumber} , Complex number type: {complexNumber}  ''')


#2. Sequence Types: collection of elements
# **str: immutable sequences of characters
# **list: a mutable ordered sequence of elements 
# **tuple: an immutable ordered sequence of elements(once created, elements cannoy be changed).
classTitle = "Python Basics"
StudentsNames = ["Ali", "Ahmad","Sara","Raha","Arya","Mahsa","Sita","Mohammad"]
bestStudents = ("Ali","Sara","Sita")

print(f''' str Sequence type:{classTitle},list Sequence type: {StudentsNames} , tuple Sequence type: {bestStudents}  ''')


#3. Set types: collection of unique elements
# **set: mutable collection of elements
# **frozenset: immutable collection of elements

newStudents = {"Sahar", "Arman", "Nila", "Bita"}
onlineStudents = frozenset({"Bahar", "Mahtab", "Sima"})

print(f''' set of set type: {newStudents} , frozenset of set type: {onlineStudents}  ''')

#4. Mapping type: unordered collection of key-value pairs, each key must be unique
# **dict: unordered and mutable collections of map keys to values
# remember this: key must be immutable(str, number or...), but value can be of any data type.

classSpecifications = {"title": classTitle, "presenStudnt": len(StudentsNames)+len(newStudents), "totalStudents": len(StudentsNames)+len(newStudents)+len(onlineStudents),}

print(f"dictionary of Mapping type: {classSpecifications} ")


#5. Boolean type:save logical values,used for conditional codes.
# **bool: just has two values: true, false.

isDuring = True

print(f"boolean type: {isDuring}")


#6. DateTime:used to store date and time. need to import
# **datetime: used for date and time 
# ** date: indicates for date
# **time: indicates for time

startDate = date(2026,10,12).strftime("%Y/%m/%d")

classTimeLine = {
    "start" : time(6,0).strftime("%H:%M"),
    "end" : time(7,0).strftime("%H:%M")
}


print(f'date of Datetime type: {startDate}, time of Datetime type: {classTimeLine["start"]}')


numberOfStudents = [*StudentsNames,*newStudents]


pythonClass = {
    "title": classTitle,
    "start_date": startDate,
    "class_timeline": classTimeLine,
    "isDuring": isDuring,
    "present_students": len(numberOfStudents),
    "total_students": len(numberOfStudents) + len(onlineStudents),
}

print(pythonClass)

