document.addEventListener('DOMContentLoaded', () => {

    const cardArray = [{
            name: 'fries',
            imgUrl: './images/fries.png'
        },
        {
            name: 'hotdog',
            imgUrl: './images/hotdog.png'
        },
        {
            name: 'ice-cream',
            imgUrl: './images/ice-cream.png'
        },
        {
            name: 'milkshake',
            imgUrl: './images/milkshake.png'
        },
        {
            name: 'pizza',
            imgUrl: './images/pizza.png'
        },
        {
            name: 'cheeseburger',
            imgUrl: './images/cheeseburger.png'
        },
        {
            name: 'fries',
            imgUrl: './images/fries.png'
        },
        {
            name: 'hotdog',
            imgUrl: './images/hotdog.png'
        },
        {
            name: 'ice-cream',
            imgUrl: './images/ice-cream.png'
        },
        {
            name: 'milkshake',
            imgUrl: './images/milkshake.png'
        },
        {
            name: 'pizza',
            imgUrl: './images/pizza.png'
        },
        {
            name: 'cheeseburger',
            imgUrl: './images/cheeseburger.png'
        },
    ];

    const grid = document.querySelector('.grid');
    const resultDisplay = document.querySelector('#result');

    var cardsChosen = [];
    var cardsChosenId = [];
    var cardsWon = [];

    //blank.png in Grid setzen
    function creatBoard() {
        for (let i = 0; i < cardArray.length; i++) {
            var card = document.createElement('img');
            card.setAttribute('src', './images/blank.png');
            card.setAttribute('data-id', i);
            card.addEventListener('click', flipCard);
            grid.appendChild(card);
        }
    }

    function flipCard() {
        var cardId = this.getAttribute('data-id');
        cardsChosen.push(cardArray[cardId].name);
        cardsChosenId.push(cardId);
        this.setAttribute('src', cardArray[cardId].imgUrl);

        if (cardsChosen.length === 2) {
            setTimeout(checkForMatch, 500);
        }
    }

    function checkForMatch() {
        var cards = document.querySelectorAll('img');
        const optionOneId = cardsChosenId[0];
        const optionTwoId = cardsChosenId[1];
        if (cardsChosen[0] === cardsChosen[1]) {
            alert('Match');
            cards[optionOneId].setAttribute('src', './images/white.png');
            cards[optionTwoId].setAttribute('src', './images/white.png');
            cardsWon.push(cardsChosen);
        } else {
            cards[optionOneId].setAttribute('src', 'images/blank.png');
            cards[optionTwoId].setAttribute('src', 'images/blank.png');
            alert("No Match");
        }
        cardsChosen = [];
        cardsChosenId = [];
        resultDisplay.textContent = cardsWon.length;
        if (cardsWon.length === cardArray.length / 2) {
            resultDisplay.textContent("You have won");
        }
    }

    cardArray.sort(() => 0.5 - Math.random());

    creatBoard();
});