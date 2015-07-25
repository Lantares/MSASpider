import urllib
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    KGREEN = '\033[92m'
    ARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getHtml(url):
    print "open url"
    page = urllib.urlopen(url)
    html = page.read()
    print "finish get html"
    return html

url = "http://academic.research.microsoft.com/Author/"

f = open("authors_list", "r");
l = f.readlines()
f.close()

f = open("author_name", "a")

for num in xrange(839, 2000):
    soup = BeautifulSoup(getHtml(url+l[num][:-1]))

    strbuf =str(num) + " " + l[num][:-1]  + " " + soup.find(attrs={"id":"ctl00_MainContent_SearchSummary_divSummary"}).span.get_text()
    print  bcolors.KGREEN + "out: " + strbuf  + bcolors.ENDC
    f.write(strbuf + "\n")

f.close()




