from bs4 import BeautifulSoup as soup   ##library to scrape website
import pyttsx  
import time  
from yahoo_finance import Share
import csv,sys
import subprocess
import urllib2
engine=pyttsx.init()
rate = engine.getProperty('rate')  #accessing the rate @ which words are being said
engine.setProperty('rate', rate-80)
LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
time.sleep(1)
#raw_input("Press enter to exit")
def readandSay():
    
    #time.sleep(1)
    f = open('stocklog.csv', 'r')
    reader = csv.reader(f,delimiter=',')
    next(f)
    #f1=open("logfile.txt","a+")
    
        
    for row in reader:
        try:
            f1=open("logfile.txt","a+")
            ##print "hey"
            comp_name= row[0]
            minValue=float(row[1])
            maxValue=float(row[2])
        #print comp_name
        #print minValue
        #print maxValue
            #share_val = Share(comp_name)
            #price=float(share_val.get_price())
            #name=share_val.get_name()
            #print name
            #print type(price)
            #print type(minValue)
            req = urllib2.Request('https://in.finance.yahoo.com/quote/'+comp_name+'?p='+comp_name)
            response = urllib2.urlopen(req)
            the_page = response.read()
            page=soup(the_page,"html.parser")
            price=page.findAll("span",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})[0].string
            price_new=float(price.replace(',',''))
            name=page.findAll("h1",{"class":"D(ib) Fz(18px)"})[0].string
            print name
            print price_new
            print maxValue
            f1.write(name + "\n")
            f1.close()
            if price_new<minValue:
                engine.say(name+ "   Share Value Dropped to ")
                engine.say(price_new)
                engine.runAndWait()
            elif price_new>maxValue:
                engine.say(name+ "   Share Value Increased to" )
                engine.say(price_new)
                engine.runAndWait()
                
        except TypeError:
            print "No Valid Information Available for  " + comp_name
        
        except IndexError:
            print "No Valid Information Available for  " + comp_name
            #time.sleep(2)
        except IOError:
            print "Spelling mistake,Must have used some extra space ,Check It"
    #f1.close()
    
while True:
  
     readandSay()

