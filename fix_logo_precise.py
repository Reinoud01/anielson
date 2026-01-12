from PIL import Image

# Paths
original_input = "/Users/rtencate/.gemini/antigravity/brain/a7a03492-77a6-46ac-9b9b-5d24b5c276a6/uploaded_image_1767702690368.png"
final_output = "/Users/rtencate/Documents/Github/Anielson/images/logo-green.png"

# Colors
target_color = (214, 232, 92, 255)  # #D6E85C

# Load the original image
img = Image.open(original_input)
img = img.convert("RGBA")
pixels = img.load()
width, height = img.size

# Step 1: Convert the image (dark text -> green, light background -> transparent)
# This is the original process_logo.py logic
new_data = []
for y in range(height):
    for x in range(width):
        item = pixels[x, y]
        # If pixel is light (background), make it transparent
        # If pixel is dark (text), make it green
        if item[0] > 150 and item[1] > 150 and item[2] > 150:
            new_data.append(target_color)
        else:
            new_data.append((0, 0, 0, 0))  # Transparent

# Apply the conversion
img.putdata(new_data)

# Step 2: Now carefully remove just the 'R' from "DER"
# Reload pixels after putdata
pixels = img.load()

# The 'R' in "DER" is located approximately at x: 375-495, y: 90-215
# We'll make these pixels transparent
x_start = 375
x_end = 495
y_start = 90
y_end = 215

for x in range(x_start, min(x_end, width)):
    for y in range(y_start, min(y_end, height)):
        pixels[x, y] = (0, 0, 0, 0)  # Make transparent

# Save the result
img.save(final_output, "PNG")
print(f"Successfully removed the 'R' from 'DER' while keeping everything else the same")
