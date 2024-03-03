import base64
import os
from django.conf import settings
import io
import cv2
import numpy as np
from PIL import Image

def save_data_url_to_image(data_url, filename):
  img_out = Image.open(io.BytesIO(data_url))
  img_out = np.array(img_out)
  img_out = cv2.cvtColor(img_out, cv2.COLOR_BGR2RGB)
  media_path = os.path.join(settings.MEDIA_ROOT, filename)
  cv2.imwrite(media_path, img_out)