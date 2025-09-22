#!/bin/bash
REGION=ap-southeast-2
CLUSTER_NAME=wisecow-cluster
REPO=wisecow
kubectl delete -f k8s/deployment.yaml
kubectl delete -f k8s/service.yaml
eksctl delete cluster --name $CLUSTER_NAME --region $REGION
aws ecr delete-repository --repository-name $REPO --region $REGION --force
