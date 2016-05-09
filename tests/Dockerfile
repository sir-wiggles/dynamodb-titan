FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y ipython python-pip curl
RUN pip install boto bulbs

WORKDIR "/root"

ENTRYPOINT ["/bin/bash"]
