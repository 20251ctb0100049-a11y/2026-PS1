# conversores/__init__.py
# Expõe a API pública do pacote.


from .temperatura import (
    celsius_para_fahrenheit, celsius_para_kelvin, fahrenheit_para_celsius
)
from .distancia import (
    km_para_milhas, milhas_para_km, metros_para_pes
)
from .massa import (
    kg_para_libras, kg_para_gramas, libras_para_kg
)

__all__ = [
    "celsius_para_fahrenheit", "celsius_para_kelvin", "fahrenheit_para_celsius",
    "km_para_milhas", "milhas_para_km", "metros_para_pes",
    "kg_para_libras", "kg_para_gramas", "libras_para_kg"
]


