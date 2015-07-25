import urllib
import re
from bs4 import BeautifulSoup
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    KGREEN = '\033[92m'
    ARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def getAnum(soup):
    return int(re.search("\((\d+)",str(soup.find(attrs={"id":"ctl00_MainContent_SearchSummary_divSummary"}).span)).group(1))

def getHtml(url):
    print "open url"
    page = urllib.urlopen(url)
    html = page.read()
    print "finish get html"
    return html

def getsoup(url, start, end):
    html = getHtml(url + "&start=" + str(start) + "&end=" + str(end))
    return BeautifulSoup(html)

def getAid(soup):
    result = []
    a = soup.find_all('h3')
    for abuf in a:
        m = re.search("Author\/(\d+)\/", str(abuf))
        result.append(m.group(1))
    return result

def getAllAid(url, maxnum):
    nowstartnum = 1
    nowendnum = 100
    isfirst = 1
    maxAnum = maxnum
    re = []
    while nowstartnum <= maxnum and nowstartnum <= maxAnum:
        print "start " + str(nowstartnum) + "--" + str(nowendnum)
        soup = getsoup(url, nowstartnum, nowendnum)
        if isfirst == 1:
            maxAnum = getAnum(soup)
            print bcolors.OKBLUE + "co-Author num: " + str(maxAnum) + bcolors.ENDC
            isfirst = 0
        re = re + getAid(soup)
        print str(nowstartnum) + "--" + str(nowendnum) + " finish."
        nowstartnum = nowstartnum + 100
        nowendnum += 100

    print bcolors.OKBLUE + "len of re: " + str(len(re)) + bcolors.ENDC
    if maxAnum > 2000:
        maxAnum = 2000
    if len(re) != maxAnum:
        sys.exit(1)
    return re

#can use
def outAllAid():
    url = "http://academic.research.microsoft.com/Detail?query=complex%20networks&searchtype=1&s=0&SearchDomain=2"
    f = open("authors_list", "w");
    re = getAllAid(url, 2000)
    for i in re:
        f.write(i + "\n")
    f.close()


f = open("authors_list", "r");
fl = f.readlines()
l = []
for i in fl:
    l.append(i[:-1])

f.close()

url = "http://academic.research.microsoft.com/Detail?entitytype=2&searchtype=1&id="

f = open("test", "a");

for time in xrange(0, 2000):
    print bcolors.HEADER + "Author num : " + str(time + 1) + bcolors.ENDC
    resu = getAllAid(url + l[time], 2000)
    strbuf = ""
    innum = 0
    for rebuf in resu:
        for i in xrange(2000):
            if l[i] == rebuf:
                strbuf  = str(time) + " " + str(i)
                print "out: " + strbuf
                f.write(strbuf + "\n")
                innum += 1
                break
    print bcolors.KGREEN + "in num: " + str(innum) + bcolors.ENDC




f.close()

#getAllAid(url, 2000)







