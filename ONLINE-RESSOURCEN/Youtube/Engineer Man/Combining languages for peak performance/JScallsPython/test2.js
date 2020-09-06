const fs = require("fs")
const net = require("net")

fs.open("data.pipe", fs.constants.O_RDONLY, (err,fd) => {
    const pipe = new net.Socket((fd));

    let buffer = "";

    pipe.on("data", data => {
        buffer += data;
    });

    //Wenn im Buffer nichts mehr ist und er geschlossen wird
    pipe.on("end", () => {
        console.log(JSON.parse(buffer));
    });
});