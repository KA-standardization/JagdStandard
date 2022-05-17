FROM centos:7

COPY . /usr/local/hello.py
COPY pip.conf /root/.pip/pip.conf

RUN yum -y install wget

CMD mv /etc/yum.repos.d/CentOS-Linux-BaseOS.repo /etc/yum.repos.d/CentOS-Linux-BaseOS.repo.bak
CMD wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
CMD mv /etc/yum.repos.d/CentOS-Base.repo CentOS-Linux-BaseOS.repo

RUN yum clean all&&yum makecache
RUN yum -y install python3
RUN yum -y install python3-devel
RUN yum -y install gcc
RUN yum -y install gcc-c++
RUN yum -y install mpich-3.2-devel.x86_64


RUN python3 -m pip install --upgrade pip
RUN pip3 install mpi4py

ENV MYPATH /usr/local
WORKDIR $MYPATH

ENV PATH $PATH:/usr/lib64/mpich-3.2/bin

CMD /bin/bash