#Base Image
FROM centos:latest

# Working Directory
WORKDIR /

# Install Python and Ncurses packages
RUN yum install python3 ncurses -y

# Install figlet
RUN yum install https://download-ib01.fedoraproject.org/pub/epel/7/x86_64/Packages/f/figlet-2.2.5-9.el7.x86_64.rpm -y

# Install sklearn library
RUN pip3 install sklearn

# Copy pre trained model and prediction code
COPY salary.* /

# Default executable command for image
CMD [ "/bin/python3", "salary.py" ]