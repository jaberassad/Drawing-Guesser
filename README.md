# QuickDraw Neural Network Training and Tkinter App

## Overview

This project involves training a neural network to recognize and classify drawings made by users. The neural network is trained using data from the QuickDraw dataset and is integrated into a Tkinter application that allows users to draw and receive real-time predictions of their drawings.

## Features

- **Data**: Trained a feedforward neural network using public data from QuickDraw datasets.
- **Neural Network**: Created a model using Tensorflow library that achives close to 90% accuracy.
- **Real-Time Predictions**: Displays the top 5 most likely categories and their probabilities as the user draws.
- **Tkinter Interface**: User-friendly drawing application built with Tkinter for drawing and predicting.

## Getting Started

### Prerequisites
- TensorFlow
- Tkinter
- Pandas
- Numpy
- PIL
- Python 3.11 and up

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/quickdraw-tkinter-app.git
   cd quickdraw-tkinter-app

2. **Run the tkinter app**

3. ```bash
   python3 app.py

### Neural Network Architecture

The neural network takes as input an array representing the user's drawing. Below is a summary of the architecture:
1. **Input Layer**:
   - Size: 784 units (flattened 28x28 pixel images)
   - **Normalization**: The input images are normalized to have values between 0 and 1.

2. **Dense Layer 1**:
   - Units: 300
   - Activation Function: ReLU

3. **Dense Layer 2**:
   - Units: 60
   - Activation Function: ReLU

4. **Dense Layer 3**:
   - Units: 50
   - Activation Function: ReLU

5. **Dense Layer 4**:
   - Units: 40
   - Activation Function: ReLU

6. **Output Layer**:
   - Units: Number of categories (equal to the number of classes in the dataset)
   - Activation Function: Softmax

### Model Training

- **Optimizer**: Adam
- **Loss Function**: Categorical Cross-Entropy
- **Metrics**: Accuracy
- **Epochs**: 10
- **Batch Size**: 32
- **Validation Split**: 0.2

The model is trained on 80% of the data while the rest is used for evaluation to reduce bias and have an accurate estimate on its performance.

For more details on the training process, you can refer to the `training.py` script.
