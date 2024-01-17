# pylint: disable = R0902
# pylint: disable = R0913
# pylint: disable = R1714
# pylint: disable = C0114
# pylint: disable = E0401

"""
Main File
"""

from datetime import datetime
from itertools import islice
import requests
import pyjokes
from .utils import correction
from .errors import BaseError, ArgumentError

URL = "http://api.brainshop.ai/get"


class ChatBot:
    """Base Chatbot object"""

    def __init__(
        self, brainid="", apikeyuser="", uiiduser="PythonChatbot", history=False, debug=False):
        self.brain = brainid
        self.apikey = apikeyuser
        self.uiid = uiiduser
        self.authorname = "HilFing"
        self.repo_link = "https://github.com/hilfing/ChatbotAPI"
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
        """Get bot credentials"""
        creds = {
            'bid': self.brain,
            'key': self.apikey,
            'uid': self.uiid
        }
        return creds

    def author(self):
        """Get author name"""
        return self.authorname

    def link(self):
        """Get repo_link to github repo"""
        return self.repo_link

    def spellcheck(self, val):
        """Enable or disable spellcheck"""
        if val is not True and val is not False:
            raise ArgumentError("Value must be boolean")
        self.spelling = val
        self.__writelog(["Spellcheck set to " + str(val)], "logs")

    def changename(self, name):
        """Change bot name"""
        if not name == "":
            self.uiid = name
            self.__writelog(
                ["Bot Name Changed.", "New Bot Credentials : " + str(self.getcreds())], "logs")
        else:
            raise ArgumentError("Incorrect argument passed")

    def sendmsg(self, message1):
        """Send message to bot"""
        msg = message1
        if self.spelling is True:
            var = correction(msg)
            if not msg == var:
                print("User input autocorrected")
                self.__writelog(["Input received", "Spell Check done"], "logs")
        self.__writelog(["Input received"], "logs")
        data = ""
        done = 0
        status = 0
        if 'jokes' in msg or 'joke' in msg and done == 0:
            data = "Here is a joke : " + pyjokes.get_joke()
            done = 1
            status = "'Pyjoke'"
        params = {
            'bid': self.brain,
            'key': self.apikey,
            'uid': self.uiid,
            'msg': msg
        }
        if params['bid'] == "" or params['key'] == "" or params['uid'] == "":
            raise BaseError("ChatBot not setup properly!")
        if done == 0:
            response = requests.get(url=URL, params=params, timeout=10)
            data = response.json()['cnt']
            status = response.status_code
            done = 1
        if done == 1:
            self.__writelog(
                ["Reply Received", "Response status_code = " + str(status)], "logs")
            self.__writelog([msg, data], "history")
            return data
        raise BaseError("Internal Error!")

    def __writelog(self, data, logtype):
        """Write to log/history"""
        if logtype == "history" and self.debug['history'] is True:
            self.__debugdata['history']\
                .extend(["User : " + data[0], self.uiid + " : " + data[1]])
        elif logtype == "logs" and self.debug['debug'] is True:
            self.__debugdata['logs']\
                .append("[" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "]")
            for i in data:
                self.__debugdata['logs'].append(i)
            self.__debugdata['logs'].append("")

    def printlogs(self, filename="Chatbot.log"):
        """Print logs to file"""
        if self.debug['debug'] is False:
            raise BaseError("Debug not enabled while creating bot")
        with open(filename, "w+", encoding="utf-8") as log_file:
            for i in self.__debugdata['logs']:
                log_file.write(i)
                log_file.write("\n")
            log_file.close()
        print("Logs written to " + filename)

    def gethistory(self, length="all"):
        """Get history"""
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

    def adddata(self, data: dict):
        """Add custom data to bot. (In production)"""
        return data
