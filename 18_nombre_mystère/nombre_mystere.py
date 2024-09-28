#!/usr/bin/env python

"""
Filename: nombre_mystere.py
Author: Nero
Description: Jeu du nombre mystère
Usage: python nombre_mystere.py
"""

from random import randint
from enum import StrEnum


class Colors(StrEnum):
    """Classe de coloration syntaxique
    """
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    PURPLE = '\033[95m'
    FAIL = '\033[91m'
    END = '\033[0m'


class MysteryNumber():
    """Classe du jeu Nombre Mystère
    """

    def __init__(self, max_tries: int, range_min: int, range_max: int):
        self.max_tries = max_tries
        self.tries = self.max_tries
        self.range_min = range_min
        self.range_max = range_max
        self.number_to_guess = randint(self.range_min, self.range_max)
        self.number_user = None

    def run(self):
        """Méthode contenant la boucle principale du jeu
        """
        msg_menu = 'Bienvenue dans le jeu du Nombre Mystère !\n' + f'Vous avez {self.tries} essais.\n' +\
            '==================================================================='
        self.display(msg_menu)
        while True:
            self.number_user = input('Veuillez entrer un nombre entre 1 et 100 : ')

            if (not self.number_user) or (not self.number_user.isdigit()) \
                    or (int(self.number_user) > 100) or (int(self.number_user) < 1):
                msg_err = f'{Colors.WARNING}Veuillez entrer un nombre valide (compris entre 0 et 100){Colors.END}\n'+\
                    f'Il vous reste {self.tries} essais\n'+\
                    '___________________________________________________________________\n'
                self.display(msg_err)
                continue

            # Message si le nombre est plus grand que le nombre à deviner
            greater_than = f'Le nombre mystère est plus grand que {self.number_user}'
            # Message si le nombre est plus petit que le nombre à deviner
            lower_than = f'Le nombre mystère est plus petit que {self.number_user}'
            if int(self.number_user) == self.number_to_guess:
                msg_won = f'{Colors.OKGREEN}Bravo ! Le nombre mystère était bien {self.number_user}\n' +\
                    f'Vous avez trouvé le nombre en {self.max_tries-self.tries} essai(s){Colors.END}\n'
                self.display(msg_won, self.replay)
            else:
                display = greater_than if int(self.number_user) < self.number_to_guess else lower_than
                self.display(display)
            self.tries -= 1
            print(f'Il vous reste {self.tries} essais')
            if self.tries == 1:
                print(Colors.PURPLE+"Dernier essai"+Colors.END)
            # Message s'il n'y a plus d'essais
            elif self.tries == 0:
                msg_lost = f'{Colors.FAIL}Dommage ! Le nombre mystère était {self.number_to_guess}!{Colors.END}'
                self.display(msg_lost, self.replay)

    def display(self, message: str, fct=None) -> None:
        """Méthode à appeler en cas de victoire
        """
        print(message)
        if fct:
            fct()

    def replay(self) -> None:
        """Méthode à appeler pour rejouer

        Raises:
            SystemExit: Exit du programme
        """
        while True:
            replay = input("Voulez-vous rejouer ? (y or n)")
            if replay == "y":
                self.tries = self.max_tries
                self.number_to_guess = randint(self.range_min, self.range_max)
                self.run()
            elif replay == "n":
                print('Fin du jeu.')
                raise SystemExit()
            else:
                print("Répondez par 'y' ou 'n'")
                continue


if __name__ == "__main__":
    game = MysteryNumber(max_tries=8, range_min=1, range_max=100)
    game.run()
