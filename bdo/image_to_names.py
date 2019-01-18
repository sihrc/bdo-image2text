# -*- coding: utf-8 -*-
import argparse
import io

import cv2
import numpy as np
import pytesseract
from PIL import Image

import re

from bdo.download import get_content_from_url

user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'

def url_to_image(url):
    content = get_content_from_url(url)
    image = Image.open(io.BytesIO(content)).convert("RGB")
    open_cv_image = np.array(image)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    return open_cv_image

def main(url):
    image = url_to_image(url)
    iamge = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    ret, image = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY)
    image = 255 - image
    string = pytesseract.image_to_string(image, lang="eng")
    lines = [re.sub(r'[\(\{][^)^}]*[\)\}]', '', line).strip() for line in string.split("\n") if line]
    return lines

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="url to image")
    args = parser.parse_args()

    url = args.image

    print(main(url))

