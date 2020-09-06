const myPromise = new Promise((resolve, reject) => {
    let condition = Math.round(Math.random());

    if (condition) {
        resolve('Promise is resolved successfully.');
    } else {
        reject('Promise is rejected');
    }
});


myPromise.then((message) => {
    console.log(message);
}).catch((message) => {
    console.log(message);
});