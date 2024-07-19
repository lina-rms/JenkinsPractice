FROM jenkins/jenkins:lts

USER root
RUN apt-get update && apt-get install -y python3 python3-pip

COPY . /var/jenkins_home/workspace

RUN jenkins-plugin-cli --plugins "git pipeline"
