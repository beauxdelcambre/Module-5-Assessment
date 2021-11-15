log_file = open("um-server-01.txt") #opening the um-server-01.txt file


def sales_reports(log_file):    #a python function 
    for line in log_file:       #looping over the data in the file
        line = line.rstrip()    #
        day = line[0:3]         #specify which index day is at
        if day == "Mon":        #specify which day to print
            print(line)         #printing the results in console      


sales_reports(log_file)         #invoking the function
