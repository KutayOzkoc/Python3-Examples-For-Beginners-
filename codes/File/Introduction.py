"""
    open() => We use this method for create and open file
    open(file_name ,file_access_mode)


    File access modes :
        "w": (write) write file from 0
        "a": (append) append something to file
        "x": (create) create file mode but if file already exist
             it gives you an exception or error
        "r": (read) read something from file.
 
"""
file = open("newFile.txt", "w")  # We create a file
print(file)  # Open returns a output value and it gives you which mode you used
file2 = open("/home/kutay/Desktop/python/codes/File/Second.txt", "w")
# We can give a path for create file

file.write("Merhaba")


file2.close()
file.close()  # We need to close files
