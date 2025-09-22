#!/bin/bash
sudo apt-get update -y
sudo apt-get install -y docker.io git curl unzip
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip && sudo ./aws/install
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl && sudo mv kubectl /usr/local/bin/
curl -s https://api.github.com/repos/weaveworks/eksctl/releases/latest | grep browser_download_url | grep linux_amd64 | cut -d '"' -f 4 | wget -qi -
tar -xzf eksctl_*_linux_amd64.tar.gz && sudo mv eksctl /usr/local/bin/
