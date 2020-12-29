# Intelligence artificielle
## 1 - Install conda, python, pip

```bash
$ brew install --cask anaconda # for env
```

## 2 - create environment

```bash
$ conda create -n my_env -y
$ conda activate my_env # to activate the environment

$ conda install python=3.7 # add python: 3.7 to ensure everything run ok
$ python -m pip install -r requirements.txt # install all needed dependency

$ conda deactivate # to deactivate

```