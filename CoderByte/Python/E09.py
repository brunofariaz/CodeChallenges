# Challenge
# Have the function TimeConvert(num) take the num parameter being passed and return the number of hours and minutes the parameter converts to 
# (ie. if num = 63 then the output should be 1:3). Separate the number of hours and minutes with a colon. 

def TimeConvert(num): 

    hours = num//60
    minutes = num % 60

    timeConverted = str(hours) + ":" + str(minutes)
    #return ':'.join([str(hours), str(minutes)]) - Join could also be a good idea here
    # code goes here 
    return timeConverted
    
# keep this function call here  
num = 126
print (TimeConvert(num))  