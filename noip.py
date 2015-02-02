#!/usr/bin/env python

import urllib2
import urllib
from base64 import b64encode

# Let's get the public IP First
publicIp = urllib2.urlopen('http://169.254.169.254/latest/meta-data/public-ipv4').read()


# This is useful too
#opener = urllib2.build_opener()
userAndPass = userAndPass = b64encode(b"gustavoelkhoury@gmail.com:0804noip").decode("ascii")
#print (userAndPass)

data = {}
data['hostname'] = 'gustavoelkhoury.no-ip.org'
data['myip'] = publicIp
encodedData = urllib.urlencode(data)
#print (encodedData)

finalUrl = 'http://dynupdate.no-ip.com/nic/update?' + encodedData
# This way also works
# opener.addheaders = [('Authorization','Basic %s' % userAndPass)]
# result = opener.open(finalUrl)
request = urllib2.Request(finalUrl)
request.add_header("Authorization","Basic %s" % userAndPass)
result = urllib2.urlopen(request)
#print result

