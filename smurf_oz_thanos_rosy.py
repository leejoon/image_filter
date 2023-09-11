from PIL import Image
from image_converter import ListToImage, ImageToList

def main():
  # Open the image.
  dog_img = Image.open("kim.png")
  pixels = ImageToList(dog_img)

  # Apply the custom filter.
  filtered_pixels = apply_filter(pixels)

  # Save an image
  filtered_image = ListToImage(filtered_pixels)
  filtered_image.save("kim_filtered.png")
  return


def apply_filter(pixels):
  # Filter the image.
  new_pixels = []

  for row in range(len(pixels)):
    new_row = []
    other_row = []
    for col in range(len(pixels[row])):
      orig_r = pixels[row][col][0]
      orig_g = pixels[row][col][1]
      orig_b = pixels[row][col][2]
      avg = (orig_r+orig_g+orig_b)/3
      r = avg
      g = avg
      b = avg
      new_row.insert(col, (orig_r, orig_b, orig_g))
      new_row.insert((2*col)+1, (orig_g, orig_b, orig_r))
      other_row.insert(col, (orig_g, orig_r, orig_b))
      other_row.insert((2*col)+1, (orig_b, orig_g, orig_r))
    new_pixels.insert(row, new_row)
    new_pixels.insert((2*row)+1, other_row)
  return new_pixels

main()
