'use strict';

console.log('the script starts');

// esimerkki materiaalista
function synchronousFunction() {
    let number = 1;
    for (let i = 1; i < 100000; i++) {
        number += i;
        console.log('synchronousFunction running');
    }
    console.log('regular function complete', number);
}

async function asynchronousFunction() {                 // asynchronous function is defined by the async keyword
    console.log('asynchronous download begins');
    try {                                               // error handling: try/catch/finally
        const response = await fetch('https://api.chucknorris.io/jokes/random');    // starting data download, fetch returns a promise which contains an object of type 'response'
        const jsonData = await response.json();          // retrieving the data retrieved from the response object using the json() function
        console.log(jsonData.value);    // log the result to the console
    } catch (error) {
        console.log(error.message);
    } finally {                                         // finally = this is executed anyway, whether the execution was successful or not
        console.log('asynchronous load complete');
    }
}

//synchronousFunction();
//asynchronousFunction();

// pics.json latausesimerkki

// oldschool promisen käsittely (toimii, mutta ei suositella)
fetch('pics.json').then(function (data) {
    console.log('response data: ', data);
    data.json().then(function (data) {
        console.log('json data', data);
        // tänne koodi, millä käsitellään ladattu json data
    }).catch(function (error) {
        console.error(error);
    });
}).catch(function (error) {
    console.error(error);
});

// suositeltu moderni tapa (await-async)
async function fetchPics(){
    const picsDiv = document.querySelector('#pics');
    try {
        const response = await fetch('pics.asjdjasd');
        //console.log('response status', response.status, response.statusText, response.ok);
        if (!response.ok) {
            throw new Error('response status not ok!');
        }
        const pics = await response.json();
        console.log('pics', pics);
        for (const pic of pics);
            const imgElem = document.createElement('img');
            imgElem.src = pic.address;
            imgElem.alt = pic.description;
            picsDiv.append(imgElem);

    } catch (error) {
        console.error(error);
        picsDiv.innerHTML = '<p>Kuvien lataamisessa onglema</p>'
    }
}

document.querySelector('button').addEventListener('click', function() {
    fetchPics();
});

console.log('the script ends');

//TODO: kopsaa githubista esimerkit, myös HTML ja JSON. MYÖS MOD03 aiheet.