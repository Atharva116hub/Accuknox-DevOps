#!/bin/bash
REGION=ap-southeast-2
REPO=wisecow
IMAGE_TAG=latest
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
ECR_URI=$AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPO:$IMAGE_TAG
aws ecr describe-repositories --repository-names $REPO --region $REGION >/dev/null 2>&1 || aws ecr create-repository --repository-name $REPO --region $REGION
docker build -t $ECR_URI .
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com
docker push $ECR_URI
