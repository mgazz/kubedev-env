
Development workflow for python applications in Kubernetes using Visual Studio Code

### Setup dev env

```
pipenv --python 3
pipenv shell
pipenv install -r requirements.txt
```

### Deploy etcd
```
helm install test bitnami/etcd -f config/etcd/values.yaml
```

### Setup telepresence (from example)
```
sudo -E kubefwd services -n annex-system -m 1234:1234
curl -s https://packagecloud.io/install/repositories/datawireio/telepresence/script.deb.sh | sudo bash
sudo apt install --no-install-recommends telepresence
kubectl create deployment hello-world --image=datawire/hello-world
kubectl expose deployment hello-world --type=LoadBalancer --port=8000
telepresence --swap-deployment hello-world --expose 8000
```

### Start debugging

```
# export setup variables
source .env.sh 
# start debugger at port 5678
./start_debug.sh 5678
```

Launch `Attach` debugger confiugration


Test trigger from inside the cluster:
```
kubectl apply -f ubuntu.yaml
kubectl exec -it ubuntu -- /bin/bash 
curl hello-world:8000
```

