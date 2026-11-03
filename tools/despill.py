#!/usr/bin/env python3
"""Despill a chroma-keyed atlas: remove green-dominant pixels + erode alpha 1px.
Usage: python3 despill.py in.png out.png
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGBA")
a = np.array(im)
r, g, b, al = a[:, :, 0].astype(int), a[:, :, 1].astype(int), a[:, :, 2].astype(int), a[:, :, 3]
green_mask = (g > 120) & (g > r + 40) & (g > b + 40) & (al > 0)
print(f"green mask px before: {green_mask.sum()}")
a[green_mask, 3] = 0
mask = (a[:, :, 3] > 0).astype(np.uint8)
a[~ndimage.binary_erosion(mask, iterations=1), 3] = 0
out = Image.fromarray(a)
out.save(dst)
cnt = sum(1 for rr, gg, bb, aa in out.getdata() if aa > 0 and gg > 200 and rr < 100 and bb < 100)
print(f"greenish opaque after: {cnt}")
