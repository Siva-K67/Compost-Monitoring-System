// commented code was adding data from dummy file
// const AWS = require('aws-sdk');
// const config = require('./config.js');

// // Setting the configurations
// AWS.config.update(config.aws_remote_config);

// const addSensorData = async () => {
//   const dynamodb = new AWS.DynamoDB.DocumentClient();

//   const sensorData = [
//     { Day: 1, Temperature: 32, pHValue: 7.0, H2S: 368 },
//     { Day: 2, Temperature: 32, pHValue: 7.0, H2S: 367 },
//     { Day: 3, Temperature: 32, pHValue: 6.8, H2S: 365 },
//     { Day: 4, Temperature: 32, pHValue: 6.8, H2S: 363 },
//     { Day: 5, Temperature: 32, pHValue: 6.8, H2S: 359 },
//   ];

//   const params = {
//     TableName: "SensorData",
//   };

//   try {
//     // Iterate through sensorData array and insert each item into the table
//     for (const item of sensorData) {
//       const data = await dynamodb.put({
//         ...params,
//         Item: {
//           sensorId: "abc123", // Replace with your actual sensorId
//           timestamp: Date.now(), // Use current timestamp as an example, adjust accordingly
//           Day:item.Day,
//           temperature: item.Temperature,
//           pHValue: item.pHValue,
//           H2S: item.H2S,
//         },
//       }).promise();

//       console.log(`Sensor Data Added for Day ${item.Day}`, data);
//     }
//   } catch (err) {
//     console.log("Error", err);
//   }
// };

// // Call the asynchronous function to insert data
// addSensorData();

const fs = require('fs');
const AWS = require('aws-sdk');
const config = require('./config.js');

// Setting the configurations
AWS.config.update(config.aws_remote_config);

// Function to parse the data from the file
const parseData = (data) => {
  const sensorData = [];
  
  // Split the data by comma to separate fields
  const fields = data.split(',');

  // Iterate through each field
  const obj = {};
  for (const field of fields) {
    // Split each field by colon to separate key and value
    const [key, value] = field.split(':');

    // Check if both key and value are present
    if (key && value) {
      // Trim whitespace from key and value, and store in object
      obj[key.trim()] = value.trim();
    }
  }
  
  // Push the object into the array
  sensorData.push(obj);

  return sensorData;
};

const addSensorDataFromFile = async () => {
  const dynamodb = new AWS.DynamoDB.DocumentClient();

  try {
    // Read data from the text file
    const dataFromFile = fs.readFileSync('datafile.txt', 'utf8');
    
    // Parse the data to extract relevant fields
    const sensorDataArray = parseData(dataFromFile);

    const params = {
      TableName: "SensorData",
    };

    // Iterate through sensorDataArray and insert each item into the table
    for (const item of sensorDataArray) {
      const data = await dynamodb.put({
        ...params,
        Item: {
          sensorId: "abc123", // Replace with your actual sensorId
          timestamp: Date.now(), // Use current timestamp as an example, adjust accordingly
          pH: item.pH,
          NH3: item.NH3,
          H2S: item.H2S,
          CH4: item.CH4,
          CO2: item.CO2,
          Soil: item.Soil,
          Temperature: item.Temperature,
          Humidity: item.Humidity,
        },
      }).promise();

      console.log(`Sensor Data Added`, data);
    }
  } catch (err) {
    console.log("Error", err);
  }
};

// Call the asynchronous function to insert data
addSensorDataFromFile();
