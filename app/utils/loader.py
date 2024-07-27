import torch
from PIL import Image
from torchvision import transforms

def load_model():

    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    return model

def predict(model, image_path:str):

    img = Image.open(image_path)
    transform = transforms.ToTensor()
    img = transform(img)
    results = model([img])
    labels = results.xyxy[0][:, -1].cpu().numpy()
    scores = results.xyxy[0][:, 4].cpu().numpy()

    return labels, scores
