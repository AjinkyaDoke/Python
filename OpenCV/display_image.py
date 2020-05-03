# importing cv2  
import cv2  
  
# path  
path = r'image_file_path'
  
# Reading an image in default mode 
image = cv2.imread(path) 
  
# Window name in which image is displayed 
window_name = 'image'
  
# Using cv2.imshow() method  
# Displaying the image  
cv2.imshow(window_name, image)  
