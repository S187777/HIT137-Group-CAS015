from PIL import Image
import time

# Step 1: Generate the number n
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print(f"Generated number: {generated_number}")

# Step 2: Open the image (replace 'Chapter1.png' with the correct file path if necessary)
image = Image.open('chapter1.jpg')

pixels = image.load()  # This allows pixel manipulation

# Step 3: Modify the pixels
width, height = image.size
total_red_value = 0  # We'll use this to store the sum of red values

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        # Add the generated number to each of the RGB components
        new_r = min(255, r + generated_number)  # Ensure we don't exceed 255
        new_g = min(255, g + generated_number)
        new_b = min(255, b + generated_number)
        
        # Update the pixel in the image
        pixels[x, y] = (new_r, new_g, new_b)
        
        # Sum the red values
        total_red_value += new_r

# Step 4: Save the modified image
image.save('chapter1out.png')

# Step 5: Print the total red value sum
print(f"Total sum of red pixel values: {total_red_value}")
