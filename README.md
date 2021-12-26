# Solution


First Question:

Used Keras for getting the model architecture of VGG19. Used cosine similarity to get similarity score between two images. Used Fastapi to deploy two model and swagger ui ti check the results. 
Created Docker image 

    FROM python:3.8-slim-buster

    WORKDIR /app

    COPY requirements.txt requirements.txt
    RUN pip3 install -r requirements.txt

    COPY . .
    EXPOSE 8000
    ENTRYPOINT [ "python3", "main.py"]


Auto Scaling:

Once we create container ,we can port it to any platform (Cloud, Kuberenetes, OnPrem, Docker-Compose). In case of Kubernetes , we can autoscale pods(container) depending upon its workload. This can be acieved using either Horizontal Pod Autoscaler (HPA) or Vertical Pod Autoscaler (VPA). HPA would auto scale the pods across different nodes in cluster. VPA would autoscale the pods within a worker node of Kubernetes cluster Lets consider we are using HPA. HPA monitors the metrics across all pods of a deployment. If the metrics indicate that the target threshold is breached, HPA sends a “Scale” request to the Kubernetes Master component. Kubernetes Master then scales out (or in) replicas as per the HPA re


Second Question:

Used Sentence Transformer to compute embeddings for the given dataset and for the input query. By using Retrain and Retrieval we can improve the results (Cross Encoder), this can score the relevancy of all docs based on the input query. Used Fastapi to deploy the code.


