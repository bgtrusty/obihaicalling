import socket, threading, thread, sys, asyncore , xbmc, xbmcgui, xbmcaddon
import urllib2
import urllib
from time import *
from string import *

print("[Obihai Calling] Startup up")
settings = xbmcaddon.Addon()
PORT = int(settings.getSetting('port'))
#PORT = 8888

# See if name and number match
# grab number
# go to https://api.opencnam.com/v2/phone/+16502530000
# Return results

while not xbmc.abortRequested:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(None)
        s.bind(("", PORT))
        print("[Obihai Calling] Connected to port " + str(PORT))
    except:
        print("[Obihai Calling] Failed to connect to port "+ str(PORT))
        s.close()
        sys.exit()
    while 1 and not xbmc.abortRequested:
        global data
        data, addr = s.recvfrom(1024)
        data = split(data, ":")
        if data[0] == "<7> [SLIC] CID to deliver":
            data = split(data[1], "'")
            if data[1] != "(null)":
                name = data[1]
                number = data[2].strip(' \n\x00')
                values = {}
                values['request'] = '{"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Call from '+name+'","message":"'+number+'","displaytime":15000,"image":"/home/username/phone.png"},"id":1}'
                fullurl = 'http://localhost/jsonrpc?' + urllib.urlencode(values)
                xbmc.executebuiltin("XBMC.Notification("+name+","+number+",7000,special://home/addons/script.obihailog/phone.png)")
                print("[Obihai Calling] Call from "+name+".  Telephone number:"+number)
            else:
                print("[Obihai Calling] Phone off hook")

s.close()
print("[Obihai Calling] Shutting down")
sys.exit()