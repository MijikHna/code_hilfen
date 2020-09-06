from typing import List, Optional
name = "Kirill"  # type: str        <- nach PEP484
question = "Wie geht's?"


def greeter01(person, queston):
    greeting_phrase = f'Hallo, {person} {question}'
    return greeting_phrase


# if __name__ == "__main__":
#     greeting = greeter01(person=name, quetion=questoin)
#     print(greeting)

# Jetzt begint Typ Annotationen
name: str = "Kirill"
question: str = "Wie geht's?"


def greeter02(person: str, quetion: str) -> str:
    greeting_phrase: str = f'Hallo, {person} {question}'
    return greeting_phrase


if __name__ == "__main__":
    greeting = greeter02(person=name, quetion=question)
    print(greeting)

name: Optional[List[str]] = "Kirill"  # Typ ist etweder List-Array oder NaN
