# Importar los modulos necesarios "numpy" para las operaciones numericas, matplotlib para graficar y mpl_toolkits para graficar en 3D
from Bio.PDB import PDBParser
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definimos la clase Proteina, 
class Proteina:
    def __init__(self, archivo_pdb):
        self.archivo_pdb = archivo_pdb  # Archivo PDB de la proteína
        self.estructura = Estructura(self.archivo_pdb)  # Estructura de la proteína
#Init es un constructor que se llama cuando se crea un objeto de esta clase e inicializa los atributos ar y estructura

# Definimos la clase Estructura
class Estructura:
    def __init__(self, archivo_pdb):
        self.archivo_pdb = archivo_pdb  # Archivo PDB de la proteína
        self.structure = None  # Estructura de la proteína
        self.parser = Parser()  # Parser para leer el archivo PDB
#Aca el metodo init inicia los atributos archivo_pdb,structure y parser
    
    def cargar_estructura(self):
        self.structure = self.parser.parsear(self.archivo_pdb)
     # Método para cargar la estructura de la proteína

# Definimos la clase Parser
class Parser:
    def __init__(self):
        pass
   
    # Método para parsear el archivo PDB y obtener la estructura de la proteína
    def parsear(self, archivo_pdb):
        parser = PDBParser()
        return parser.get_structure('mi_proteina', archivo_pdb)

# Definimos la clase Coordenadas
class Coordenadas:
    def __init__(self, structure): #Init inicia los atributos de abajo
        self.structure = structure  # Estructura de la proteína
        self.atom_coords = []  # Coordenadas de los átomos de la proteína

    #itera sobre structure do proteína y obtiene coords de cada átomo y almacena en  para obtener las coordenadas de los átomos de la proteína
    def obtener_coordenadas(self):
        for model in self.structure:
            for chain in model:
                for residue in chain:
                    for atom in residue:
                        self.atom_coords.append(atom.get_coord()) 
        self.atom_coords = np.array(self.atom_coords)
#Se almacena las coordenadas de cada atomo

# Definimos la clase Visualizador
class Visualizador:
    def __init__(self, atom_coords):
        self.atom_coords = atom_coords  # Coordenadas de los átomos de la proteína

    # Método para dibujar la proteína
    def dibujar(self):
        fig = plt.figure()#crea una nueva figura en la que se dibuja el grafico
        ax = fig.add_subplot(111, projection='3d')#la figura se divide en una cuadrícula de 1 fila y 1 columna.
        x = self.atom_coords[:,0] #es un array de NumPy que contiene las coordenadas de todos los átomo
        y = self.atom_coords[:,1] #se extraen las coordenadas x, y, z de cada átomo de la proteína. 
        z = self.atom_coords[:,2]
        ax.scatter(x, y, z)#Esta línea crea un gráfico de dispersión 3D en el subplot utilizando las coordenadas de los átomos.
        plt.show()
        #se muestra el grafico

# Creamos una instancia de la clase Proteina
proteina = Proteina('C:\\DATABASE\\Universidad Comunera\\Programación 2\\Programación\Github\\visualmolecular\\visualmolecular\\8f48.pdb')

# Cargamos la estructura de la proteína
proteina.estructura.cargar_estructura()

# Creamos una instancia de la clase Coordenadas
coordenadas = Coordenadas(proteina.estructura.structure)

# Obtenemos las coordenadas de los átomos
coordenadas.obtener_coordenadas()

# Creamos una instancia de la clase Visualizador
visualizador = Visualizador(coordenadas.atom_coords)

# Dibujamos la proteína
visualizador.dibujar()

# Observación: PDBConstructionWarning: WARNING: Chain A is discontinuous at line 5956: 
# Esta advertencia se produce cuando la biblioteca Bio.PDB encuentra una discontinuidad en la cadena de la proteína. 
# Esto es bastante común ya que muchos archivos PDB contienen errores o discontinuidades. 
# En este caso, se ha ignorado el problema para facilitar la visualización.

