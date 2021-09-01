const axios = require('axios');
var Joke = require('one-liner-joke');
const wiki = require('wikipedia');
const errors = require('./error');
const brainshopurl = "http://api.brainshop.ai/get"

let bid = "undefined";
let apikey = "undefined";
let jokefilter = {'exclude_tags': ['dirty', 'racist', 'marriage', 'sex']}
const getcreds = function () {
    let as = "Brain ID : " + bid + " \nAPIKey : " + apikey;
    return as;
}
function capfirst(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
  }
const sendmsg = async function (message,uiid = "ChatBot") {
    try {
        message = message.toLowerCase()
        if (message === "" || message == null) {
            throw new errors.NoMessagePassed();
        }
        if (message.includes("joke")) {
            return Joke.getRandomJoke(jokefilter).body;
        }
        if (message.includes("wikipedia")) {
            (async () => {
                try {
                    message = message.replace("wikipedia", "")
                    message = capfirst(message)
                    const page = await wiki.page(message);
                    const summary = await page.summary();
                    let result = "According to Wikipedia: \n" + summary
                    return summary
                    //Response of type @wikiSummary - contains the intro and the main image
                } catch (error) {
                    console.log(error);
                    return error;
                    //=> Typeof wikiError
                }
            })()
        }
        params = {
            'bid' : bid,
            'key' : apikey,
            'uid' : uiid,
            'msg' : message
        }
        const response = await axios.get(brainshopurl,{params});
        return response.data.cnt;
    } catch (error) {
        console.error(error);
        return error;
    }
}
const chatbotsetup = function (brain, api) {
    if (brain === "" || brain == null) {
        throw new errors.EssentialArgumentMissing("Brain ID is required!")
    }
    if (api === "" || api == null) {
        throw new errors.EssentialArgumentMissing("API Key is required!")
    }
    bid = brain;
    apikey = api;
    console.log("Chatbot Credentials Set!");
    console.log(getcreds());
}

module.exports = {chatbotsetup, getcreds , sendmsg}