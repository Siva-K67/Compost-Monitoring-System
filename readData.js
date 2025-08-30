// readData.js

const AWS = require('aws-sdk');
const config = require('./config.js');

// Setting the configurations
AWS.config.update(config.aws_remote_config);

const readSensorData = async () => {
  const dynamodb = new AWS.DynamoDB.DocumentClient();

  const params = {
    TableName: "SensorData",
  };

  try {
    // Call DynamoDB to scan the table
    const data = await dynamodb.scan(params).promise();
    
    if (data.Items.length === 0) {
      console.log("No Sensor Data found");
    } else {
      console.log("Sensor Data:");
      data.Items.forEach(item => {
        console.log(item);
      });
    }
  } catch (err) {
    console.log("Error", err);
  }
};

// Call the asynchronous function to read data
readSensorData();
