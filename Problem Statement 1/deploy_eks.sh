#!/bin/bash
REGION=ap-southeast-2
CLUSTER_NAME=wisecow-cluster
eksctl create cluster --name $CLUSTER_NAME --region $REGION --nodes 2 --node-type t3.medium
aws eks --region $REGION update-kubeconfig --name $CLUSTER_NAME
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
