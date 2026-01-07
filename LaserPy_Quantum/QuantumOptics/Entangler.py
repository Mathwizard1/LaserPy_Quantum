from __future__ import annotations

from numpy import (
    array, 
    zeros
)

class QuantumEntangler:
    def __init__(self, photons: tuple[Photon,...]) -> None:
        self.photons: tuple[Photon,...] = photons
        self.quantum_state = QuantumState(len(photons))

    def __repr__(self) -> str:
        string = "QuantumEntangler:\n"
        for photon in self.photons:
            string += f"photon:{id(photon)}\n"
        string += str(self.quantum_state)
        return string
    
    def __add__(self, other: QuantumEntangler) -> QuantumEntangler:
        if not set(self.photons).isdisjoint(other.photons):
            print("System's are already entangled.\n")
            return self

        photons = self.photons + other.photons
        result = QuantumEntangler(photons)
        result.quantum_state = self.quantum_state + other.quantum_state
        return result

    def sync_qubits(self):
        for photon in self.photons:
            photon.quantum_entangler = self

    # def __del__(self):
    #     print(f"DEBUG: QuantumEntangler at {id(self)} has been destroyed.")

class QuantumState:
    def __init__(self, n: int = 1, zfill = False) -> None:
        self.n_qubits = n
        
        if zfill:
            self._state = zeros((1 << n), dtype= complex)
        else:
            self._state = array([1.0 + 0j] + [0.0 + 0j] * ((1 << n) - 1), dtype=complex)

    def __repr__(self) -> str:
        return f"QuantumState({self.n_qubits} qubits:\n" + str(self._state) + ")\n"

    def __add__(self, other: QuantumState) -> QuantumState:
        n_A = self.n_qubits
        n_B = other.n_qubits
        n_merged = n_A + n_B

        mask_A = (1 << n_A) - 1
        mask_B = (1 << n_B) - 1

        result = QuantumState(n_merged, zfill= True)
        for i_merged in range(n_merged):
            i_A = i_merged & mask_A
            i_B = (i_merged >> n_A) & mask_B
            result._state[i_merged] = self._state[i_A] * other._state[i_B]

        return result

from ..Photon import Photon