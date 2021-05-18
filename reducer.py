import sys
def Repeating(a,n):
    max_num=max(a)
    a=sort(a)
    max=[]
    min=[]
    count=1
    current=a[0]
    maxOccured=a[0]
    maxcount=0
    for i in range(1,n):
        if current==a[i]:
            count+=1
        else:
            if count>maxcount:
                maxcount=count
                maxoccured=current
                max.append(maxoccured)
            elif count == maxcount:
                maxoccured=current
                max.append(maxoccured)
            if count==1:
                min.append(current)
            current=a[i]
            count=1
    return max,maxcount,min
occurrences=[]
number=[]
for line in sys.stdin:
    if line != "":
        number, occurrence = line.split()
        number = int(number)
        numbers.append(number)
max_occurred_numbers, max_occurrences, min_occurred_numbers = Repeating(numbers, len(numbers))
print("Max occurred numbers: ", max_occurred_numbers, " with ", max_occurrences, " occurrences")
min_occurrences = 1     
print("Min occurred numbers: ", sorted(min_occurred_numbers, key=str), " with ", min_occurrences, " occurrences")
                
        
