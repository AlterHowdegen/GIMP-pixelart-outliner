#!/usr/bin/env python
# License: Public Domain - https://creativecommons.org/share-your-work/public-domain/cc0/

from gimpfu import *
import math

def create_outline(image):

    xOffsets = [1, -1, 0, 0]
    yOffsets = [0, 0, 1, -1]
    layers = []

    originalLayer = image.active_layer

    for i in range(4):

        pdb.gimp_selection_none(image)
        pdb.gimp_selection_all(image)
        pdb.gimp_edit_copy(originalLayer)

        selection = pdb.gimp_edit_paste(originalLayer, TRUE)
        pdb.gimp_floating_sel_to_layer(selection)

        newLayer = image.active_layer
        layers.append(newLayer)

        pdb.gimp_selection_layer_alpha(newLayer)
        pdb.gimp_selection_translate(image, xOffsets[i], yOffsets[i])
        pdb.gimp_bucket_fill(newLayer, FG_BUCKET_FILL, NORMAL_MODE, 100, 0, TRUE, 0, 0)

        # newLayer.translate(xOffsets[i], yOffsets[i])

    for i in range(len(layers) - 1):
        j = (len(layers) - 2) - i
        pdb.gimp_image_merge_down(image, layers[j], EXPAND_AS_NECESSARY)

    pdb.gimp_image_lower_layer(image, image.active_layer)
    image.active_layer.name = originalLayer.name + " Outline"

register(
    "python_fu_create_outline",
    "Creates a cornerless outline of the current layer.",
    "Creates a cornerless outline of the current layer.",
    "Alter Howdegen",
    "Alter Howdegen",
    "2020",
    "Create Pixelart Outline",
    "*",
    [
        (PF_IMAGE, 'image', 'Input image:', None)
    ],
    [],
    create_outline, menu="<Image>/Filters/Pixelart/")

main()
