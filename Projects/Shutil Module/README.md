
## Shutil Module in Python

Shutil is a Python module that provides a higher level interface for working with file and directories. 
The name `shutil` is short for shell utility. 
It provides a convenient and efficient way to automate tasks that are commonly performed on files and directories. 
In this repl, we'll take a closer look at the shutil module and its various functions and how they can be used in Python.

<br>

<p align="center">
  <img src="https://github.com/user-attachments/assets/578831f1-cdee-48de-9a70-d384c8091884" alt="image">
</p>

<br>

## 🌟 Explanation

#### The following are some of the most commonly used functions in the shutil module:

- `shutil.copy(src, dst)` : This function copies the file located at src to a new location specified by dst. If the destination location already exists, the original file will be overwritten.

- `shutil.copy2(src, dst)` : This function is similar to shutil.copy, but it also preserves more metadata about the original file, such as the timestamp.

- `shutil.copytree(src, dst)` : This function recursively copies the directory located at src to a new location specified by dst. If the destination location already exists, the original directory will be merged with it.

- `shutil.move(src, dst)` : This function moves the file located at src to a new location specified by dst. This function is equivalent to renaming a file in most cases.

- `shutil.rmtree(path)` : This function recursively deletes the directory located at path, along with all of its contents. This function is similar to using the rm -rf command in a shell.

<br>

## ⚙️ Prerequisites

- Install Python 3 to run the code.
- Import shutil

<br>

## 🛠️ How to Run

- Clone this repository to your local machine.
- Navigate to the directory containing the script.
- Run the script using Python.

<br>

### To copy a file:

```python3
  python3 copy_file.py
```

<br>

### To copy folders:

```python3
  python3 copy_folder.py
```

<br>

## 📺 Output

### Before running the script

![image](https://github.com/user-attachments/assets/521c4b67-9a59-49eb-a787-0ef521b80d31)

### After running the script

![image](https://github.com/user-attachments/assets/8cf6ace9-9af6-4a49-b990-51b3fa5c3f90)

<br>

## 📜 Conclusion

As you can see, the shutil module provides a simple and efficient way to perform common file and directory-related tasks in Python. 
Whether you need to copy, move, delete, or preserve metadata about files and directories, the shutil module has you covered.
In conclusion, the shutil module is a powerful tool for automating file and directory-related tasks in Python.
Whether you are a beginner or an experienced Python developer, the shutil module is an essential tool to have in your toolbox.

<br>

## 🤖 Author
[Atharva Baikar](https://github.com/DarkGuardian641)
