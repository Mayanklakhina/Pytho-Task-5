# Files : create, open, read and writing.


#(i) Creating a file with write mode enabled and then closing it.

my_file = open("randomFile.txt", "w")             
my_file.close() 
               


#(ii) Writing to a file.
with open("randomFile.txt","w") as f:
 
 f.write("This is just a random file to check the files I/O functionality.\n")    


                                              
#(iii) Appending to a file.
with open("randomFile.txt","a") as f:
 
 f.write("This 2nd line has been appended by Python :) ..\n")    
                                                   


#(iv) Reading some characters from the file.   

with open("randomFile.txt","r") as f:
 s = f.read(4)                       # This will read first 4 characters from the file.
 print(s,"\n") 


#(v) Reading the whole file.

with open("randomFile.txt","r") as f:
 s = f.read()                          # This will read the whole file.
 print(s)       


#(vi) Reading the first line from the file.

with open("randomFile.txt","r") as f:
 spell = f.readline()                     # This will read the first line of the file.
 print(spell)


#(vii) Reading the second line from the file.


 s = f.readline()                      # This will read the second line of the file.
 print(s)                  
 