#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt

# Create a blank canvas (white background)
width, height = 200, 200
emoji = np.ones((height, width, 3))  # 3 for RGB color

# Define colors
yellow = [1, 0.87, 0]  # RGB color for yellow
black = [0, 0, 0]      # RGB color for black

# Create the face (a yellow circle)
center_x, center_y = width // 2, height // 2
radius = 80
for i in range(height):
    for j in range(width):
        if ((i - center_y) ** 2 + (j - center_x) ** 2) <= radius ** 2:
            emoji[i, j] = yellow

# Create the eyes (one open, one closed)
eye_radius = 10
left_eye_center = (center_x - 30, center_y - 20)
right_eye_center = (center_x + 30, center_y - 20)

# Left eye (open)
for i in range(height):
    for j in range(width):
        if ((i - left_eye_center[1]) ** 2 + (j - left_eye_center[0]) ** 2) <= eye_radius ** 2:
            emoji[i, j] = black

# Right eye (winking)
for i in range(height):
    for j in range(width):
        if ((i - right_eye_center[1]) ** 2 + (j - right_eye_center[0]) ** 2) <= eye_radius ** 2:
            emoji[i, j] = black

# Create the mouth (a smiling arc)
theta = np.linspace(0, np.pi, 100)
smile_x = center_x + 40 * np.cos(theta)
smile_y = center_y + 10 - 30 * np.sin(theta)
for i in range(len(smile_x)):
    x, y = int(smile_x[i]), int(smile_y[i])
    if 0 <= x < width and 0 <= y < height:
        emoji[y, x] = black

# Display the emoji
plt.imshow(emoji)
plt.axis('off')
plt.show()


# In[ ]:




