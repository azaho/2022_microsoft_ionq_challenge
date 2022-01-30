# QUACKJACK: Quantum Blackjack

![QUACKJACK](https://media.discordapp.net/attachments/479732598294315010/937288959598411826/unknown.png)
QUACKJACK is as much an educational tool as it is a fun game: players are able to create and see the actual circuits being run on the quantum computer.

## Description
Welcome to the future: Quantum Gambling with QUACKJACK!

In this game, player's goal is to manipulate their quantum circuit to get more points than the opponent, but not go bust.

On their turn, a player can either draw two more qubits or create entanglement by placing a Controlled-NOT gate in their circuit.

Drawn qubits will become one of the following states at random:

    [0] A qubit with pure 0 value
    
    [1] A qubit with pure 1 value (equivalently, an X gate will be added to it)
    
    [+] In superposition of 0 and 1: (|0> + |1>)/sqrt(2) (equivalently, an H gate will be added)
    
    [-] In superposition of 0 and 1: (|0> - |1>)/sqrt(2) (equivalently, X and H gates will be added).
    
A Controlled-NOT gate from qubit A to B works as follows:

    - If A is 0, then B will be left unchanged
    
    - If A is 1, then B will be inverted.
    
When all qubits are drawn and all gates are placed, the circuit will be run on an IonQ quantum computer. In the end, all qubits will be classically measured, and player's score will be the sum of qubits' values.

Player will go bust if their score ends up being more than 5.

Of the players who did not go bust, the player with the highest score wins the bets.



CONFIGURATION:

    - Maximum number of qubits you can draw: 8
    
    - Maximum number of gates you can apply: 2
    
    - Qubits have to be drawn at once: 2
    
    - Player will go bust if they have more than: 5
    
## How to run
After installing the dependencies (from requirements.txt), the game can be started by running main.py:

    python main.py
    
## iQuHACK 2022 - Thank You!

<p align="left">
  <a href="https://azure.microsoft.com/en-us/solutions/quantum-computing/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151488491-609828a4-cd1f-4076-b5b2-a8d9fc2d0fa4.png" width="30%"/> </a>
  <a href="https://ionq.com/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151488159-da95eb05-9277-4abe-b1ba-b49871d563ed.svg" width="20%" style="padding: 1%;padding-left: 5%"/></a>
  <a href="https://iquhack.mit.edu/" target="_blank"><img src="https://user-images.githubusercontent.com/10100490/151647370-d161d5b5-119c-4db9-898e-cfb1745a8310.png" width="8%" style="padding-left: 5%"/> </a>
  
</p>
For our team, iQuHACK was a great way to end our first month of studying quantum computation in 6.S089 at MIT. During the Hackathon we were able to use our creativity, apply what we've learned in the class and acquire new skills (most of us used GitHub for the first time). We are thankful to the organizers and sponsors of the event for this opportunity.
    
