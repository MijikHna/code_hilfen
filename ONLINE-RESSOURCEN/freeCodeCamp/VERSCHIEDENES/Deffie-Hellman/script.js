function encrypt(message, key) {
    chipherText = message.split('').map(character => {
        const characterAsciiCode = character.charCodeAt(0);
        return String.fromCharCode(characterAsciiCode + key.length)
    });
    chipherText = chipherText.join('');
    return chipherText;
}

function decrypt(chipher, key) {
    let message = chipher.split('').map(character => {
        const characterAsciiCode = character.charCodeAt(0);
        return String.fromCharCode(characterAsciiCode - key.length)
    }).join('');
    return message;
}