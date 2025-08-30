const AWS = require('aws-sdk');
const config = require('./config.js');

// Setting the configurations
AWS.config.update(config.aws_remote_config);

// Creating the table named "SensorData"
const createSensorDataTable = async () => {
  // Making a DynamoDB instance
  const dynamodb = new AWS.DynamoDB();

  // Providing table name, attribute name, etc as params
  const params = {
    TableName: "SensorData",
    KeySchema: [
      { AttributeName: "sensorId", KeyType: "HASH" },
      { AttributeName: "timestamp", KeyType: "RANGE" },
    ],
    AttributeDefinitions: [
      { AttributeName: "sensorId", AttributeType: "S" },
      { AttributeName: "timestamp", AttributeType: "N" }, // Assuming timestamp is a number, adjust accordingly
    ],
    ProvisionedThroughput: {
      ReadCapacityUnits: 5,
      WriteCapacityUnits: 5
    }
  };

  try {
    // Call DynamoDB to create the table
    const data = await dynamodb.createTable(params).promise();
    console.log("SensorData Table Created", data);
  } catch (err) {
    console.log("Error", err);
  }
};


// Call the asynchronous functions
createSensorDataTable();


