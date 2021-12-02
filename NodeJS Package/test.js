const lol = require('./index')
lol.chatbotsetup('156099', '4TG9iu82pFOu9XjD')
lol.getcreds()
lol.sendmsg('hi', 'test').then((res) => {
  console.log(res) // Print the contest data on the console
})
  .catch((err) => {
    console.log(err) // Error handler
  })
