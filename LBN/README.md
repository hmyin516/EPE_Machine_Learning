# Lorentz Boost Network
Implementation of the Lorentz Boost Network [paper](https://arxiv.org/pdf/1812.09722.pdf) and [repo](https://github.com/riga/LBN)

## Data files for training
**zenodo**: Raw top tagging data files from the [Top Quark Tagging Reference Dataset](https://zenodo.org/record/2603256)

**five-classifier dataset (with restricted access)**: Raw five classifier datasets from [five-class dataset](https://cernbox.cern.ch/index.php/s/AgzB93y3ac0yuId?path=%2Ffixed)
### Package dependencies
- Python3
- h5py
- numpy
- pandas
- cudatoolkit
- TensorFLow
- torchvision
## Installing LBN and creating an enviroment
Create a conda environment and install necessary packages:
```
create --name=TF2 python=3.6 numpy pandas scipy matplotlib h5py scikit-learn jupyter
conda activate TF2
install keras==2.4.2 tensorflow==2.2.0
conda install tensorflow-gpu
pip install LBN

```
## Top Tagging
The top-tagging `train/LBN_TopTagging.ipynb` is the most complete notebook
## 5-Classifier
Work in progress

