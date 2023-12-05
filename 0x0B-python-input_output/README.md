# 0x0B. Python - Input/Output

Python uses file objects to interact with external files on your computer. These file objects can be any sort of file you have on your computer, whether it be an audio file, a text file, emails, Excel documents, etc.
To open a file in Python, you use the built-in open() function. The open() function takes two parameters: the name of the file, and the mode for which we would like to open the file.
For example, if we wanted to open a file named example.txt for reading, we would use:
```
file = open("example.txt", "r")
```
Here, "r" stands for read mode, which is one of the many modes you can choose to open a file with. Some other modes include "w" for write (will write to a file, and create it if it doesn't exist), "a" for append (will add onto files), and "r+" for both reading and writing.
To read a file, you can use the read() method, like so:
```
print(file.read())
```
And to write to a file, you can use the write() method:
```
file = open("example.txt", "w")
file.write("This is a new line")
```
Remember to always close your files when you're done with them:
```
file.close()
```


## Tasks/Files


|     Tasks           |Files                          |
|----------------|-------------------------------|
|0. Read file|`'0-read_file.py'`            |
|1. Write to a file|`1-write_file.py`            |
|2. Append to a file|`2-append_write.py`|
|3. To JSON string|`3-to_json_string.py`|
|4. From JSON string to Object|`4-from_json_string.py`|
|5. Save Object to a file|`5-save_to_json_file.py`|
|6. Create object from a JSON file|`6-load_from_json_file.py`|
|7. Load, add, save|`7-add_item.py`|
|8. Class to JSON|`8-class_to_json.py`|
|9. Student to JSON|`9-student.py`|
|10. Student to JSON with filter|`10-student.py`|
|11. Student to disk and reload|`11-student.py`|
|12. Pascal's Triangle|`12-pascal_triangle.py`|

