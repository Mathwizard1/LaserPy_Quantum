import gc

from LaserPy_Quantum import Photon
from LaserPy_Quantum.QuantumOptics.Entangler import QuantumEntangler

# gc.set_debug(gc.DEBUG_COLLECTABLE)

A = Photon()
B = Photon()

QE = QuantumEntangler((A, B))
# A.quantum_entangler = QE_AB
# B.quantum_entangler = QE_AB
QE.sync_qubits()

print(A.quantum_entangler)

C = Photon()

QE = QE + C.set_qubit()
QE.sync_qubits()

gc.collect()

print(C.quantum_entangler)

