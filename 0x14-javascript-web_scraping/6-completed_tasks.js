#!/usr/bin/node
// Computes the number of tasks completed by user id.

const url = process.argv[2];
const completedTasks = {};
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body).filter(task => task.completed);
    for (let index = 1; index <= 10; index++) {
      const userTasks = tasks.filter(task => task.userId === index);
      if (userTasks.length) {
        completedTasks[index.toString()] = userTasks.length;
      }
    }
    console.log(completedTasks);
  }
});
