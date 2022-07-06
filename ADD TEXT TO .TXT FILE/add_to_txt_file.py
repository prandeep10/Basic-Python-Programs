fileout = open("student_list.txt", "w") # We can use any other file-types too, HTML Works fine.
for i in range(3):
    a = str(input("Enter Student Name :"))
    fileout.write(a)
    fileout.write("\n")
fileout.close()
