# Start from the Jupyter scipy-notebook as a base
FROM quay.io/jupyter/scipy-notebook:2024-02-24

# Switch to root to install system dependencies
USER root

# Install system dependencies required for Quarto and other operations
RUN apt-get update && apt-get install -y \
    make \
    gdebi-core \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Quarto
ARG QUARTO_VERSION="1.4.537"
RUN curl -o quarto-linux-arm64.deb -L https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-arm64.deb && \
    gdebi --non-interactive quarto-linux-arm64.deb && \
    rm quarto-linux-arm64.deb

# Switch back to the jovyan user to perform operations that don't require root
USER ${NB_UID}

# Copy the environment.yml into the container to update the base environment
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

# Start Jupyter Notebook with no token or password for simplicity
# Note: Consider the security implications of this approach for your use case
CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''"]
