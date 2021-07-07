import requests


URL = "http://api.brainshop.ai/get"


brain = ""
apikey = ""
uiid = ""
msg = ""

def chatbotsetup(brainid, apikeyuser, uiiduser = "PythonChatbot"):
    global brain
    global apikey
    global uiid
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




                                                                                                                                                                                                                                                               