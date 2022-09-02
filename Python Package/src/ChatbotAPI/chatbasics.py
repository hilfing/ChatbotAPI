import requests
import pyjokes
from datetime import datetime
from itertools import islice
from .utils import correction
from .errors import BaseError, ArgumentError

URL = "http://api.brainshop.ai/get"


class ChatBot:

    def __init__(self, brainid="", apikeyuser="", uiiduser="PythonChatbot", history=False, debug=False):
        self.brain = brainid
        self.apikey = apikeyuser
        self.uiid = uiiduser
        self.authorname = "HilFing"
        self.link = "https://github.com/hilfing/ChatbotAPI"
        self.spelling = False
        self.debug = {
            'debug': debug,
            'history': history
        }
        self.__debugdata = {
            'history': [
            ],
            'logs': [
            ]
        }
        self.customdata = []
        self.__writelog(["Bot Initialised", "Bot Credentials : " + str(self.getcreds())], "logs")

    def getcreds(self):
        creds = {
            'bid': self.brain,
            'key': self.apikey,
            'uid': self.uiid
        }
        return creds

    def author(self):
        return self.authorname

    def link(self):
        return self.link

    def spellcheck(self, val):
        if val is not True or val is not False:
            raise ArgumentError("Value must be boolean")
        self.spelling = val

    def changename(self, name):
        if not name == "":
            self.uiid = name
            self.__writelog(["Bot Name Changed.", "New Bot Credentials : " + str(self.getcreds())], "logs")
        else:
            raise ArgumentError("Incorrect argument passed")

    def sendmsg(self, message1):
        msg = message1
        if self.spelling is True:
            x = correction(msg)
            if not msg == x:
                print("User input autocorrected")
                self.__writelog(["Input received", "Spell Check done"], "logs")
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
            raise BaseError("ChatBot not setup properly!")
        elif done == 0:
            r = requests.get(url=URL, params=params)
            data = r.json()['cnt']
            done = 1
        if done == 1:
            self.__writelog(["Reply Received", "Response status_code = " + str(r.status_code)], "logs")
            self.__writelog([msg, data], "history")
            return data
        else:
            raise BaseError("Internal Error!")

    def __writelog(self, data, logtype):
        if logtype == "history" and self.debug['history'] is True:
            self.__debugdata['history'].extend(["User : " + data[0], self.uiid + " : " + data[1]])
        elif logtype == "logs" and self.debug['debug'] is True:
            self.__debugdata['logs'].append("[" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "]")
            for i in data:
                self.__debugdata['logs'].append(i)
            self.__debugdata['logs'].append("")

    def printlogs(self, filename="Chatbot.log"):
        if self.debug['debug'] is False:
            raise BaseError("Debug not enabled while creating bot")
        f = open(filename, "w+")
        for i in self.__debugdata['logs']:
            f.write(i)
            f.write("\n")
        f.close()
        print("Logs written to " + filename)

    def gethistory(self, length="all"):
        if self.debug['history'] is False:
            raise BaseError("History has not been enabled while creating bot")
        his_len = len(self.__debugdata['history'])
        if length == "all" or length == 0:
            length = his_len
        if length > his_len or not length % 2 == 0:
            raise ArgumentError("Length argument is not even or larger than history length.")
        his = self.__debugdata['history']
        data = iter(his)
        split = [his_len - length, length]
        output = [list(islice(data, elem))
                  for elem in split]
        output[1].insert(0, "Here is your History:")
        return output[1]

    def adddata(self, input, output):
        return
        # TODO add code


print("ChatBotAPI by HilFing initialised.\nThank you for using this library.\n\n")
