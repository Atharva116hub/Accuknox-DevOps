# Wisecow Application

Wisecow is a simple web application that serves "wisdom" using `cowsay` and `fortune`.  
This project demonstrates **containerization, Kubernetes deployment, and CI/CD integration** using AWS ECR and EKS.

---

## Project Structure

wisecow/
├── Dockerfile
├── wisecow.sh
├── k8s/
│ ├── deployment.yaml
│ └── service.yaml
├── .github/
│ └── workflows/
│ └── cicd.yml
├── README.md
└── LICENSE

yaml
Copy code

---

## Prerequisites

- AWS CLI configured with access to your account
- Docker installed
- kubectl installed
- eksctl installed
- Git installed

---

## Setup and Execution

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd wisecow
chmod +x wisecow.sh
2. Build Docker Image
bash
Copy code
docker build -t wisecow .
3. Tag and Push to AWS ECR
bash
Copy code
export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
aws ecr get-login-password --region ap-southeast-2 | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.ap-southeast-2.amazonaws.com
docker tag wisecow:latest $AWS_ACCOUNT_ID.dkr.ecr.ap-southeast-2.amazonaws.com/wisecow:latest
docker push $AWS_ACCOUNT_ID.dkr.ecr.ap-southeast-2.amazonaws.com/wisecow:latest
4. Deploy on Kubernetes (EKS)
Update k8s/deployment.yaml with your ECR image:

yaml
Copy code
image: 924673053488.dkr.ecr.ap-southeast-2.amazonaws.com/wisecow:latest
Apply manifests:

bash
Copy code
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl rollout status deployment/wisecow-deployment
kubectl get pods
kubectl get svc wisecow-service
5. Access the Application
Use the EXTERNAL-IP from the service:

cpp
Copy code
http://<EXTERNAL-IP>
You should see a cowsay-generated wisdom message.

CI/CD
The project includes a GitHub Actions workflow (.github/workflows/cicd.yml) that:

Builds the Docker image on push to main

Pushes the image to AWS ECR

(Optional) Can trigger deployment to Kubernetes

Make sure to configure the GitHub repository secrets:

DOCKER_USERNAME → AWS username (AWS)

DOCKER_PASSWORD → aws ecr get-login-password output

AWS_ACCOUNT_ID → Your AWS account ID

License
This project is licensed under the Apache License 2.0. See LICENSE for details.

yaml
Copy code

---

If you want, I can also **write a complete `cicd.yml` GitHub Actions workflow** that automatically builds, pushes, and updates the deployment on EKS, ready to paste into your repository.  

Do you want me to do that next?
