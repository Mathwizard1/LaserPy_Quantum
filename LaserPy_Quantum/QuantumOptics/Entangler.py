from __future__ import annotations

from numpy import (
    array
)

ENTANGLEMENT_UPPER_LIMIT = 5

class QuantumEntangler:
    def __init__(self, photons: tuple[Photon,...]) -> None:
        self.photons: tuple[Photon,...] = photons
        self.quantum_state = QuantumState(len(photons))

    def __repr__(self) -> str:
        string = ""
        for photon in self.photons:
            string += str(photon) + "\n"
        string += "Quantum State:\n" + str(self.quantum_state)
        return string
    
    def __add__(self, other: QuantumEntangler) -> QuantumEntangler:
        photons = self.photons + other.photons
        
        # TODO Quantum state maths
        result = QuantumEntangler(photons)
        result.quantum_state = self.quantum_state + other.quantum_state
        return result

    def set_quantum_state(self, quantum_state: QuantumState):
        self.quantum_state = quantum_state

class QuantumState:
    def __init__(self, n: int = 1) -> None:
        self.state = array([1.0 + 0j] + [0.0 + 0j] * ((2 ** n) - 1), dtype=complex)

    def __add__(self, other: QuantumState) -> QuantumState:
        result = QuantumState()
        return result

from ..Photon import Photon