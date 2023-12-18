from Bio.PDB import PDBParser
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Cargar la estructura de la proteína desde un archivo PDB
parser = PDBParser()
structure = parser.get_structure('mi_proteina', 'C:\\DATABASE\\Universidad Comunera\\Programación 2\\Programación\\messi\\8f48.pdb')

# Crear una lista para almacenar las coordenadas de los átomos
atom_coords = []

# Iterar sobre todos los átomos en la estructura
for model in structure:
    for chain in model:
        for residue in chain:
            for atom in residue:
                # Añadir las coordenadas del átomo a la lista
                atom_coords.append(atom.get_coord())