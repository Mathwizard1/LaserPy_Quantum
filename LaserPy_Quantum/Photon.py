from __future__ import annotations

from dataclasses import dataclass

from numpy import (
    dtype, object_,
    angle, abs
)

from .Constants import ERR_TOLERANCE

""" Photon dtype for Photon class"""
Photon_dtype = dtype([
    ('field', complex),
    ('frequency', float),
    ('photon_number', float),
    ('source_phase', float),
    ('quantum_entangler', object_) # For simplicity, store the Python object
])

@dataclass(slots= True)
class Photon:
    """
    Photon class.
    """
    # Microscopic parameters 
    field: complex = ERR_TOLERANCE + 0j
    frequency: float = ERR_TOLERANCE

    # Macroscopic parameters
    photon_number: float = ERR_TOLERANCE
    source_phase: float = ERR_TOLERANCE

    # Quantum parameters
    quantum_entangler: QuantumEntangler|None = None

    # Allowing id based-hashing
    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return self is other

    @classmethod
    def from_photon(cls, other: Photon) -> Photon:
        """Photon classmethod from photon constructor"""
        photon = cls.__new__(cls)
        photon.field = other.field
        photon.frequency = other.frequency

        photon.photon_number = other.photon_number
        photon.source_phase = other.source_phase

        photon.quantum_entangler = other.quantum_entangler
        return photon

    @property
    def amplitude(self) -> float:
        """amplitude (V/m) of the field"""
        return abs(self.field)

    @property
    def phase(self) -> float:
        """phase (rad) of the field"""
        return float(angle(self.field))

    def __repr__(self):
        return (f"Photon(ω={self.frequency:.4e}rad/s, |E|={self.amplitude:.4e}V/m, φ={self.phase:.2f}rad)")

    def set_qubit(self):
        if(not self.quantum_entangler):
            self.quantum_entangler = QuantumEntangler((self,))
        return self.quantum_entangler
Empty_Photon = Photon()

from .QuantumOptics.Entangler import QuantumEntangler