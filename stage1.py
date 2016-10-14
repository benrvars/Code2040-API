# stage1.py
# Ben Rodriquez-Vars

from json import dumps, loads
from urllib2 import urlopen, Request

info = {'token':'ee9e0acbc941dbb77897706eb67008c7'}

token = dumps(info)

req = Request('http://challenge.code2040.org/api/getstring', token)

string = loads(urlopen(req).read())['result']

print "string: " + string

revString = string[::-1]

print "revString: " + revString

send = {'token':'ee9e0acbc941dbb77897706eb67008c7', 'string':revString}

res = Request('http://challenge.code2040.org/api/validatestring', data=dumps(send)) 

final = loads(urlopen(res).read())['result']

print final
