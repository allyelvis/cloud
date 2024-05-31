const { PubSub } = require('@google-cloud/pubsub');
const pubsub = new PubSub();

exports.publishMessage = async (req, res) => {
    try {
        const data = JSON.stringify(req.body);
        const dataBuffer = Buffer.from(data);

        await pubsub.topic('my-topic').publish(dataBuffer);

        res.status(200).send('Message published.');
    } catch (error) {
        console.error(error);
        res.status(500).send(error);
    }
};
