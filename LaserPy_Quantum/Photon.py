from __future__ import annotations

from dataclasses import dataclass

from numpy import (
    dtype, object_,
    angle, abs
)

from .QuantumOptics.Entangler import QuantumState

from .Constants import ERR_TOLERANCE

""" Photon dtype for Photon class"""
Photon_dtype = dtype([
    ('field', complex),
    ('frequency', float),
    ('photon_number', float),
    ('source_phase', float),
    ('photon_id', int),
    ('quantum_state', object_) # For simplicity, store the Python object
])

@dataclass(slots= True)
class Photon:
    """
    Photon class.
    """
    # Microscopic parameters 
    field: complex
    frequency: float

    # Macroscopic parameters
    photon_number: float = ERR_TOLERANCE
    source_phase: float = ERR_TOLERANCE

    # Quantum parameters
    photon_id: int = -1
    quantum_state: QuantumState|None = None

    @classmethod
    def from_photon(cls, other: Photon) -> Photon:
        """Photon classmethod from photon constructor"""
        photon = cls.__new__(cls)
        photon.field = other.field
        photon.frequency = other.frequency

        photon.photon_number = other.photon_number
        photon.source_phase = other.source_phase

        photon.photon_id = other.photon_id
        photon.quantum_state = other.quantum_state
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

Empty_Photon = Photon(ERR_TOLERANCE + 0j, ERR_TOLERANCE)