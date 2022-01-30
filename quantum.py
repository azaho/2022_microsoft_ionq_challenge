from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from azure.quantum.qiskit import AzureQuantumProvider
import config
import random

from azure.quantum.qiskit import AzureQuantumProvider
provider = AzureQuantumProvider (
    resource_id = "/subscriptions/b1d7f7f8-743f-458e-b3a0-3e09734d716d/resourceGroups/aq-hackathons/providers/Microsoft.Quantum/Workspaces/aq-hackathon-01",
    location = "eastus"
)


simulator_backend = provider.get_backend("ionq.simulator")
qpu_backend = provider.get_backend("ionq.qpu")


def measure(circuit):
    if config.BACKEND == "simulator":
        job = simulator_backend.run(circuit, shots = 1)
        result = job.result()
        probabilities = result.data()["probabilities"]
    if config.BACKEND == "qpu":
        job = qpu_backend.run(circuit, shots = 1)
        result = job.result()
        probabilities = result.get_counts(circuit)
    #print(probabilities)
    return random.choices(list(probabilities.keys()), list(probabilities.values()))[0]


if __name__=="__main__":
    circuit = QuantumCircuit(3, 3)
    circuit.name = "3-qubit GHZ circuit"
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.x(2)
    circuit.measure([0, 1, 2], [0, 1, 2])
    print(measure(circuit))
