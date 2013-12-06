#shutdown.py
#Get messages, if a message contains "shutdown" command, shut down the system
import sms, os, pickle, re
rules = pickle.load(file("rules.pik"))
message = []
kill = False
sms.login()

bank = re.match("^bank")

while kill == False:
    try:
        while message == []:
            sms.getmessage(message)
        for n in message:
            sms.delete()
            if n 
            os.popen(rules[n])
        message = []
    except KeyboardInterrupt:
        print "Keyboard Interrupt Detected!"
        kill = True
