import sys, getopt
from PIL import Image
import numpy as np

def load_file(argv):
	inputfile = ""
	try:
		opts, args = getopt.getopt(argv,"hi:",["ifile="])
	except getopt.GetoptError:
		print("split_img.py -i <inputfile>")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("split_img.py -i <inputfile>")
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
	print("inputfile: " + inputfile)
	image = Image.open(inputfile)
	return image, inputfile

def change_image_channels(image):
	# 4 channels to 3 channels
	if image.mode == 'RGBA':
		r, g, b, a = image.split()
		image = Image.merge("RGB", (r, g, b))
	# 1 channel to 3 channels
	elif image.mode != 'RGB':
		image = image.convert("RGB")
	return image

# def print_size(image_array):
# 	row = len(image_array)
# 	column = len(image_array[0])
# 	channel = len(image_array[0][0])
# 	print("resolution: {} x {} x {}".format(row, column, channel))
# 	return row, column

def select_method():
	print("choose a method to split the image: ")
	print("1. 1 x 2" + "    " + "9. 3 x 2")
	print("2. 1 x 3" + "    " + "10. 3 x 3")
	print("3. 1 x 4" + "    " + "11. 3 x 4")
	print("4. 2 x 1" + "    " + "12. 4 x 1")
	print("5. 2 x 2" + "    " + "13. 4 x 2")
	print("6. 2 x 3" + "    " + "14. 4 x 3")
	print("7. 2 x 4" + "    " + "15. 4 x 4")
	print("8. 3 x 1" + "    " + "16. other")
	choice = input("your choice: ")
	choice = int(choice)
	if(choice == 0):
		return 1, 1
	elif(choice == 1):
		return 1, 2
	elif(choice == 2):
		return 1, 3
	elif(choice == 3):
		return 1, 4
	elif(choice == 4):
		return 2, 1
	elif(choice == 5):
		return 2, 2
	elif(choice == 6):
		return 2, 3
	elif(choice == 7):
		return 2, 4
	elif(choice == 8):
		return 3, 1
	elif(choice == 9):
		return 3, 2
	elif(choice == 10):
		return 3, 3
	elif(choice == 11):
		return 3, 4
	elif(choice == 12):
		return 4, 1
	elif(choice == 13):
		return 4, 2
	elif(choice == 14):
		return 4, 3
	elif(choice == 15):
		return 4, 4
	elif(choice == 16):
		row = int(input("row:    "))
		column = int(input("column: "))
		return row, column
	else:
		sys.exit(1)

def split_image(image, filename, row, column, r, c):
	piece_row1 = row // r
	piece_row2 = piece_row1 + row % r
	piece_column1 = column // c
	piece_column2 = piece_column1 + column % c
	for i in range(r):
		if(i == r-1):
			piece_row = piece_row2
		else:
			piece_row = piece_row1
		for j in range(c):
			if(i == r-1):
				piece_column = piece_column2
			else:
				piece_column = piece_column1
			cropped = image.crop((j*piece_column1, i*piece_row1, j*piece_column1+piece_column, i*piece_row1+piece_row))
			path = "./{}_{}_{}.jpg".format(filename.split('.')[0], i, j)
			print("output: " + path)
			cropped_column, cropped_row = cropped.size
			print("resolution: {} x {}".format(cropped_column, cropped_row))
			cropped.save(path)

def main(argv):
   img, filename = load_file(argv)
   # img.show()
   column, row = img.size
   print("resolution: {} x {}".format(column, row))
   img = change_image_channels(img)
   # img_arr = np.array(img)
   # row, column = print_size(img_arr)
   r, c = select_method()
   split_image(img, filename, row, column, r, c)
   
   
if __name__ == "__main__":
   main(sys.argv[1:])