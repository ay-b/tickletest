# Test task 

## Objectives
1. Create a code covered with unit tests
2. Create a container running that code
3. Create a CI pipeline to run the tests with the code updates
4. Create a deployment script using some CD-tool
5. Explain everything

## 1. Code

This is a simpliest «calculator» script written with Python.  
It can add, subtract, multiply and divide num pairs only.  
Absolutely no error handling included. 

## 2. Container

Dockerfile is included in this repo.  
Compile it with `docker build -t test:latest .`

## 3. CI pipeline

Travis CI was used to run tests.  
My own is located here: https://travis-ci.org/ay-b/tickletest

## 4. Deployment

Ansible script can be called with `ansible-playbook deploy.yml` to deploy to localhost

To use the container, use the following commands:
`docker run --rm test:latest add 123456789 987654321`  
`docker run --rm test:latest sub 123456789 987654321`  
`docker run --rm test:latest mul 123456789 987654321`  
`docker run --rm test:latest div 123456789 987654321`  


## 5. Explain everything
See above. 