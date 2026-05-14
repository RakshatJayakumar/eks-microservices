# EKS Kubernetes Microservices

## Overview
Two-microservice application deployed on AWS EKS (Elastic Kubernetes Service)
demonstrating container orchestration, service discovery, and horizontal auto-scaling.

## Architecture
LoadBalancer
↓
flask-app (port 5000)
↓
worker-service (port 5001)

## Tech Stack
- Python / Flask
- Docker
- Kubernetes (AWS EKS)
- AWS ECR (container registry)
- Horizontal Pod Autoscaler (HPA)

## Kubernetes Resources
- Deployments for both microservices
- ClusterIP service for worker-service
- LoadBalancer service for flask-app
- ConfigMap for environment configuration
- HPA scaling between 1-5 replicas at 70% CPU

## Project Structure
eks-microservices/
├── flask-app/
│   ├── app/main.py
│   ├── Dockerfile
│   └── requirements.txt
├── worker-service/
│   ├── app/main.py
│   ├── Dockerfile
│   └── requirements.txt
└── k8s/
    ├── configmap.yaml
    ├── flask-app-deployment.yaml
    ├── worker-deployment.yaml
    └── hpa.yaml

## Endpoints
- GET / — Service health and version
- GET /health — Liveness probe endpoint
- GET /data — Fetches processed data from worker-service

## Deployment
# Create EKS cluster
eksctl create cluster --name rakshat-eks-cluster --region eu-west-1 \
  --nodegroup-name workers-small --node-type t3.small --nodes 2 --managed

# Apply manifests
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/flask-app-deployment.yaml
kubectl apply -f k8s/worker-deployment.yaml
kubectl apply -f k8s/hpa.yaml

# Check status
kubectl get pods
kubectl get services

## Destroy
eksctl delete cluster --name rakshat-eks-cluster --region eu-west-1