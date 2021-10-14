![Simple Flask Application CI/CD](https://github.com/n-g-s/simple-app-example/workflows/Simple%20Flask%20Application%20CI/CD/badge.svg)
#### Repository structure
```
.
├── .github
│   └── workflows
│       └── main.yml
├── .gitignore
├── Dockerfile
├── README.md
├── app.py
├── bench_prep.iml
├── deployment
│   ├── k8s-deployment.yml
│   └── k8s-ingress.yml
├── requirements.txt
├── tests
│   ├── integration.py
│   └── unit_test.py
└── timer
    └── timer.py
```
#### Docker Image pull command
`docker pull dhforngs/simple-app-example`

#### GitHub WorkFlow
- ci
    * Lint with flake8
    * Running Unit tests
    * Running Integration tests
- cd
    * If CI flow went good, building the docker image
    * Pushing the docker image to DockerHub


## For Local test
#### Clone repo
`git clone https://github.com/n-g-s/simple-app-example.git`

`cd simple-app`
#### Create virtual environment for python
`python -m venv venv`

`source venv/bin/activate` 

#### Install additional libraries 
`pip install -r requirements.txt`

#### Run Unit and Integration tests
`python -m unittest tests/unit_test.py`

`python -m unittest tests/integration.py`

#### Run application
`python app.py`

## For K8S test
Tested on docker for mac
#### Clone repo
`git clone https://github.com/n-g-s/simple-app-example.git`

`cd simple-app`

#### Apply deployment manifest without Ingress
`kubectl apply -f deployment/k8s-deployment.yml`

#### Enable port forwarding
`kubectl port-forward svc/simple-app-svc 5000:80`

#### Test the simple app
```
 http http://127.0.0.1:5000/status/ready
 HTTP/1.0 200 OK
 Content-Length: 15
 Content-Type: application/json
 Date: Wed, 29 Jan 2020 08:44:47 GMT
 Server: Werkzeug/0.16.1 Python/3.8.1
 
 {
     "ready": true
 }
```
#### If you have ingress apply ingress for a simple app
`kubectl apply -f deployment/k8s-ingress.yml`

#### Test the simple app via ingress
``` 
http http://bench.kubernetes.docker.internal/status/ready

HTTP/1.1 500 INTERNAL SERVER ERROR
Connection: keep-alive
Content-Length: 16
Content-Type: application/json
Date: Wed, 29 Jan 2020 08:50:25 GMT
Server: nginx/1.17.7

{
    "ready": false
}
```
```
http http://bench.kubernetes.docker.internal/status/ready
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 15
Content-Type: application/json
Date: Wed, 29 Jan 2020 08:50:39 GMT
Server: nginx/1.17.7

{
    "ready": true
}
```
