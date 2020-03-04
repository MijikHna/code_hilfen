#### 1 - Install kubectl
1. `curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -`
2. `echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list`
3. `sudo apt-get update`
4. `sudo apt install kubectl`
##### Autokompetion
1. bash: `echo 'source <(kubectl completion bash)' >>~/.bashrc`; zsh: `echo 'source <(kubectl completion zsh)' >>~/.zshrc`
2. `kubectl completion bash >/etc/bash_completion.d/kubectl`

#### 2 - Minicube installieren
1. von hier https://github.com/kubernetes/minikube/releases letztes .deb Package herunterladen und installiren
2. `echo 'source <(minikube completion zsh)' >>~/.zshrc`
3. `minikube start --vm-driver=virtualbox` oder `minikube start`
4. `minikube status`
5. `minikube config set memory 3072`
6. `minikube stop`

#### 3 - Dashboard
1. `minikube dashboard`
