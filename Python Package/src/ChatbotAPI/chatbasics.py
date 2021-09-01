import requests
import pyjokes

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
    
def getcreds():
    creds = {
        'bid': brain,
        'key': apikey,
        'uid': uiid,
    }
    return creds

def sendmsg(message1):
    msg = message1
    if 'jokes' in msg or 'joke' in msg :
        data = "Here is a joke : " + pyjokes.get_joke()
        return data
    PARAMS = {
        'bid': brain,
        'key': apikey,
        'uid': uiid,
        'msg': msg
    }
    data = requests.get(url=URL, params=PARAMS).json()['cnt']
    
    return data


                                                                                                                                                                                                                                                              
