from PIL import Image
import os

# Paths
input_path = "/Users/rtencate/.gemini/antigravity/brain/a7a03492-77a6-46ac-9b9b-5d24b5c276a6/uploaded_image_1767702690368.png"
output_path = "images/logo-green.png"

# Colors
target_color = (214, 232, 92, 255) # #D6E85C

def process_logo():
    if not os.path.exists(input_path):
        print(f"Error: Input file {input_path} not found.")
        return

    img = Image.open(input_path)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        # Check if pixel is light (white-ish)
        # Using a simple threshold sum of RGB
        # Inverted logic:
        # If pixel is light (Text), make it Target Color
        # If pixel is dark (Background), make it Transparent
        if item[0] > 150 and item[1] > 150 and item[2] > 150:
            new_data.append(target_color) 
        else:
            new_data.append((0, 0, 0, 0)) # Transparent

    img.putdata(new_data)
    img.save(output_path, "PNG")
    print(f"Successfully saved transparent logo to {output_path}")

if __name__ == "__main__":
    process_logo()
