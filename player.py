import qrandom
import quantum
import config
from qiskit import QuantumCircuit


class Player:
    def __init__(self):
        self.cards = []
        self.cards_len = 0
        self.gates_applied = 0
    
    def _build_qubits(self, show_classical_register=False):
        if show_classical_register:
            self.circuit = QuantumCircuit(self.cards_len, self.cards_len)
        else:
            self.circuit = QuantumCircuit(self.cards_len)
        for i in range(self.cards_len):
            r = self.cards[i]
            # apply X?
            if r % 2 == 1:
                self.circuit.x(i)
            # apply H?
            if r // 2 == 1:
                self.circuit.h(i)

    def _draw_one(self):
        r = qrandom.next_int(4)
        self.cards.append(r)
        self.cards_len += 1
        self._build_qubits()
        return config.ID_TO_SYMBOL[self.cards[-1]]

    def can_draw(self):
        return config.QUBIT_COUNT - self.cards_len >= config.DRAW_QUBITS

    def draw(self):
        if not self.can_draw():
            raise Exception("Not enough qubits to draw more")
        res = []
        for i in range(config.DRAW_QUBITS):
            res.append(self._draw_one())
        return res

    def finish_drawing(self):
        self._build_qubits(show_classical_register=True)

    def can_apply_gate(self):
        return config.GATE_COUNT - self.gates_applied > 0

    def apply_gate(self, gate, q_a, q_b):
        self.gates_applied += 1
        if gate == 'CNOT':
            self.circuit.cx(q_a, q_b)
        else:
            self.gates_applied -= 1
            raise Exception(f"Gate not supported: {gate}")

    def finish_applying_gates(self):
        temp = list(range(self.cards_len))
        self.circuit.measure(temp, temp)

    def run(self):
        res = [int(i) for i in quantum.measure(self.circuit)]
        res.reverse()
        return res
