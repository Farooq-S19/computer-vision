# computer-vision
This repository contains a fully optimized computer vision pipeline designed for image preprocessing, feature extraction, model training, and real-time inference. The project uses modern deep-learning frameworks like OpenCV and PyTorch to deliver high-accuracy visual understanding across various tasks.
Key Features

Automated Image Preprocessing
Includes noise removal, resizing, sharpening, edge enhancement, and morphological transformations.

Robust Feature Extraction
Uses CNN-based deep feature extraction for highly reliable representations.

Multiple Vision Tasks Supported

Image classification

Object detection

Semantic segmentation

Image similarity & embedding generation

OCR (optional)

Modular Architecture
Each component (preprocessing → detection → classification → postprocessing) is separated for easy debugging and upgrading.

Dataset Handling
Efficient image loaders, train/val/test split utilities, augmentation pipeline.

Model Training Pipeline
Single-command training script with live metrics, early stopping, and checkpointing.

Real-time Inference Engine
Optimized for CPU/GPU with support for ONNX export and quantization.

Explainability Tools
Grad-CAM heatmaps for understanding model predictions.

🛠️ Tech Stack

Languages: Python

Libraries:

OpenCV

PyTorch

TensorFlow (optional)

NumPy, Pandas

Matplotlib, Pillow

Deployment: Flask / FastAPI (optional), ONNX Runtime

Hardware: CPU/GPU compatible
