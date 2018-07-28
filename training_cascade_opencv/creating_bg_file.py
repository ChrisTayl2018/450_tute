

n = 1

for n in range(180):
	line = "neg/neg"+str(n)+".png\n"
	with open("bg.txt", "a") as text_file:

		text_file.write(line)
	
	n+=1