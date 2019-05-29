import sys
per = float(sys.argv[1])

def switch(grade):
    case = {
        'A': 'Excellent',
        'B': 'Very Good',
        'C': 'Good',
        'D': 'Above Average',
        'E': 'Satisfactory'
    }
    return case[grade] 

if per >= 90:
    grade = 'A'
elif per >= 80 and per < 90:
    grade = 'B'
elif per >= 70 and per < 80:
    grade = 'C'
elif per >= 60 and per < 70:
    grade = 'D'
else:
    grade = 'E'

print(switch(grade))
print("Percentage: %.2f, Grade: %s" % (per, grade))



