from torch.utils.data import *
import json
import torchvision.transforms as transforms
from PIL import Image
NB_CLASS = 61
def default_loader(path):
    return Image.open(path).convert('RGB')


class MyDataSet(Dataset):
    def __init__(self, json_Description, transform=None, target_transform=None, loader=default_loader, path_pre=None):
        description = open(json_Description, 'r')
        imgs = json.load(description)
        image_path = [element['image_id'] for element in imgs]
        image_label = [element['disease_class'] for element in imgs]
        imgs_Norm = list(zip(image_path, image_label))
        self.imgs = imgs_Norm
        self.transform = transform
        self.target_transform = target_transform
        self.loader = loader
        self.path_pre = path_pre

    def __getitem__(self, index):
        path, label = self.imgs[index]
        img = self.loader(self.path_pre + path)
        if self.transform is not None:
            img = self.transform(img)
        if self.target_transform is not None:
            label = self.target_transform(label)
        return img, label

    def __len__(self):
        return len(self.imgs)


normalize_torch = transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225]
)

normalize_05 = transforms.Normalize(
    mean=[0.5, 0.5, 0.5],
    std=[0.5, 0.5, 0.5]
)

normalize_dataset = transforms.Normalize(
    mean=[0.463, 0.400, 0.486],
    std=[0.191, 0.212, 0.170]
)


def preprocesswithoutNorm(image_size):
    return transforms.Compose([
        transforms.Resize((image_size, image_size)),
        transforms.ToTensor()
    ])


def preprocess(normalize, image_size):
    return transforms.Compose([
        transforms.Resize((image_size, image_size)),
        transforms.ToTensor(),
        normalize
    ])


def preprocess_hflip(normalize, image_size):
    return transforms.Compose([
        transforms.Resize((image_size, image_size)),
        HorizontalFlip(),
        transforms.ToTensor(),
        normalize
    ])



