# -*- coding: utf-8 -*-
import argparse
import os
import re

import cv2
import pytesseract


SPLIT_REGEX = "[^0-9^a-z^A-Z^_]+"
REPLACE_REGEX = r"\([\(\)]+\)"
pattern = re.compile(SPLIT_REGEX)


def main(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    ret, threshed = cv2.threshold(image, 60, 255, cv2.THRESH_BINARY)
    result = 255 - threshed
    string = pytesseract.image_to_string(result, lang="eng")
    lines = string.split("\n")

    for line in lines:
        if not line:
            continue

        line = re.sub(r'\([^)]*\)', '', line)
        line = re.sub(r'\{[^}]*\}', '', line)
        split = [x for x in pattern.split(line) if x and x != "_"]

        name_parts = []
        for item in split:
            if item.isdigit():
                points = item
                break
            else:
                name_parts.append(item)

        name = "_".join(name_parts)

        print(name, points)



def validate_path(path):
    if not os.path.exists(path):
        raise ValueError(f"Filepath {path} does not exist")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image", help="path to image")
    args = parser.parse_args()

    path = args.image
    validate_path(path)

    main(path)
