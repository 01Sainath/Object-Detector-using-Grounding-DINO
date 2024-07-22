# Object Detector using Grounding DINO

## Introduction
This project demonstrates the use of the Grounding DINO model for object 
detection tasks. Grounding DINO is a state-of-the-art open-set object detection model designed to 
accurately detect objects in images with high precision. This repository 
provides an easy-to-use interface for running the model on your own images.

## Features
- Easy to use : You just have to follow the steps given below in Installation and Usage section
- High Accuracy : Utilizes Grounding DINO's advanced architecture for precise object detection.
- Customizable : Can be customized for detecting any arbritary objects.
- Easy Integration: Simple API for integrating the model into your applications.

## Installations

1. Python version = Python 3.12.4
2. Create a python project and clone this repository inside that:

    ```bash
    git clone https://github.com/01Sainath/Object-Detector-using-Grounding-DINO.git
    ```

3. Install all the dependencies specified in the requirements.txt file, for example
   ```bash
    pip install torch
    pip install torchvision
    etc
    ```
4. Install fastapi
    ```bash
    pip install fastapi
    ```
5. Create a directory named weights inside the cloned repository
6. Paste the following url in browser and "groundingdino_swint_ogc.pth" this
   file will be downloaded put that file in weights directory.
   ```bash
    https://github.com/IDEA-Research/GroundingDINO/releases/download/v0.1.0-alpha/groundingdino_swint_ogc.pth
    ```

## Usage

1. Open the terminal and jump to the directory where the main.py is then run the following command.
    ```bash
    fastapi dev main.py
    ```
2. Then boom the api is ready to use into your applications. Just dont forget to send an image when you hit the api-endpoint.
3. A sample webpage is there in the repository in "Basic_Html_Page" directory.

## Thank you 
