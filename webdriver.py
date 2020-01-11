from selenium import webdriver
import time
from fake_useragent import UserAgent


DPATH = 'chromedriver.exe'



def getWebDriver(headless = True):
    print(':: Starting WebDriver.............')
    fakeUserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    options = webdriver.ChromeOptions()

    if(headless):
        options.add_argument("--headless")
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument('--lang=en_US')
    # options.add_argument('user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36')
    driver = webdriver.Chrome(DPATH,options = options)

    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": UserAgent().random})
    print(':: WebDriver STARTED!')

    return driver

def loadPage(dr,url,TO = 3):
    print(':: Loading NSE Page.................')
    dr.set_page_load_timeout(TO)
    try:
        dr.get(url)
    except:
        pass
    print(':: Page LOADED!')
    print('user-agent :',dr.execute_script('return navigator.userAgent'))

def findTargetELement(dr,tid = '',tclass = '',ttag = '',timeout = 2):
    start = time.time()
    while time.time()-start < timeout:
        try:
            # return dr.find_element_by_id(tid)
            return dr.find_element_by_tag_name(ttag)
        except:
            pass

    print('ERROR::Target NOT FOUND!')
    dr.find_element_by_tag_name(ttag)




def terminate(dr):

    dr.quit()
    print()
    print("FINISH :: WEBDRIVER TERMINATED!")






