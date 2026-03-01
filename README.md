# Epigenetics
Epigenetics Project + Lecture Code

OwenCode -> Python code from or refactored from  J. A. Owen et al., Science 382, eadg3053
(2023). DOI: 10.1126/science.adg3053

HistoneCode -> Julia code from Xiangting Li, Tom Chou; Stochastic nucleosome disassembly mediated by remodelers and histone fragmentation. J. Chem. Phys. 28 November 2023; 159 (20): 204107. https://doi.org/10.1063/5.0165136

### Windows Environment Setup
Assumes Python, pip, and condo are already installed.

# Create the environment:
conda create -n epimem python=3.10 -y

conda activate epimem

# Install Libraries:
conda install -y openmm numpy scipy pandas matplotlib tqdm networkx

# Install Git
Confirm its installed:

git --version

# Install Polychrom and EoN using pip
pip install git+https://github.com/open2c/polychrom.git
pip install EoN

# Import Check:
python -c "import openmm; import numpy; import scipy; import matplotlib; import networkx; import EoN; import polychrom; print('ALL IMPORTS OK')"
