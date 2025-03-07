# PNG Background Color Converter

This script takes a transparent PNG image and places it on a colored background (red, green, or blue) for keying effects, creating a new image with the same dimensions.

## Requirements

- Python 3.6+
- Pillow library

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Simply run the script:

```bash
python luma.py
```

The script will:
1. Ask you for the name of your PNG file (must be in the same directory)
2. Present you with color options:
   - 1. Red
   - 2. Green (default)
   - 3. Blue
3. Create a new file with your chosen background color and a unique timestamp

## Example

If you have `logo.png` in your directory:
1. Run `python luma.py`
2. Enter: `logo.png`
3. Choose a color (1-3)
4. The script will create something like: `logo_green_20240319_143022.png`

## Output Files

Output files are automatically named using this format:
`originalname_color_timestamp.png`

For example:
- `logo_red_20240319_143022.png`
- `logo_green_20240319_143022.png`
- `logo_blue_20240319_143022.png`

Each file gets a unique timestamp, so you never need to worry about overwriting existing files.

## Why Use This for Keying?

Color keying and luma keying are techniques used in video production to replace areas of an image based on color or brightness levels. This tool makes it easy to prepare images for:
- Green screen effects
- Blue screen effects
- Red screen effects
- Various keying techniques in video editing software 