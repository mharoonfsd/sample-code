
# We will use Ubuntu for our image
FROM ubuntu:18.04

# Updating Ubuntu packages
RUN apt-get update 

# Adding wget and bzip2
RUN apt-get install -y wget bzip2

# Add sudo
RUN apt-get -y install sudo

# Add user ubuntu with no password, add to sudo group
RUN adduser --disabled-password --gecos '' ubuntu
RUN adduser ubuntu sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ubuntu
WORKDIR /home/ubuntu/
RUN chmod a+rwx /home/ubuntu/

# Miniconda installing
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py37_4.8.3-Linux-x86_64.sh
RUN bash Miniconda3-py37_4.8.3-Linux-x86_64.sh -b
RUN rm Miniconda3-py37_4.8.3-Linux-x86_64.sh

# Set path to conda
ENV PATH /home/ubuntu/miniconda3/bin:$PATH
ENV DEBUG 1
ENV SECRET_KEY 't+@9v3qe3-q^gy^^k0&@@_k%zlr+vanvu_)*^q3)3_ny2mku%2'

# Updating Miniconda packages
RUN conda update conda
# RUN conda update anaconda
# RUN conda update --all

# Initiate BASH Shell for conda
RUN conda init bash

# Create and set working directory
RUN mkdir library
WORKDIR /home/ubuntu/library

# Add currentdirectory code to working directory
ADD . /home/ubuntu/library

# Install MySQL Client Dev package for mysql connectivity
RUN sudo apt-get install -y build-essential python3.6-dev default-libmysqlclient-dev libmysqlclient-dev

# Create Environment
RUN conda env create --file environment.yml

# Activate the environment
RUN activate libraryenv

# Install Requirements
RUN pip install -r requirements.txt

# Collect Static Files
RUN python manage.py collectstatic --noinput

# Setup Debugger
CMD python3 -m ptvsd --host 0.0.0.0 --port 5000 --wait --multiprocess -m gunicorn library.wsgi:application --bind 0.0.0.0:8080

# Expose Port for Django
EXPOSE 8080
