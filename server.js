const express = require('express');
const bodyParser = require('body-parser');
const AWS = require('aws-sdk');
const config = require('./config.js');
const cors = require('cors');

const app = express();
const PORT = 3000;

// Setting the configurations for AWS
AWS.config.update(config.aws_remote_config);

app.use(cors());
app.use(bodyParser.json());

app.get('/api/data', async (req, res) => {
  const dynamodb = new AWS.DynamoDB.DocumentClient();
  const params = {
    TableName: "SensorData",
  };

  try {
    const data = await dynamodb.scan(params).promise();

    if (data.Items.length === 0) {
      res.status(404).json({ error: "No Sensor Data found" });
    } else {
      res.json(data.Items);
    }
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
