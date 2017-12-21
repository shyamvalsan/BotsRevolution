#!/usr/bin/python
import os
import sys
import csv
import datetime
import time
import twitter
 
def test():
 
        #run speedtest-cli
        a = os.popen("python /usr/bin/speedtest-cli --simple").read()
        #split the 3 line result (ping,down,up)
        lines = a.split('\n')
        print(a)
        ts = time.time()
        date =datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #if speedtest could not connect set the speeds to 0
        if "Cannot" in a:
                p = 100
                d = 0
                u = 0
        #extract the values for ping down and up values
        else:
                p = lines[0][6:11]
                d = lines[1][10:14]
                u = lines[2][8:12]
        print(date,p, d, u)
        #save the data to file for local network plotting
        out_file = open('/home/pi/Development/airtelTwitterBot/data.csv', 'a')
        writer = csv.writer(out_file)
        writer.writerow((ts*1000,p,d,u))
        out_file.close()
 
        #connect to twitter
        TOKEN="701082337010782208-CA1OzhU2i56cIDktfeRKGLaBIoNu4iM"
        TOKEN_KEY="134zUQ3LQb4xvXleGQPaVhKTukwx5iHZDOPZReFWZsgpz"
        CON_SEC="lZSHGYI8i7bAuTMK1lsy0fQoO"
        CON_SEC_KEY="NGMzDbWs2Zkk5nOnZcJ8JjUXc397GbSmHYH1ib1VjYNQB9h4uu"
 
        my_auth = twitter.OAuth(TOKEN,TOKEN_KEY,CON_SEC,CON_SEC_KEY)
        twit = twitter.Twitter(auth=my_auth)
 
        #try to tweet if speedtest couldnt even connet. Probably wont work if the internet is down
        if "Cannot" in a:
                try:
                        tweet="Hey @Airtel_Presence why is my internet down? #WhyAirtel"
                        twit.statuses.update(status=tweet)
                except:
                        pass
 
        # tweet if down speed is less than whatever I set
        elif eval(d)<8:
                print("trying to tweet")
                try:
                        # i know there must be a better way than to do (str(int(eval())))
                        tweet="Hey @Airtel_Presence why is my internet speed " + str(int(eval(d))) + " Mbps "  + "when I pay for 16 Mbps? #WhyAirtel"
                        twit.statuses.update(status=tweet)
                except:
                        pass
        return
       
if __name__ == '__main__':
        test()
        print("completed")
