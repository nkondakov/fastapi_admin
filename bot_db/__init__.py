import sys
import os
from pathlib import Path

directory = Path(os.getcwd()).parents[1] / "mercury"
sys.path.append(str(directory))

from db import *
