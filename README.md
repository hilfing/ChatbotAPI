# ChatbotAPI  
 An python package to make it easier to connect to the brainshop API and make a working AI chatbot  
 
 # How to install it  
 Do `py -m pip install ChatbotAPI` and you are done.  
 
 # How to use?  
 There are only 2 commands in this package.(more will be added soon)  
 To use it just do  
 ```
 from ChatbotAPI.chatbasics import sendmsg, chatbotsetup  
 chatbotsetup("Brain ID","API Key")  
 data = sendmsg("HI")  
 print(data)  
 ```
 1. To get Brain Id and other info go to [BrainShop](https://brainshop.ai)  
 2. Make an account  
 3. Make a brain and don't change any settings  
 4. Go to the settings tab and copy the BrainID and APIkey and then use it  
    PS: To use your own uid just do `chatbotsetup("Brain ID","API Key","UID")`  
 5. Voila! It works! Now enjoy your AI chatbot.  
 Thats All  
 
 # Features
 AI Chatbot. Can make interesting conversations.  
 Can do math.  
 Can say jokes.  


 PackageWebsite - [BrainshopChatbotAPI on Pypi](https://pypi.org/project/BrainshopChatbotAPI/)  
 AuthorWebsite - [PaulStudios](https://paulstudios.great-site.net)  
