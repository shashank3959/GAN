# Basic Vanilla GAN implementation
import numpy as np

import torch
from torch import nn, optim
from torch.autograd.variable import Variable
from torchvision import transforms, datasets

DATA_FOLDER = './torch_data/VGAN/MNIST'