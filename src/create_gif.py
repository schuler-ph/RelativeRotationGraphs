import os
import imageio
import glob
from rrg_db import DatabaseManager

png_dir = "src/plots"
config = DatabaseManager().get_config()

images = []
for file_name in sorted(os.listdir(png_dir)):
    if file_name.endswith(".png"):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave("src/gifs/animated3.gif", images, duration=0.2)

if config["remove_files_after_gif"]:
    files = glob.glob(png_dir + "/*")
    for f in files:
        os.remove(f)
