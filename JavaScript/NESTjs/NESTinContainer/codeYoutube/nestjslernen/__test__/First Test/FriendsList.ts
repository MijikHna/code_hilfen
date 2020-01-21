export class FriendsList {
    friends = [];

    addFriend(name) {
        this.friends.push(name);
        this.announceFriendship(name);
    }

    announceFriendship(name) {
        global.console.log(`${name} is now a friend!`); //global
    }

    removeFriend(name) {
        const idx = this.friends.indexOf(name);

        if (idx === -1) {
            throw new Error("Friend not found");
        }

        this.friends.splice(idx, 1); //eigentlich removen
    }
}