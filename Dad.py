import requests
import pyfiglet
import termcolor
from random import choice


class Joke(object):

    def main(self):

        header = pyfiglet.figlet_format("Dad Joke 3000")
        header = termcolor.colored(header, color="magenta")
        print(header)

        term = input("Let me tell you a joke! Give me a topic: ")
        response_json = requests.get(
            "https://icanhazdadjoke.com/search",
            headers={"Accept": "application/json"},
            params={"term": term}
        ).json()
        results = response_json["results"]
        total_jokes = response_json["total_jokes"]
        if total_jokes > 6:
            print(
                f"Oh man, I've got way too many jokes here. There is {total_jokes} jokes about {term}. "
                f"Let's see... Here's one:\n",
                choice(results)['joke']
            )
        elif total_jokes > 1:
            print(
                f"I've got {total_jokes} jokes about {term}. Here's one:\n",
                choice(results)['joke']
            )
        elif total_jokes == 1:
            print(
                f"I've got one joke about {term}. Here it is:\n",
                results[0]['joke']
            )
        else:
            print(f"Sorry, I don't have any jokes about {term}! Please try again.")

        repeat = input("Would you like to hear another? y/n ")
        if repeat.lower() == "y":
            Joke.main(self)
        else:
            exit()



if __name__ == '__main__':
    Joke().main()
