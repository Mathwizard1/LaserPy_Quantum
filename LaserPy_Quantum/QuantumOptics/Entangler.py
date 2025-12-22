from __future__ import annotations

from numpy import (
    ndarray,
    array
)

ENTANGLEMENT_UPPER_LIMIT = 5

def default_polarization(n: int):
    """:meta private:"""
    return array([1.0 + 0j] + [0.0 + 0j] * ((2 ** n) - 1), dtype=complex)

class QuantumState:
    def __init__(self, photon_ids: tuple[int]) -> None:
        self.num_qubits = len(photon_ids)
        self.photon_ids = photon_ids
        self.global_state: ndarray = default_polarization(self.num_qubits)