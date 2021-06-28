# BrainshopChatbotAPI  
 An python package to make it easier to connect to the brainshop API and make a working AI chatbot  
 
 #How to use?  
 There are only 2 commands in this package.(more will be added soon)  
 The function structure is `BrainshopChatbotAPI.chatbasics.sendmsg(<text to be sent to the AI>)`.  
 To use it just do  
 ```
 from BrainshopChatbotAPI.chatbasics import sendmsg, chatbotsetup  
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
 
 #How to install it  
 Do `py -m pip install BrainshopChatbotAPI` and you are done.  


 PackageWebsite - [BrainshopChatbotAPI on Pypi](https://pypi.org/project/BrainshopChatbotAPI/)  
 AuthorWebsite - [PaulStudios](https://paulstudios.great-site.net)  
