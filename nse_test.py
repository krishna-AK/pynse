import pynse as nse


nse.initialize()                        #   use nse.initialize(headless = False) for debugging
nse.connectToIndexFeed(time_out= 10)     #   increase timeout for poor connections

x = nse.getIndicesTable()
print('FORMAT :: ',x['FORMAT'])         #   use url
                                        #   https://www1.nseindia.com/live_market/dynaContent/live_watch/live_index_watch.htm
                                         #   for Reference
print('NIFTY 50 :: ',x['NIFTY 50'])
print('NIFTY FMCG :: ',x['NIFTY PVT BANK'])

nse.releaseResources()                  #   clear all created processes



