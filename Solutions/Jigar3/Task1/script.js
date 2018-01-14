// var xhttp = new XMLHttpRequest();
// xhttp.open("POST", "https://jobs.github.com/positions.json?description=ruby&location=newyork");
// xhttp.setRequestHeader("Content-type", "application/json");
// xhttp.send();
// // var response = JSON.parse(xhttp.responseText);
//
// var response = xhttp.responseText;
// console.log(response)
const yargs = require('yargs')
const h2p = require('html2plaintext')
const request = require('request');


const argv = yargs
  .options({
    a: {
      describe: 'Address of the location',
      demand: true,
      alias: 'address',
      string: true
    },
    d: {
      describe: 'Job Description',
      demand: true,
      alias: 'jobDes',
      string: true
    }
  })
  .help()
  .alias('help', 'h')
  .argv;

request({
  url: `http://jobs.github.com/positions.json?description=${argv.jobDes}&location=${argv.address}`,
  json: true,
}, (error,response, body) => {
  for(var i=0; i<body.length; i++){
    console.log(`Job ${i+1} ==>`)
    console.log(`Title: ${body[i].title}`);
    console.log(`Location: ${body[i].location}`);
    console.log(`Type: ${body[i].type}`);
    var description = h2p(body[i].description);
    console.log(`Description: ${description}`)
    console.log(`Company: ${body[i].company}`);
    var howTo = h2p(body[i].how_to_apply);
    console.log(`How to apply: ${howTo}`);
    console.log(`-------------------------------------------`)
  }
}
)
