const Twilio = require("twilio");
require("dotenv").config();

const client = new Twilio(
  process.env.TWILIO_ACCOUNT_SID,
  process.env.TWILIO_AUTH_TOKEN
);

client.messages
  .list()
  .then((messages) =>
    console.log(`The most recent message is ${messages[0].body}`)
  );

console.log("Gathering your message log");
