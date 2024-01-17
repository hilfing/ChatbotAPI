# ChatbotAPI 
An nodejs package to make it easier to connect to the brainshop API and make a working AI chatbot  
 
 # How to install it  
 Do `npm i chatbotapi` and you are done.  
 
 # How to use?  
 There are only 3 commands in this package.(more will be added soon)  
 To use it just do  
 ```
bot = require('chatbotapi')
bot.chatbotsetup("Brain ID", "API Key")
console.log(bot.getcreds()) //Shows the Bot credentials entered with chatbotsetup
bot.sendmsg("Hi")
  .then((res) => {
    console.log(res); // Print the data on the console
  })
  .catch((err) => {
    console.log(err); // Error handler
  }); 
 ```
 1. To get Brain Id and other info go to [BrainShop](https://brainshop.ai)  
 2. Make an account  
 3. Make a brain and don't change any settings  
 4. Go to the settings tab and copy the BrainID and APIkey and then use it  
    PS: To use your own uid just do `sendmsg("message","UID")`  
 5. Voila! It works! Now enjoy your AI chatbot.  
 6. You can find the Logs of this package in a file named `chatbot.log`  
 Thats All  
 
 # Features
 AI Chatbot.  
 Can make interesting conversations.  
 Can do math.  
 Can say jokes.  


 PackageWebsite - [ChatbotAPI on NPM JS](https://www.npmjs.com/package/chatbotapi)  
 AuthorWebsite - [PaulStudios](https://paulstudios.great-site.net)  
