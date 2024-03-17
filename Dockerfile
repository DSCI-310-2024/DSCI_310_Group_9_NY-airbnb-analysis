# Start from the Jupyter scipy-notebook as a base
FROM quay.io/jupyter/scipy-notebook:2024-02-24

# Install dependencies from your environment.yml
COPY environment.yml /tmp/environment.yml
RUN conda env update --name base --file /tmp/environment.yml && \
    conda clean --all -f -y

# Install additional dependencies not covered by environment.yml
RUN conda install -y \
    pytest=8.1.1 \
    vl-convert-python=1.3.0 \
    tabulate=0.9.0 \
    click=8.1.7 && \
    conda clean --all -f -y

# Make sure pip is up to date
RUN pip install --upgrade pip

# Copy the contents of the project into the container
COPY . /home/jovyan/work

# Expose the port Jupyter Notebook runs on
EXPOSE 8888

# Start Jupyter Notebook
CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''"]
