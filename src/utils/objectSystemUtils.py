import json
from PIL import Image
import os.path
from os import path
from utils import globalInfo

import pygame

infoObject = globalInfo.variables()
cellSize = infoObject.gridCellSize
existingPaths = []


def getObjectByType(x, y, typeID, rotation):
    with open("./data/types.json", encoding="utf8") as f:
        types = json.load(f)

    type = types[str(typeID)]
    pngPath = type["src"]

    if path.exists("./sprites/{}".format(pngPath)):
        pngPath = "./sprites/{}".format(pngPath)
        returnCode = 0
    else:
        pngPath = "./sprites/error.png"
        returnCode = 1


    if "down" in rotation:
        if not "./sprites/temp/down_{}.png".format(typeID) in existingPaths:
            imageObject = Image.open(pngPath)
            imageObject = imageObject.transpose(Image.FLIP_TOP_BOTTOM)
            imageObject.save("./sprites/temp/down_{}.png".format(typeID))
        else:
            existingPaths.append("./sprites/temp/down_{}.png".format(typeID))
        pngPath = "./sprites/temp/down_{}.png".format(typeID)
    elif "flipped" in rotation:
        if not "./sprites/temp/flipped_{}.png".format(typeID) in existingPaths:
            imageObject = Image.open(pngPath)
            imageObject = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
            imageObject.save("./sprites/temp/flipped_{}.png".format(typeID))
        else:
            existingPaths.append("./sprites/temp/flipped_{}.png".format(typeID))
        pngPath = "./sprites/temp/flipped_{}.png".format(typeID)

    if "flipped" in rotation and "down" in rotation:
        if not "./sprites/temp/flipped_down_{}.png".format(typeID) in existingPaths:
            imageObject = Image.open(pngPath)
            imageObject = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
            imageObject = imageObject.transpose(Image.FLIP_TOP_BOTTOM)
            imageObject.save("./sprites/temp/flipped_down_{}.png".format(typeID))
        else:
            existingPaths.append("./sprites/temp/flipped_down_{}.png".format(typeID))
        pngPath = "./sprites/temp/flipped_down_{}.png".format(typeID)

    returnY = 720 - y * cellSize - cellSize
    returnX = x * cellSize

    hitboxType = type["type"]

    return pngPath, returnX, returnY, hitboxType, returnCode


if __name__ == "__main__":
    print(
        "This is a library, not a script, strting test, this could take a few microseconds"
    )
    print(getObjectByType(0, 0, 1, "right"))
