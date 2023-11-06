from PIL import Image
from image_converter import ListToImage, ImageToList

def main():
  # Open the image.
  dog_img = Image.open("duck.png")
  pixels = ImageToList(dog_img)

  # Apply the custom filter.
  filtered_pixels = apply_filter(pixels)

  # Save an image
  filtered_image = ListToImage(filtered_pixels)
  filtered_image.save("filtered.png")
  return


def apply_filter(pixels):
  # Filter the image.
  new_pixels = []

  for row in range(len(pixels)):
    new_row = []
    for col in range(len(pixels[row])):
      orig_r = pixels[row][col][0]
      orig_g = pixels[row][col][1]
      orig_b = pixels[row][col][2]
      avg = (orig_r+orig_g+orig_b)/3
      if col == 0:
        new_row.append((255, 255, 255))
      else:
        prev_r = pixels[row][col-1][0]
        prev_g = pixels[row][col-1][1]
        prev_b = pixels[row][col-1][2]
        prev_avg = (prev_r+prev_g+prev_b)/3
        diff = abs(prev_avg - avg)
        if abs(prev_r-orig_r) > 4 or abs(prev_g-orig_g) > 4 or abs(prev_b-orig_b)>4:
          new_row.append((255-diff, 255-diff, 255-diff))
        else:
          new_row.append((255, 255, 255))
    new_pixels.insert(row, new_row)
  return new_pixels

main()
