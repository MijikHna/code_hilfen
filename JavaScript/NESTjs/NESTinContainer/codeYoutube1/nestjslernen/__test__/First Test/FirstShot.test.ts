import { FriendsList } from "./FriendsList";


describe("FriendList", () => {
    let friendsList: FriendsList;

    beforeEach(() => {
        friendsList = new FriendsList();
    });


    it("init friends list", () => {
        expect(friendsList.friends.length).toEqual(0);
    });


    it("add a friend to friends list", () => {
        friendsList.addFriend("Test")
        expect(friendsList.friends.length).toEqual(1);
    });

    //hier Mock Funktion benutzen 
    //Mock - trackt, welche, wie oft, mit welchen Parametern Funktion aufgerufen wurde => Behavior simulieren
    it("announce friend ship", () => {
        friendsList.announceFriendship = jest.fn(); //Mock-Funktion die trackt die Funktion announceFriendship()

        expect(friendsList.friends.length).not.toHaveBeenCalled(); //not flipped hier das Output
        friendsList.addFriend("Test")
        expect(friendsList.friends.length).toHaveBeenCalledTimes(1); //Oder z.B so
    });

    describe("remove Friend", () => {
        it("remove a Friend", () => {
            friendsList.addFriend("Text");
            expect(friendsList.friends[0]).toEqual("Text");
            friendsList.removeFriend("Text");
            expect(friendsList.friends[0]).toBeUndefined();
        });

        it("throw an Error", () => {
            expect(() => friendsList.removeFriend("Text")).toThrow(); //die expect erwartet Throw
            expect(() => friendsList.removeFriend("Text")).toThrow(new Error("Friend not found"));
            //expect(friendsList.friends[0]).toBeUndefiend();
        });
    });

    describe("FriendList", () => {
        it("init friends list", () => {
            //const firendsList = new FriendsList();
            expect(friendsList.friends.length).toEqual(0);
        });

        it("add a friend to friends list", () => {
            //const firendsList = new FriendsList();
            friendsList.addFriend("Test")
            expect(friendsList.friends.length).toEqual(1);
        });

        //hier Mock Funktion benutzen 
        //Mock - trackt, welche, wie oft, mit welchen Parametern Funktion aufgerufen wurde => Behavior simulieren
        it("announce friend ship", () => {
            //const firendsList = new FriendsList();
            friendsList.announceFriendship = jest.fn(); //Mock-Funktion die trackt die Funktion announceFriendship()

            expect(friendsList.friends.length).not.toHaveBeenCalled(); //not flipped hier das Output
            friendsList.addFriend("Test")
            expect(friendsList.friends.length).toHaveBeenCalledTimes(1); //Oder z.B so
        });
    });
});