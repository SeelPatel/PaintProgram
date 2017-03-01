#Python
#Created by Seel Patel

import datetime #module used to get the current date and time

def errorMsg(msg):
    msg = "ERROR: " + str(datetime.datetime.now()) + " : " + msg #create the error msg
    errorFile = open("Extra/errors.txt","a") #open the errors file
    errorFile.write(msg + "\n") #write the error message in the file
    print(msg) #print message to user
    errorFile.close() #close the error file
