# Project: PyDockSwift
PyDockSwift empowers you to kickstart Python projects effortlessly. Seamlessly Dockerized your projects and save valuable time.

## Prerequisites Software
* Java 8
* Python => 3.11.x 

## Local Setup & Run
1. Create Python Virtual environment. Make sure you are using virtualenv belonging to python 3.x.x
``` 
   1. pip install virtualenv
   2. virtualenv venv OR python -m venv venv
```
2. Open Terminal and activate your virtual environment and install external python modules via below command
```
   1. (For Windows):    venv\Scripts\activate
   2. (For mac):        source venv\bin\activate
   3. pip install -r requirements.txt
```
## Build .whl files for distribution
1. Generating .whl files for this python project distribution
   1. `cd <Root directory>`
   2. `python setup.py package`
   3. `This will Generate artifacts under dist/ directory.`
   4. For clean-up : `python setup.py clean` 

## Build Docker Image

This project includes a script `build.sh` that you can use to build a Docker image for this python project.

```
# help
./build.sh -h

# build an image with defaults
./build.sh

# build an image with custom values
./build.sh -r <REGISTRY> -v <VERSION>
```

