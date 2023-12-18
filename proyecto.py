from Bio.PDB import PDBParser
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Cargar la estructura de la proteína desde un archivo PDB
parser = PDBParser()
structure = parser.get_structure('mi_proteina', 'C:\\DATABASE\\Universidad Comunera\\Programación 2\\Programación\\messi\\8f48.pdb')