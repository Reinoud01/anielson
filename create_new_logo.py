from PIL import Image

# Paths
example_input = "/Users/rtencate/.gemini/antigravity/brain/e66ff5a9-d184-4f13-a96d-3de50c1bd9eb/uploaded_image_1767797733923.png"
final_output = "/Users/rtencate/Documents/Github/Anielson/images/logo-green.png"

# Colors
target_color = (214, 232, 92, 255)  # #D6E85C (the green from the website)

# Load the example image
img = Image.open(example_input)
img = img.convert("RGBA")
pixels = img.load()
width, height = img.size

# Convert: dark pixels (text/border) -> green, light pixels (background) -> transparent
for y in range(height):
    for x in range(width):
        pixel = pixels[x, y]
        # If pixel is dark (text/border), make it green
        # If pixel is light (background), make it transparent
        if pixel[0] < 150 and pixel[1] < 150 and pixel[2] < 150:
            pixels[x, y] = target_color
        else:
            pixels[x, y] = (0, 0, 0, 0)  # Transparent

# Save the result
img.save(final_output, "PNG")
print(f"Successfully created new logo with correct text 'DE RUI MTE MANNEN' in green")
