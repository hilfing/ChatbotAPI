
import requests


URL = "http://api.brainshop.ai/get"


brain = "156099"
apikey = "4TG9iu82pFOu9XjD"
uiid = "JarvisAI"
msg = "Hi"


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
