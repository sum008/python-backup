t=int(input())

while t>=1:
    date = input("Enter in format yyyy:mm:dd  : ")
    date = date.split(":")
    year = int(date[0])
    month = int(date[1])
    day_of_med = int(date[2])
    
    if month==2 :
        if year%4==0:
            if year%4==0:
                if year%100==0:
                    if year%400==0:
                        print((29-day_of_med)//2+1)
        else:
            print((59-day_of_med)//2+1) #28+31(even month so she will not mess up till odd month comes which is 31)
            
    elif(month==4 or month==6 or month==9 or month==11): #30+31(These are even months so she will not mess up alternate days)
        print((61-day_of_med)//2+1)
    else:
        print((31-day_of_med)//2+1) #31(These are odd months so she will mess up on next month)
        
    t-=1    