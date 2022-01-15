import requests
import pyjokes
from datetime import datetime
import errors

URL = "http://api.brainshop.ai/get"


class ChatBot:

    def __init__(self, brainid="", apikeyuser="", uiiduser="PythonChatbot", history=False, debug=False):
        self.brain = brainid
        self.apikey = apikeyuser
        self.uiid = uiiduser
        self.debug = {
            'debug': debug,
            'history': history
        }
        if history:
            self.debugdata = {
                'history': [
                ],
                'logs': [
                ]
            }
        self.__writelog(["Bot Initialised", "Bot Credentials : " + str(self.getcreds())],"logs")

    def getcreds(self):
        creds = {
            'bid': self.brain,
            'key': self.apikey,
            'uid': self.uiid
        }
        return creds

    def sendmsg(self, message1):
        msg = message1
        self.__writelog(["Input received"], "logs")
        data = ""
        done = 0
        if 'jokes' in msg or 'joke' in msg and done == 0:
            data = "Here is a joke : " + pyjokes.get_joke()
            done = 1
        params = {
            'bid': self.brain,
            'key': self.apikey,
            'uid': self.uiid,
            'msg': msg
        }
        if params['bid'] == "" or params['key'] == "" or params['uid'] == "":
            raise errors.BaseError("ChatBot not setup properly!")
        elif done == 0:
            data = requests.get(url=URL, params=params).json()['cnt']
            done = 1
        if done == 1:
            self.__writelog(["Reply Received"], "logs")
            self.__writelog([msg, data], "history")
            return data
        else:
            raise errors.BaseError("Internal Error!")

    def __writelog(self, data, logtype):
        if logtype == "history" and self.debug['history'] is True:
            self.debugdata['history'].extend(["User : " + data[0], "Bot : " + data[1]])
        elif logtype == "logs" and self.debug['debug'] is True:
            self.debugdata['logs'].append("[" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "]")
            for i in data:
                self.debugdata['logs'].append(i)

    def printlogs(self, filename="Chatbot.log"):
        f = open(filename, "w+")
        for i in self.debugdata['logs']:
            print(i)
            f.write(i)
            f.write("\n")
        f.close()

bot = ChatBot("156099", "4TG9iu82pFOu9XjD","Test", True, True)
