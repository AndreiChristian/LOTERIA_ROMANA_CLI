import random
import time
import os


def print_loteria_ascii_art():
    print("  _           _            _         _____                                   ")
    print(" | |         | |          (_)       |  __ \                                  ")
    print(" | |     ___ | |_ ___ _ __ _  __ _  | |__) |___  _ __ ___   __ _ _ __   __ _ ")
    print(" | |    / _ \| __/ _ \ '__| |/ _` | |  _  // _ \| '_ ` _ \ / _` | '_ \ / _` |")
    print(" | |___| (_) | ||  __/ |  | | (_| | | | \ \ (_) | | | | | | (_| | | | | (_| |")
    print(" |______\___/ \__\___|_|  |_|\__,_| |_|  \_\___/|_| |_| |_|\__,_|_| |_|\__,_|")


class LoteriaRomana:
    def __init__(self):
        self.participanti = ["Rafa", "Cecilia", "Alex", "Horatiu", "Ivona", "Andrei", "Nicolae"]
        self.castigatori = []

    def get_castigator(self):
        # If all participants have been selected, reset the list
        if len(self.castigatori) == len(self.participanti):
            self.castigatori = []
            self.clear_console()
            print("\033[1;36;40mToti participantii au fost selectati. Resetare...\033[0m")
            time.sleep(1.5)
        # Select a participant who hasn't won yet
        participant = random.choice([s for s in self.participanti if s not in self.castigatori])
        self.castigatori.append(participant)
        return participant

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def afisare_castigator(self, nume):
        print("\033[1;34;40m-----------------------------------------------------\033[0m")
        print("\033[1;34;40m|                                                   |\033[0m")
        print("\033[1;34;40m|    \033[1;37;40mMarele castigator: \033[1;34;40m                            |\033[0m")
        print("\033[1;34;40m|     \033[1;37;40m{}\033[1;34;40m                          |\033[0m".format(nume.center(20)))
        print("\033[1;34;40m|                                                   |\033[0m")
        print("\033[1;34;40m-----------------------------------------------------\033[0m")

    def run(self):
        self.clear_console()
        print_loteria_ascii_art()

        print("\033[1;36;40mBine ati venit la Loteria Romana!\033[0m")
        while True:
            input("\033[1;96;40mApasa ENTER pentru a selecta marele castigator...\033[0m")
            self.clear_console()
            print("\033[1;36;40mBine ati venit la Loteria Romana!\033[0m")
            self.afisare_castigator(self.get_castigator())
            print("\033[1;94;40m-------------------------------\033[0m")


if __name__ == "__main__":
    loterie = LoteriaRomana()
    loterie.run()

