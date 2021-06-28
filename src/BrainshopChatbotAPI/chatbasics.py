import requests


URL = "http://api.brainshop.ai/get"


brain = ""
apikey = ""
uiid = ""
msg = ""

def setup(brainid, apikeyuser, uiiduser):
    brain = brainid
    apikey = apikeyuser
    uiid = uiiduser

def sendmsg(message1):
    msg = message1
    PARAMS = {
        'bid': brain,
        'key': apikey,
        'uid': uiid,
        'msg': msg
    }
    data = requests.get(url=URL, params=PARAMS).json()['cnt']
    return data
