import re

def get_host(url):
    urlparts = url.split('://')
    if len(urlparts)>1:
        pat = re.compile('[/?]')
        urlparts = pat.split(urlparts[1])
        host = urlparts[0]
        return host
    return ''

