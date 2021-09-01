lol = require('./index')
lol.chatbotsetup("156099", "4TG9iu82pFOu9XjD")
lol.sendmsg("hi","test").then((res) => {
    // If the function successfully retrieves the data, it enters this block
    console.log(res); // Print the contest data on the console
  })
  .catch((err) => {
    console.log(err); // Error handler
  });
