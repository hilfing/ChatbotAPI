const axios = require('axios');
const errors = require('./error');
const brainshopurl = "http://api.brainshop.ai/get"

let bid = "undefined";
let apikey = "undefined";
const getcreds = function () {
    let as = "Brain ID : " + bid + " \nAPIKey : " + apikey;
    return as;
}
const sendmsg = async function (message,uiid = "ChatBot") {
    try {
        if (message === "" || message == null) {
            throw new errors.NoMessagePassed()
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
        console.error(error)
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