#!/usr/bin/env python3
"""Convert openbixel atlas JSON to Phaser JSON Hash (cell rects, trimmed=false).
Usage: python3 convert_phaser.py atlas.json atlas_image.png out.json
"""
import json, sys
atlas = json.load(open(sys.argv[1]))
image = sys.argv[2]
frames = {}
for action, data in atlas["actions"].items():
    for i, f in enumerate(data["frames"]):
        frames[f"{action}_{i}"] = {
            "frame": {"x": f["x"], "y": f["y"], "w": f["w"], "h": f["h"]},
            "rotated": False, "trimmed": False,
            "spriteSourceSize": {"x": 0, "y": 0, "w": f["w"], "h": f["h"]},
            "sourceSize": {"w": f["w"], "h": f["h"]},
        }
out = {"frames": frames, "meta": {"app": "Muse asset pipeline", "version": "1.0",
       "image": image, "format": "RGBA8888", "size": atlas["size"], "scale": "1"}}
json.dump(out, open(sys.argv[3], "w"), indent=2)
print(f"frames: {len(frames)} -> {sys.argv[3]}")
