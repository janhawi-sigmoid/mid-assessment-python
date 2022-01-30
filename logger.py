class Logger:
    def __init__(self):
        self.logs={}

    def shouldPrintMessage(self,timestamp,message):
        if self.logs.__contains__(message):
            if(timestamp - self.logs[message] >=10):
                self.logs[message] = timestamp
                return True
            else:
                return False
        else:
            self.logs[message] = timestamp
        return True

logger = Logger()
log_list=[]

count = int(input("Enter no of logs"))
while count:
    timestamp,message = input("Enter timestamp and message separated by comma").split(",")
    log_list.append(logger.shouldPrintMessage(int(timestamp),message))
    count-=1

print(f"Printing logs : {log_list} \n")