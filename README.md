## Python Lambda function on Docker image

* Install docker on your machine if not exists already
* Create the lambda function lambdaDocker.py
* Create the requirments.txt file to install the dependencies in your build
* Create the Dockerfile

### To push the build from local to AWS: 
The following steps worked for me.
1. Create a repository lambdadockerpython in AWS ECR
2. Make sure AWS CLI is connecting from local machine using keyid, access key and token
3. Follow the steps in View push commands once selecting ECR
4. Create a lambda function using the Container image

#### Run Logs: (replacing some docker ids and image to xxx)
(base) PS C:\Users\kamal\PycharmProjects\lambdaDocker> aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin xxx.dkr.ecr.us-east-1.amazonaws.com
Login Succeeded  
(base) PS C:\Users\kamal\PycharmProjects\lambdaDocker> docker build -t lambdadockerpython .  
[+] Building 1.3s (9/9) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                                                                 0.0s 
 => => transferring dockerfile: 32B                                                                                                                                                                                                  0.0s 
 => [internal] load .dockerignore                                                                                                                                                                                                    0.0s 
 => => transferring context: 2B                                                                                                                                                                                                      0.0s 
 => [internal] load metadata for public.ecr.aws/lambda/python:3.8                                                                                                                                                                    1.2s 
 => [internal] load build context                                                                                                                                                                                                    0.0s 
 => CACHED [2/4] COPY requirements.txt ./                                                                                                                                                                                            0.0s 
 => CACHED [3/4] RUN pip3 install -r requirements.txt                                                                                                                                                                                0.0s 
 => CACHED [4/4] COPY lambdaDocker.py ./                                                                                                                                                                                             0.0s 
 => exporting to image                                                                                                                                                                                                               0.0s 
 => => exporting layers                                                                                                                                                                                                              0.0s 
 => => writing image sha256:xxx                                                                                                                                         0.0s 
 => => naming to docker.io/library/lambdadockerpython                                                                                                                                                                                0.0s 

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them  
(base) PS C:\Users\kamal\PycharmProjects\lambdaDocker> docker tag lambdadockerpython:latest xxx.dkr.ecr.us-east-1.amazonaws.com/lambdadockerpython:latest
(base) PS C:\Users\kamal\PycharmProjects\lambdaDocker> docker push xxx.dkr.ecr.us-east-1.amazonaws.com/lambdadockerpython:latest  
The push refers to repository [993818375429.dkr.ecr.us-east-1.amazonaws.com/lambdadockerpython]
4cd5dea7d933: Pushed  
6a8ab05f2fb3: Pushed  
d5b25a877e53: Pushed  
9bf81b2dbdd4: Pushed  
dffe1d92fa26: Pushed  
5f96311c404e: Pushed  
87d111f6565d: Pushed  
007a04e345da: Pushed  
c662e800f5c9: Pushed  
latest: digest: sha256:xx size: 2207  
(base) PS C:\Users\kamal\PycharmProjects\lambdaDocker>   

#### Run log from lambda (replaced request id)
START RequestId: xxx Version: $LATEST  
Sample lambda function with Docker!  
Request json msg: {"message": "lambda from container"}  
END RequestId: xxx  
REPORT RequestId: xxx	Duration: 103.44 ms	Billed Duration: 6488 ms	Memory Size: 128 MB	Max Memory Used: 100 MB	Init Duration: 6383.95 ms  


#### To test it locally
* Docker build command
* `docker build -t lambda-docker . `
* Run the docker container
* `docker run -p 9000:8080 lambda-docker:latest`
* To test the function
* `curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d "{"""message""":"""hello"""}"`


### Reference steps (node.js)
https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/