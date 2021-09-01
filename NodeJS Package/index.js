const axios = require('axios');
var Joke = require('one-liner-joke');
const errors = require('./error');
const brainshopurl = "http://api.brainshop.ai/get"

let bid = "undefined";
let apikey = "undefined";
let jokefilter = {'exclude_tags': ['dirty', 'racist', 'marriage', 'sex']}
const getcreds = function () {
    let as = "Brain ID : " + bid + " \nAPIKey : " + apikey;
    return as;
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