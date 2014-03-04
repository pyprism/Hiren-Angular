
var request = require('request');

var doId = '' ,
    key = '' ;
var cloudId = '',
    token = '';
var options = {
    url: 'https://api.digitalocean.com/droplets/?client_id=' + doId + '&api_key=' + key

};

var cloudOption ={
    url: 'https://www.cloudflare.com/api_json.html?a=zone_load_multi&tkn=' + token + '&email=' + cloudId
};

function callback(error, response, body) {
    if (!error && response.statusCode == 200) {
        var info = JSON.parse(body);
        var x = info.droplets;
        console.log(info.droplets[0].ip_address);
    }
}

function Ccallback(error, response, body) {
    var info = JSON.parse(body);
    console.log(info.response.zones);
}



request.post(cloudOption,Ccallback);
//request(options, callback);