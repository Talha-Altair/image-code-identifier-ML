import cv2
from pyzbar.pyzbar import decode
import os

def BarcodeReader(image):
    
    img = cv2.imread(image)

    detectedBarcodes = decode(img)
    
    if not detectedBarcodes:
        return ("Barcode Not Detected in this image")
    else:
        for barcode in detectedBarcodes:
            (x, y, w, h) = barcode.rect
            
            cv2.rectangle(img, (x-10, y-10),(x + w+10, y + h+10),(255, 0, 0), 2)

            if barcode.data!="":
                return (barcode.data)
            else:
                return "data not clear"

if __name__ == "__main__":

    all_images = os.listdir('static/')

    for image in all_images:

        print(f"File_name:{image}")

        try:
            data = BarcodeReader(f'static/{image}')
        except:
            data = "Not an Image"

        print(f'data: {data}\n')
