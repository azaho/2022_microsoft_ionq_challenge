
# Number of algorithmic qubits available for use
QUBIT_COUNT = 8

# Reasonable number of gates to allow players to apply
GATE_COUNT = 2

# How many qubits one drawing will use
DRAW_QUBITS = 2

# ID-symbol maps
ID_TO_SYMBOL = ['0', '1', '+', '-']
SYMBOL_TO_ID = {s:i for i, s in enumerate(ID_TO_SYMBOL)}

# How much is bust
BUST_NUMBER = 5

# using qpu or simulator for circuit computation
BACKEND = "qpu"#"simulator"

# using qpu or prng for random number generation (pick qubit initial state)
# note: can only use qpu here if BACKEND="qpu".
RNG_BACKEND = "prng"
