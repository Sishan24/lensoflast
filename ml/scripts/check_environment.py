import sys
import cv2
import numpy as np
import tensorflow as tf

print("Python:", sys.version.split()[0])
print("TensorFlow:", tf.__version__)
print("OpenCV:", cv2.__version__)
print("NumPy:", np.__version__)
print("Visible TensorFlow devices:", tf.config.list_physical_devices())
