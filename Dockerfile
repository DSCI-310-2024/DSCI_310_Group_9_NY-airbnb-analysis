# Start from the Jupyter scipy-notebook as a base
FROM quay.io/jupyter/scipy-notebook:2024-02-24

USER root

# Install  dependencies 
RUN conda install -y \
    python=3.11 \
    ipykernel=6.29.3 \
    jupyterlab=4.1.5 \
    matplotlib=3.8.3 \
    nb_conda_kernels \
    nbconvert=7.16.2 \
    numpy=1.26.4 \
    pandas=2.2.1 \
    pip=23.2.1 \
    scikit-learn=1.4.1.post1 \
    scipy=1.12.0 \
    seaborn=0.13.2 \
    tabulate=0.9.0 \
    vl-convert-python=1.3.0 \
    tabulate=0.9.0 \
    click=8.1.7 \
    make=4.3 \
    jupyter=1.0.0 \
    quarto=1.4.550 \
    iniconfig=2.0.0 \
    pluggy=1.4.0 \
    pytest=8.1.1

RUN pip install pynyairbnb=0.3.0

RUN apt-get update
RUN apt-get install lmodern -y
# RUN tlmgr update --self
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    lmodern \
    && rm -rf /var/lib/apt/lists/*