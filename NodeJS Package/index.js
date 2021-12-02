const axios = require('axios')
const Joke = require('one-liner-joke')
const wiki = require('wikipedia')
const fs = require('fs')
const EventEmitter = require('events')
const errors = require('./error')
const event = new EventEmitter()
const brainshopurl = 'http://api.brainshop.ai/get'
async function clearlogfile () {
  fs.writeFile('chatbot.log', 'ChatBotAPI Logs :-\n\n', (err) => {
    if (err) {
      console.log(err)
    }
  })
}
clearlogfile()
let bid = 'undefined'
let apikey = 'undefined'
const jokefilter = { exclude_tags: ['dirty', 'racist', 'marriage', 'sex'] }
const writelog = function (call, input = '', output = '') {
  output = 'User : ' + input + ' | Bot : ' + output
  if (call === 'getcreds') {
    const as = 'Brain ID : ' + bid + ' | APIKey : ' + apikey
    fs.appendFile('chatbot.log', "Event : The 'getcreds' function was called. \nOutPut : " + as + '\n-----------------------------------------------------------------\n', (err) => {
      if (err) {
        console.log(err)
      }
    })
  }
  if (call === 'sendmsg') {
    fs.appendFile('chatbot.log', "Event : The 'sendmsg' function was called. \nOutPut : " + output + '\n-----------------------------------------------------------------\n', (err) => {
      if (err) {
        console.log(err)
      }
    })
  }
  if (call === 'chatbotsetup') {
    fs.appendFile('chatbot.log', "Event : The 'chatbotsetup' function was called. \nOutPut : Chatbot Credentials Set!" + '\n-----------------------------------------------------------------\n', (err) => {
      if (err) {
        console.log(err)
      }
    })
  }
  if (call === 'logs') {
    fs.appendFile('chatbot.log', "Event : The 'logs' function was called." + '\n-----------------------------------------------------------------\n', (err) => {
      if (err) {
        console.log(err)
      }
    })
  }
}
const getcreds = function (setup = false) {
  const as = 'Brain ID : ' + bid + ' \nAPIKey : ' + apikey
  event.emit('getcreds')
  if (setup === false) {
    writelog('getcreds')
  }
  return as
}
function capfirst (string) {
  return string.charAt(0).toUpperCase() + string.slice(1)
}
const sendmsg = async function (message, uiid = 'ChatBot') {
  try {
    event.emit('sendmsg')
    message = message.toLowerCase()
    if (message === '' || message == null) {
      throw new errors.NoMessagePassed()
    }
    if (message.includes('joke')) {
      const as = Joke.getRandomJoke(jokefilter).body
      writelog('sendmsg', message, as)
      return as
    }
    if (message.includes('wikipedia')) {
      (async () => {
        try {
          message = message.replace('wikipedia', '')
          message = capfirst(message)
          const page = await wiki.page(message)
          const summary = await page.summary()
          const result = 'According to Wikipedia: \n' + summary
          writelog('sendmsg', message, result)
          return result
        } catch (error) {
          console.log(error)
          return error
        }
      })()
    }
    const params = {
      bid: bid,
      key: apikey,
      uid: uiid,
      msg: message
    }
    const response = await axios.get(brainshopurl, { params })
    writelog('sendmsg', message, response.data.cnt)
    return response.data.cnt
  } catch (error) {
    console.error(error)
    return error
  }
}
const chatbotsetup = function (brain, api) {
  event.emit('chatbotsetup')
  if (brain === '' || brain == null) {
    throw new errors.EssentialArgumentMissing('Brain ID is required!')
  }
  if (api === '' || api == null) {
    throw new errors.EssentialArgumentMissing('API Key is required!')
  }
  bid = brain
  apikey = api
  console.log('Chatbot Credentials Set!')
  console.log(getcreds(true))
  writelog('chatbotsetup')
}
// WIP
const logs = function (pass) {
  if (pass !== 'asdfg') {
    return
  }
  fs.readFile('chatbot.log', 'utf8', (err, data) => {
    if (err) {
      console.log(err)
      return err
    }
    writelog('logs')
    return data.toString()
  })
}

module.exports = { chatbotsetup, getcreds, sendmsg, logs }
