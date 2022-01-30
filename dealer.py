import numpy as np
import sys
from player import Player
import os
import config


def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    print("== [ QUACKJACK ] == ")
    print("\n")


class Dealer:
    def __init__(self):
        self.players = []
        
    def greet(self):
        cls()
        print("Welcome to QUACKJACK!")
        print("In this game, player's goal is to manipulate their quantum circuit to get more points than the opponent, but not go bust.")
        print("On their turn, a player can either draw two more qubits or create entanglement by placing a Controlled-NOT gate in their circuit.")
        print("""Drawn qubits will become one of the following states at random:
    [0] A qubit with pure 0 value
    [1] A qubit with pure 1 value (equivalently, an X gate will be added to it)
    [+] In superposition of 0 and 1: (|0> + |1>)/sqrt(2) (equivalently, an H gate will be added)
    [-] In superposition of 0 and 1: (|0> - |1>)/sqrt(2) (equivalently, X and H gates will be added).""")
        print("""A Controlled-NOT gate from qubit A to B works as follows:
    - If A is 0, then B will be left unchanged
    - If A is 1, then B will be inverted.""")
        print("""When all qubits are drawn and all gates are placed, the circuit will be run on an IonQ quantum computer. In the end, all qubits will be classically measured, and player's score will be the sum of qubits' values.""")
        print(f"Player will go bust if their score ends up being more than {config.BUST_NUMBER}.")
        print("Of the players who did not go bust, the player with the highest score wins the bets.")
        print("\n")
        print(f"""CONFIGURATION:
    - Maximum number of qubits you can draw: {config.QUBIT_COUNT}
    - Maximum number of gates you can apply: {config.GATE_COUNT}
    - Qubits have to be drawn at once: {config.DRAW_QUBITS}
    - Player will go bust if they have more than: {config.BUST_NUMBER}\n\n""")

    def init_players(self):
        n = int(input("How many people will play? "))
        for i in range(n):
            self.players.append(Player())

    def run_player(self, i):
        pl = self.players[i]
        s = f"PLAYER {i+1}:"
        # draw cards
        while True:
            cls()
            drew = [f"[{x}]" for x in pl.draw()] 
            print(f"{s} You drew {' and '.join(drew)}")
            print(f"{s} Your circuit so far:")
            print(pl.circuit.draw())
            if not pl.can_draw():
                print(f"{s} You can't draw any more qubits!")
                break
            if input(f"{s} Draw (Y/N)? ").upper() != "Y":
                print(f"{s} You stopped drawing qubits.")
                break
        pl.finish_drawing()
        input(f"{s} Press ENTER to proceed to gates.\n")
        # apply gates
        while True:
            cls()
            print(f"{s} Your circuit so far:")
            print(pl.circuit.draw())
            if not pl.can_apply_gate():
                print(f"{s} You can't apply any more gates!")
                break
            if input(f"{s} Apply a Controlled-NOT gate (Y/N)? ").upper() != "Y":
                print(f"{s} You stopped applying gates.")
                break
            cards = [int(x) for x in input(f"{s} Cards to apply the gate to (ex. 0 1): ").split(" ")]
            pl.apply_gate("CNOT", cards[0], cards[1])
        pl.finish_applying_gates()
        input(f"{s} Press ENTER to finish your turn.\n")

    def run_players(self):
        for i in range(len(self.players)):
            cls()
            input(f"PLAYER {i+1}: Press ENTER to play.")
            self.run_player(i)
        cls()
        for i in range(len(self.players)):
            print(f"PLAYER {i+1}: Your circuit is:")
            print(self.players[i].circuit.draw())
            print("")
        input("PLAYERS: Press ENTER to run your circuits on IonQ!\n")
        scores = []
        for i in range(len(self.players)):
            pl = self.players[i]
            print(f"PLAYER {i+1}: Evaluating your circuit...")
            res = pl.run()
            score = sum(res)
            print(f"\nPLAYER {i+1}: Your qubits evaluate to: {res}")
            print(f"PLAYER {i+1}: You receive a score of {score}")
            if score > config.BUST_NUMBER:
                score = -1
                print(f"PLAYER {i+1}: You go bust.")
            scores.append(score)
            print("")
        max_score = max(scores)
        winners = [str(i+1) for i in range(len(self.players)) if scores[i]==max_score]
        print("")
        if len(winners) > 1:
            winners = ' and '.join(winners)
            print(f"WINNERS: PLAYERS {winners}")
        else:
            print(f"WINNER: PLAYER {winners[0]}")
        print("")
        return input("Play again (Y/N)? ").upper() == "Y"
        


