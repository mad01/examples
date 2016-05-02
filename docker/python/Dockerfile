FROM python:2.7.11

ADD id_rsa_docker /root/.ssh/id_rsa
ADD id_rsa_docker.pub /root/.ssh/id_rsa.pub
RUN echo "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config
RUN chown -R root:root /root/.ssh

WORKDIR /app/test
RUN git clone git@github.com:mad01/examples.git

WORKDIR /app/test/examples/docker/python
RUN pip install -r requirements.txt
