import socket
import sys
import urllib2
import urllib
from time import *
from string import *


#PORT = int(xbmcaddon.Addon.getSetting('port'))
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(None)
s.bind(("", PORT))
while 1:
    global data
    data, addr = s.recvfrom(1024)
    #print (data)
    data = split(data, ":")
    if data[0] == "<7> [SLIC] CID to deliver":
        data = split(data[1], "'")
        if data[1] != "(null)":
            name = data[1]
            number = data[2].strip(' \n\x00')
            values = {}
            values['request'] = '{"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Call from '+name+'","message":"'+number+'","displaytime":15000,"image":"/home/username/phone.png"},"id":1}'
            fullurl = 'http://192.168.1.99/jsonrpc?' + urllib.urlencode(values)
            r = urllib2.urlopen(fullurl)
            r = urllib2.urlopen('http://localhost/jsonrpc?' + urllib.urlencode(values))
            print ('Call from ' + name + ' and ' + number)
            # values = {'request': '{"jsonrpc":"2.0","method":"GUI.ShowNotification","params":{"title":"Call from '+name+'","message":"'+number+' calling extension","displaytime":15000,"image":"/home/username/phone.png"},"id":1}'}
            # r = requests.get("http://localhost/jsonrpc", params=payload)


s.close()
sys.exit()