from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

def get_image_caption(image_path):
    
    image = Image.open(image_path).comvert('RGB')
    model_name = "Salesforce/blip-image-captioning-large"
    device = "cuda"

    processor = BlipProcessor.from_pretrained(model_name).to(device)
    model = BlipForConditionalGeneration.from_pretrained(model_name).to(device)

    pass

def detect_objects(image_path):

    pass

if __name__ == '__main__':
    pass
