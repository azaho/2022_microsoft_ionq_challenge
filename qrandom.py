import random
import config
import quantum
from qiskit import QuantumCircuit

def next_int(max_int):
    if config.RNG_BACKEND == "qpu":
        circuit = QuantumCircuit(config.QUBIT_COUNT, config.QUBIT_COUNT)
        for i in range(config.QUBIT_COUNT): circuit.h(i)
        temp = list(range(config.QUBIT_COUNT))
        circuit.measure(temp, temp)
        number = int(quantum.measure(circuit), 2)
        return number % max_int
    return random.randrange(max_int) 
