#!/usr/bin/env python3
import sys
from PIL import Image
from datetime import datetime

def add_green_background(input_path, output_path, color='green'):
    """
    Takes a transparent PNG image and places it on a colored background.
    
    Args:
        input_path (str): Path to the input transparent PNG image
        output_path (str): Path to save the output image
        color (str): Background color - 'red', 'green', or 'blue'
    """
    # Define color mappings
    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255)
    }
    
    try:
        # Open the transparent image
        img = Image.open(input_path).convert("RGBA")
        
        # Create a new image with colored background of the same size
        width, height = img.size
        bg_color = colors.get(color.lower(), colors['green'])  # Default to green if invalid color
        background = Image.new("RGBA", (width, height), bg_color + (255,))
        
        # Composite the transparent image onto the colored background
        composite = Image.alpha_composite(background, img)
        
        # Save the result
        composite.convert("RGB").save(output_path)
        
        print(f"Successfully created image with {color} background: {output_path}")
        
    except Exception as e:
        print(f"Error processing image: {e}")
        sys.exit(1)

def main():
    # Get the filename
    filename = input("Enter the PNG file name: ")
    
    # Get the color choice
    print("\nChoose background color:")
    print("1. Red")
    print("2. Green")
    print("3. Blue")
    choice = input("Enter choice (1-3) [default=2]: ").strip()
    
    # Map choice to color
    color_map = {'1': 'red', '2': 'green', '3': 'blue'}
    color = color_map.get(choice, 'green')
    
    # Generate unique output filename using timestamp and color
    base_name = filename.rsplit('.', 1)[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{base_name}_{color}_{timestamp}.png"
    
    add_green_background(filename, output_filename, color)

if __name__ == "__main__":
    main() 