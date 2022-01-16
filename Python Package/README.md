# ChatbotAPI  
 An python package to make it easier to connect to the brainshop API and make a working AI chatbot  
 
 ## How to install it  
 Do `py -m pip install ChatbotAPI` and you are done.  
 
 ## How to use?  
 There are various commands and utilities in this package.
 To use it just do  
 ```
 from ChatbotAPI.chatbasics import Chatbot
 bot = Chatbot(BrainId, ApiKey, BotName, history, debug)
 data = bot.sendmsg("Hi")  
 print(data)  
 ```
 1. To get Brain Id and other info go to [BrainShop](https://brainshop.ai)  
 2. Make an account  
 3. Make a brain and don't change any settings  
 4. Go to the settings tab and copy the BrainID and APIkey and then use it  
 5. Use boolean for history and debug switch.  
 6. To turn on spellchecker use `bot.spellcheck(True)`  
 7. Voila! It works! Now enjoy your AI chatbot.  
 Thats All  
 
 
 ## Features
 AI Chatbot. Can make interesting conversations.  
 Can do math.  
 Can say jokes.  
 Has history function and debugging with logs.  
 Support multiple bot instances with different settings    

 ## Docs  
[Wiki](https://github.com/hilfing/ChatbotAPI/wiki/Python)  

 PackageWebsite - [ChatbotAPI on Pypi](https://pypi.org/project/ChatbotAPI/)  
 AuthorWebsite - [PaulStudios](https://paulstudios.great-site.net)  
