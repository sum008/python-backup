

def get_day(month):
    if month==1:return 31
    elif month == 2 : 
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    return 29
                 
        else: return 28
    elif month == 3 : return 31
    elif month == 4 : return 30
    elif month == 5 : return 31
    elif month == 6 : return 30
    elif month == 7 : return 31
    elif month == 8 : return 31
    elif month == 9 : return 30
    elif month == 10 : return 31
    elif month == 11 : return 30
    elif month == 12 : return 31

t = int(input("Number of test cases : "))

while t>=1:
    
    date = input("Enter in format yyyy:mm:dd  : ")
    date = date.split(":")
    year = int(date[0])
    month = int(date[1])
    day_of_med = int(date[2])
    no_of_days=0
    med_count=0
    
    while True:
        till_day = get_day(month)
        print(till_day)
        cur_day=0
        for i in range(day_of_med, till_day+1 ,2):
            cur_day=i
            med_count+=1
        
        if day_of_med%2==0:
            day_of_med=2
            if month!=12:
                month+=1
            else:
                month=1
            
            if(2+(till_day-cur_day)==2):
                pass
            else:
                break;
        else:
            day_of_med=1
            if month!=12:
                month+=1
            else:
                month=1
            
            if(1+(till_day-cur_day)==2):
                pass
            else:
                break;
            
    print(med_count)
    t-=1       
    
    
    
    
    