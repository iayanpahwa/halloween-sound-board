import ST7789 as ST7789
from PIL import Image
from sys import exit

display_type = "square"
image_file = "images/a.png"

# Create ST7789 LCD display class.
disp = ST7789.ST7789(
    height=135 if display_type == "rect" else 240,
    rotation=0 if display_type == "rect" else 90,
    port=0,
    cs=ST7789.BG_SPI_CS_FRONT,  # BG_SPI_CS_BACK or BG_SPI_CS_FRONT
    dc=9,
    spi_speed_hz=80 * 1000 * 1000,
    offset_left=0 if display_type == "square" else 40,
    offset_top=53 if display_type == "rect" else 0
)

WIDTH = disp.width
HEIGHT = disp.height

# Initialize display.
disp.begin()

# Load an image.
print('Loading image: {}...'.format(image_file))
image = Image.open(image_file)

# Resize the image
image = image.resize((WIDTH, HEIGHT))
disp.display(image)

exit("image displayed")