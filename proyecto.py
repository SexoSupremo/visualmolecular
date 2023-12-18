from Bio.PDB import PDBParser
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Proteina:
    def __init__(self, archivo_pdb):
        self.archivo_pdb = archivo_pdb
        self.estructura = Estructura(self.archivo_pdb)
        
class Estructura:
    def __init__(self, archivo_pdb):
        self.archivo_pdb = archivo_pdb
        self.structure = None
        self.parser = Parser()

    def cargar_estructura(self):
        self.structure = self.parser.parsear(self.archivo_pdb)