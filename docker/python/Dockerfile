FROM python:2.7.11

ADD id_rsa /root/.ssh/id_rsa
ADD id_rsa.pub /root/.ssh/id_rsa.pub
RUN echo "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config
RUN chown -R root:root /root/.ssh

RUN git config --global user.name "Jenkins"
RUN git config --global user.email jenkins@example.com
RUN git config --global push.default simple 

WORKDIR /app/test
RUN git clone git@github.com:mad01/examples.git

WORKDIR /app/test/examples/docker/python
RUN pip install -r requirements.txt
