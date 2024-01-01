from PIL import Image

with Image.open("1.jpeg") as im:
    # Resize the image
    im_resized = im.resize((80, 80))
    # Save the resized image
    im_resized.save("1_1.jpeg")