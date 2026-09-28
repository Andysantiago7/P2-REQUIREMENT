def calculate(Act1,Act2,Act3):
    total = Act1 + Act2 + Act3
    avg = total/3
    return avg

number_students = int(input("HOW MANY STUDENTS: "))
print()

for i in range (1,4):
    student_name = input(f"ENTER STUDENT NAME {i}: ")
    print("ENTER NAME: ", student_name)
    
    Act1 = int(input("ENTER ACTIVITY 1 SCORE: "))
    Act2 = int(input("ENTER ACTIVITY 2 SCORE: "))
    Act3 = int(input("ENTER ACTIVITY 3 SCORE: "))
    
    avg = calculate(Act1,Act2,Act3)
    
    if avg >= 90:
        perf = "EXCELLENT!"
    elif avg >= 80:
        perf = "GOOD!"
    elif avg >= 70:
        perf = "PASSED"
    else:
        perf = "FAILED"
        
    print()
    print("AVERAGE:" , avg)
    print("PERFORMANCE:", perf)
    print()