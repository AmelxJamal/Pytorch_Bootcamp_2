import torch
from torch.utils.data import DataLoader,random_split
import argparse


args = argparse.Namespace(
    lr = 1e-4,
    bs = 8,
    train_size = 0.8,
    weight_decay = 1.0,
    path = "./data/images",
    metadata = "./data/metadata_ok.csv" 
)