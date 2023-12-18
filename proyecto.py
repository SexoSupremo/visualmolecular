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

class Parser:
    def __init__(self):
        pass

    def parsear(self, archivo_pdb):
        parser = PDBParser()
        return parser.get_structure('mi_proteina', archivo_pdb)

class Coordenadas:
    def __init__(self, structure):
        self.structure = structure
        self.atom_coords = []

    def obtener_coordenadas(self):
        for model in self.structure:
            for chain in model:
                for residue in chain:
                    for atom in residue:
                        self.atom_coords.append(atom.get_coord())
        self.atom_coords = np.array(self.atom_coords)
        
class Visualizador:
    def __init__(self, atom_coords):
        self.atom_coords = atom_coords

    def dibujar(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = self.atom_coords[:,0]
        y = self.atom_coords[:,1]
        z = self.atom_coords[:,2]
        ax.scatter(x, y, z)
        plt.show()

# Crear una instancia de la clase Proteina
proteina = Proteina('C:\\DATABASE\\Universidad Comunera\\Programación 2\\Programación\\messi\\8f48.pdb')

# Cargar la estructura de la proteína
proteina.estructura.cargar_estructura()

# Crear una instancia de la clase Coordenadas
coordenadas = Coordenadas(proteina.estructura.structure)

# Obtener las coordenadas de los átomos
coordenadas.obtener_coordenadas()