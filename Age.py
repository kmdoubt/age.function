#this function returns the current age of a birthday
def age(month, day, year):
    
        #----------------------converts months to digits------------------
    if (month == 'february'):
        month = 2
    elif (month == 'march'):
        month = 3
    elif (month == 'april'):
        month = 4
    elif (month == 'may'):
        month = 5
    elif (month == 'june'):
        month = 6
    elif (month == 'july'):
        month = 7
    elif (month == 'august'):
        month = 8
    elif (month == 'september'):
        month = 9
    elif (month == 'october'):
        month = 10
    elif (month == 'november'):
        month = 11
    elif (month == 'december'):
        month2 = 12
    #-------------------------------------------------------------------------------
    
    #-------------------------converts to days, until the date of birth------
    leap_years = (year-1)//4
    y = ((year-1)*365)+leap_years
    if (month == 2):
        y = y + 31
    elif (month == 3):
        if (year%4 == 0):
            y = y + 60
        else:
            y = y + 59
    elif (month == 4):
        if (year%4 == 0):
            y = y + 91
        else:
            y = y + 90  
    elif (month == 5):
        if (year%4 == 0):
            y = y + 121
        else:
            y = y + 120
    elif (month == 6):
        if (year%4 == 0):
            y = y + 151
        else:
           y = y + 151
    elif (month == 7):
        if (year%4 == 0):
            y = y + 183
        else:
            y = y + 182
    elif (month == 8):
        if (year%4 == 0):
            y = y + 213
        else:
            y = y + 212
    elif (month == 9):
        if (year%4 == 0):
            y = y + 244
        else:
            y = y + 243
    elif (month == 10):
        if (year%4 == 0):
            y = y + 274
        else:
            y = y + 273
    elif (month == 11):
        if (year%4 == 0):
            y = y + 305
        else:
            y = y + 304
    elif (month == 12):
        if (year%4 == 0):
            y = y + 335
        else:
            y = y + 334
        
    y = y + day
    
    #-----------------------------------------------
    import datetime
    year2 = datetime.date.today().year
    month2 = datetime.date.today().month
    day2 = datetime.date.today().day
    
    leap_years2 = (year2-1)//4
    z = ((year2-1)*365)+leap_years2
    if (month2 == 2):
        z = z + 31
    elif (month2 == 3):
        if (year2%4 == 0):
            z = z + 60
        else:
            z = z + 59
    elif (month2 == 4):
        if (year2%4 == 0):
            z = z + 91
        else:
            z = z + 90  
    elif (month2 == 5):
        if (year2%4 == 0):
            z = z + 121
        else:
            z = z + 120
    elif (month2 == 6):
        if (year2%4 == 0):
            z = z + 151
        else:
           z = z + 151
    elif (month2 == 7):
        if (year2%4 == 0):
            z = z + 183
        else:
            z = z + 182
    elif (month2 == 8):
        if (year2%4 == 0):
            z = z + 213
        else:
            z = z + 212
    elif (month2 == 9):
        if (year2%4 == 0):
            z = z + 244
        else:
            z = z + 243
    elif (month2 == 10):
        if (year2%4 == 0):
            z = z + 274
        else:
            z = z + 273
    elif (month2 == 11):
        if (year2%4 == 0):
            z = z + 305
        else:
            z = z + 304
    elif (month2 == 12):
        if (year2%4 == 0):
            z = z + 335
        else:
            z = z + 334

    z = z + day2
    

    x = z - y        #--------- x is the number of days lived -------------
    
    old = 0
    leap_days = leap_years - leap_years2

    #-------------------the following converts days-of-life to completed years--------
    if (year2%4 == 0):
        if (month2 == 2):
            if (day2 == 29):
                leap_days = leap_days + 1
        elif (month2 >= 3):
            leap_days = leap_days + 1

    while (leap_days > 0):
        x = x - 366
        old = old + 1
        leap_days = leap_days - 1
        
    while (x >= 365):
        x = x - 365
        old = old + 1

    return(old)





