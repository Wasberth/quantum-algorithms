import numpy as np
from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import json

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.h(1)
circuit.draw("mpl")

backend = Aer.get_backend('statevector_simulator')
compiled = transpile(circuit, backend)

job = backend.run(compiled, shots=1024)
result = job.result()

counts = result.get_counts()
plot_histogram(counts)

print(json.dumps(counts, indent=4))