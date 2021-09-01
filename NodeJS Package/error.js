class NoMessagePassed extends Error {  
    constructor () {
        super("Message field cannot be kept empty.")
        this.name = this.constructor.name
        Error.captureStackTrace(this, this.constructor);
    }
}
class EssentialArgumentMissing extends Error {  
    constructor (message) {
        super(message)
        this.name = this.constructor.name
        Error.captureStackTrace(this, this.constructor);
    }
}


module.exports = {NoMessagePassed, EssentialArgumentMissing}