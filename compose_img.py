import PIL.Image as Image

def get_r_c():
   r = int(input("r: "))
   c = int(input("c: "))
   return r, c

def compose_image(r, c):
   image = [[Image  for i in range(c)] for j in range(r)]
   for i in range(r):
      for j in range(c):
         filename = "{}_{}.jpg".format(i, j)
         print("loading: " + filename)
         image[i][j] = Image.open(filename)
         # image[i][j].show()
   row = 0
   column = 0
   for i in range(r):
      _, piece_row = image[i][0].size
      row += piece_row
   for j in range(c):
      piece_column, _ = image[0][j].size
      column += piece_column
   piece_column, piece_row = image[0][0].size
   to_image = Image.new('RGB', (column, row))
   for i in range(r):
      for j in range(c):
         to_image.paste(image[i][j], (piece_column*j, piece_row*i))
   return to_image.save("./compose_image.jpg")

def main():
   r, c = get_r_c()
   compose_image(r, c)
   
if __name__ == "__main__":
   main()