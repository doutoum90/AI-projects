# Artificial Intelligence 
## 1 - Install conda, python, pip

```bash
$ brew install --cask anaconda # for env
```

## 2 - create environment

```bash
$ conda create -n my_env -y # to create the environment
$ conda activate my_env # to activate the environment
$ conda install python=3.7 # add python: 3.7 to ensure everything run ok
conda install -c conda-forge pydot  graphviz # to enable plot_model of tensorflow
$ python -m pip install -r requirements.txt # install all needed dependency
$ jupyter notebook # lunch jupyter
$ conda deactivate # to deactivate after finishing work
```