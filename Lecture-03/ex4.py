hours=float(input("Enter the number of hours worked:"))
rate=float(input("Enter the hourly pay rate: "))
if hours<=40:
    print("The gross pay is",hours*rate)
elif hours>40:
    print("The gross pay is",(hours-40)*(b*1.5)+(40*rate))