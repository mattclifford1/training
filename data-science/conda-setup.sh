
#!/bin/bash

# =========== Python ===============
# make sure conda is accessable
CONDA_BASE=$(conda info --base)
source $CONDA_BASE/etc/profile.d/conda.sh

# create virtual env
VENV=data-science
conda create -n $VENV python=3.8
conda activate $VENV

# install dependancies
pip install --upgrade pip
pip install -r requirements.txt
