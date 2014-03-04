
var request = require('request');

var doId = '457429a47bc44ba98ada4a66d181aad1' ,
    key = '7e79c411cb2dbb41ad364ca78dbdd9a8' ;
var cloudId = 'areose21@gmail.com',
    token = '7ca53cd5a4d6e9411adbb224eec2c4c0e4f81';
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
   // console.log(info.response.zones.objs[0].zone_name);
    console.log(getValues(info,'zone_name'));
}



request.post(cloudOption,Ccallback);
//request(options, callback);
//////////////////////////////////////////////////////////////////////////////////////////////
function getObjects(obj, key, val) {
    var objects = [];
    for (var i in obj) {
        if (!obj.hasOwnProperty(i)) continue;
        if (typeof obj[i] == 'object') {
            objects = objects.concat(getObjects(obj[i], key, val));
        } else
//if key matches and value matches or if key matches and value is not passed (eliminating the case where key matches but passed value does not)
        if (i == key && obj[i] == val || i == key && val == '') { //
            objects.push(obj);
        } else if (obj[i] == val && key == ''){
//only add if the object is not already in the array
            if (objects.lastIndexOf(obj) == -1){
                objects.push(obj);
            }
        }
    }
    return objects;
}

//return an array of values that match on a certain key
function getValues(obj, key) {
    var objects = [];
    for (var i in obj) {
        if (!obj.hasOwnProperty(i)) continue;
        if (typeof obj[i] == 'object') {
            objects = objects.concat(getValues(obj[i], key));
        } else if (i == key) {
            objects.push(obj[i]);
        }
    }
    return objects;
}

//return an array of keys that match on a certain value
function getKeys(obj, val) {
    var objects = [];
    for (var i in obj) {
        if (!obj.hasOwnProperty(i)) continue;
        if (typeof obj[i] == 'object') {
            objects = objects.concat(getKeys(obj[i], val));
        } else if (obj[i] == val) {
            objects.push(i);
        }
    }
    return objects;
}




//example of grabbing objects that match some key and value in JSON
//console.log(getObjects(js,'ID','SGML'));
//returns 1 object where a key names ID has the value SGML

//example of grabbing objects that match some key in JSON
//console.log(getObjects(js,'ID',''));
//returns 2 objects since keys with name ID are found in 2 objects

//example of grabbing obejcts that match some value in JSON
//console.log(getObjects(js,'','SGML'));
//returns 2 object since 2 obects have keys with the value SGML

//example of grabbing objects that match some key in JSON
//console.log(getObjects(js,'ID',''));
//returns 2 objects since keys with name ID are found in 2 objects

//example of grabbing values from any key passed in JSON
//console.log(getValues(js,'ID'));
//returns array ["SGML", "44"]

//example of grabbing keys by searching via values in JSON
//console.log(getKeys(js,'SGML'));
//returns array ["ID", "SortAs", "Acronym", "str"]