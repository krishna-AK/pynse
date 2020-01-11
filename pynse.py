import webdriver as nsewd
import re


INDEX_TABLE = None
DRIVER = None

def initialize(headless = True):
    global DRIVER

    if DRIVER == None:
        DRIVER = nsewd.getWebDriver(headless)



def connectToIndexFeed(time_out = 3):
    global DRIVER,INDEX_TABLE
    url = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/live_index_watch.htm'
    tag = 'tbody'
    nsewd.loadPage(DRIVER, url,time_out)
    content = ''
    try:
         INDEX_TABLE = nsewd.findTargetELement(DRIVER, ttag=tag)
         print(':: Connected to IndexFeed!')
    except:
        releaseResources()
        quit()



def getIndicesTable(time_out = 10):
    global INDEX_TABLE
    tab = {'FORMAT' : ('CURRENT','%CHANGE','OPEN','HIGH','LOW','PREV.CLOSE','52W HIGH','52W LOW')}
    # print(INDEX_TABLE)
    index_E = '\s?\n?([A-Z]+[A-Z, ]*[A-Z, ,0-9]*)\s+(\-*\d+\,*\d*\.\d+)\s+(\-*\d+\,*\d*\.' \
              '\d+)\s+(\-*\d+\,*\d*\.\d+)\s+(\-*\d+\,*\d*\.\d+)\s+(\-*\d+\,*\d*\.\d+)\s+(\-' \
              '*\d+\,*\d*\.\d+)\s+(\-*\d+\,*\d*\.\d+)\s+(\-*\d+\,*\d*\.\d+)\s+'

    content = INDEX_TABLE.text
    r = re.compile(index_E)
    t = r.findall(content)
    if t == None:
        releaseResources()
        print('EROOR :: NULL OBJECT RETURNED!')
        quit()
    # print(t)
    for i in t:
        tab[i[0]] = i[1:9]
    # print(tab)
    return tab


def releaseResources():
    global DRIVER
    nsewd.terminate(DRIVER)

