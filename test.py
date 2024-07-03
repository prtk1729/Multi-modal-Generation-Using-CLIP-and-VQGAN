from CLIP import clip
import torch
import torchvision
import torchvision.transforms as transforms
import torchvision.transforms.functional as F

if __name__ == "__main__":
    print( clip.available_models() )