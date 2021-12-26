# Solution


First Question:

Used Keras for getting the model architecture of VGG19. Used cosine similarity to get similarity score between two images. Used Fastapi to deploy two model and swagger ui ti check the results. 

run command: uvicorn main:application --reload 

![image](https://user-images.githubusercontent.com/73247157/147416128-77956a98-042a-4105-b404-e9babb15b57c.png)


<img width="1246" alt="Screenshot 2021-12-26 at 11 28 53 PM" src="https://user-images.githubusercontent.com/73247157/147416365-00d48a41-7c77-4c9b-a189-a31fe8943e02.png">



Created Docker image 

    FROM python:3.8-slim-buster

    WORKDIR /app

    COPY requirements.txt requirements.txt
    RUN pip3 install -r requirements.txt

    COPY . .
    EXPOSE 8000
    ENTRYPOINT [ "python3", "main.py"]


Auto Scaling:

Once we create container ,we can port it to any platform (Cloud, Kuberenetes, OnPrem, Docker-Compose). In case of Kubernetes , we can autoscale pods(container) depending upon its workload. This can be acieved using either Horizontal Pod Autoscaler (HPA) or Vertical Pod Autoscaler (VPA). HPA would auto scale the pods across different nodes in cluster. VPA would autoscale the pods within a worker node of Kubernetes cluster Lets consider we are using HPA. HPA monitors the metrics across all pods of a deployment. If the metrics indicate that the target threshold is breached, HPA sends a “Scale” request to the Kubernetes Master component. Kubernetes Master then scales out (or in) replicas as per the HPA request.


Second Question:

Used Sentence Transformer to compute embeddings for the given dataset and for the input query. By using Retrain and Retrieval we can improve the results (Cross Encoder), this can score the relevancy of all docs based on the input query. Used Fastapi to deploy the code.

run command : uvicorn smain:application --reload



<img width="1240" alt="Screenshot 2021-12-26 at 10 44 23 PM" src="https://user-images.githubusercontent.com/73247157/147415984-4a8a1166-859d-4e92-960f-d4ede91b32df.png">
<img width="1146" alt="Screenshot 2021-12-26 at 10 43 50 PM" src="https://user-images.githubusercontent.com/73247157/147415985-9bc83019-3c3c-42db-82b0-65fb51e1297c.png">



