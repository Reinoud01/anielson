from PIL import Image, ImageDraw

# Paths
original_input = "/Users/rtencate/.gemini/antigravity/brain/a7a03492-77a6-46ac-9b9b-5d24b5c276a6/uploaded_image_1767702690368.png"
final_output = "/Users/rtencate/Documents/Github/Anielson/images/logo-green.png"

# Colors
target_color = (214, 232, 92, 255)  # #D6E85C

# Load the original image
img = Image.open(original_input)
img = img.convert("RGBA")
width, height = img.size

# First, convert to green with transparency
pixels = img.load()
for x in range(width):
    for y in range(height):
        pixel = pixels[x, y]
        # If pixel is dark (text), make it green
        # If pixel is light (background), make it transparent
        if pixel[0] < 150 and pixel[1] < 150 and pixel[2] < 150:
            pixels[x, y] = target_color
        else:
            pixels[x, y] = (0, 0, 0, 0)  # Transparent

# Now remove the 'R' from "DER" by making those pixels transparent
# The R in "DER" is approximately at x: 370-495, y: 85-220
x_start = 370
x_end = 495
y_start = 85
y_end = 220

for x in range(x_start, min(x_end, width)):
    for y in range(y_start, min(y_end, height)):
        pixels[x, y] = (0, 0, 0, 0)  # Make transparent

# Save the result
img.save(final_output, "PNG")
print(f"Successfully created logo with 'DE RUI MTE MANNEN' (removed the R from DER)")
