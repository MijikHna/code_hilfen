import Redis from 'ioredis';

//const redis = new Redis();
const redis = new Redis(6379, '10.200.0.10');
//const redis = new Redis({password: "sicheresPasword"});


redis.set("name", "Kirill");
redis.get("name", (err, result) => {
    console.log(result);
});

//Kapitel 3:
// Unterteil 2 - String in Action
//redis.set(key, value, [ex, sec])
redis.set("name", "Emmanuel", "EX", 5); //set + expire
redis.get("address", (err, result) => {
    console.log(result);
});

redis.incrby("address", 300);
redis.get("address", (err, result) => {
    console.log(result);
});

redis.mset("street", "Awesome", "city", "San Francisco");
redis.mget("street", "city", (err, result) => {
    console.log(result);
});