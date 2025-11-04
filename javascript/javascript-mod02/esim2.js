console.log("moro");


let emptyArray = [];

//taulukko array
let items = [1, 2, 3, {name : 'Konsta'}, [0,1,2], 'merkkijono'];
console.log(items);



console.log(items[3]);               // Alkioon viitataan indeksillä

items[0] = 99;                       // Alkion arvoa voidaan muuttaa indeksin avulla
console.log(items);

items[9] = 'Olen uusi alkio';
console.log(items);

console.log(items[6]);     //välissä on nyt määrittelemätön alkio "undefined". Ei tartte vielä tästä olla huolissaan.

let fruits = ['Banaani', 'Mango', 'Pear', 'Strawberry'];
console.log(fruits);
console.log('Taulukon pituus:', fruits.length);

let elem = document.querySelector('#heading');
console.log(elem);
console.dir(elem);
//elem.innerText = 'Mod2 esimerkit';

// taulukon looppaus eri tavoin
// perinteinen for
// yleinen tapa. Tarvitaan indeksi
console.log('--------------------')
console.log('Perinteinen FOR-looppi')

for (let i = 0; i < fruits.length; i++) {
    console.log(`Hedelmä ${i+1} on ${fruits[i]}`);
}

// Helppo ja nopea tapa iteroida ilman indeksiä

console.log('----------------------')
console.log('Läpikäynti for / of rakenteella, joilla saadaan arvot');

for (let fruit of fruits) {
    console.log(fruit);
}

// Harvemmin käytetään taulukoiden kanssa
// Js objektien kanssa jeba
console.log('----------------------')
console.log('Läpikäynti for / in rakenteella, joilla saadaan arvot ja index');
for (const index in fruits) {
    console.log(index, fruits[index]);
}


// Näin lisäät arrayhin tietoa:

fruits.sort();
console.log(fruits);
fruits.reverse();
console.log(fruits);

// ei toimi numeroiden kanssa kovinkaan hyvin'

const ages = [2300, 28, 33, 19, 2000];
ages.sort();
console.log(ages);

// Tämä toimii numeroiden kanssa
ages.sort(((a, b) => a - b));
console.log(ages);
ages.sort((a, b) => b - a);
console.log(ages);

// shift() deletes and returns the 1st item in the array
// pop() deletes and returns the last item in the array
// push(value) adds the value at the end of the array, multiple values separately
// includes(value) checks whether the array contains the given value

let hedelmat = ['Banaani', 'Mango', 'Päärynä', 'Omena'];

// shift() poistetaan taulukon eka arvo ja otetaan muuttuja talteen'
const hedelma = hedelmat.shift();
console.log('Poistettiin', hedelma);
console.log(hedelmat);


// unshift lisää taulukon alkuun

hedelmat.unshift('Kiwi');
console.log(hedelmat);

// sama kuin shift mutta vika
const vika = hedelmat.pop();
console.log('Poistettiin', vika);
console.log(hedelmat);

hedelmat.push('Satsuma', 'Mandariini');
console.log(hedelmat);

// includes tsekkaa onko arvo taulukossa ja palauttaa true/false
console.log(hedelmat.includes('Kiwi'));

