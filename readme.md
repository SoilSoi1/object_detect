# Graphite Bipolar Plate Defect Detection
***
## Step 1:Prepare Tools for Running
- Conda
- Pycharm
- Labelimg  

***Make sure download them by sequences above.***  
***If you have equipped them or you are using them, just skip Step 1.***
### Conda
Conda is a powerful tool to manage the visual environments for Python projects.
There are two conda applications: **ANACONDA** and **MiniCONDA**. 
MiniCONDA is the simply version of ANACONDA without GUI, where only command can be uesd.  
It's easy to set up Miniconda.  
1. Click the connection: <https://www.anaconda.com/download> to visit the official web to download suitable version of miniconda.
There is no need to register, just skip it.   
Also, you can visit the Tsinghua Mirror to download it: <https://mirrors.tuna.tsinghua.edu.cn/>
2. You only need to download and set uo it by default way, **but** don't remember to tick "Add Miniconda to my PATH environment variable."   
3. Check if miniconda is setted up successfully:   
Open CMD window (win + R, then input "cmd" and click "Enter"), input `conda --version`.
If number of conda's version occurs, that will be a success.   

After setup, find the Powershell in Miniconda's root folder and open it. 
You will see a "base" as a start of commandline, which means you are in _**base** environment_.
However, considering that deeplearning needs a complicated environment, we have to create a new environment to make sure a new project can be run, and how to create it?   

Input the command into Powershell as:  
```commandline
conda create -n <your_envs_name> python=<python version you want>
```
Input *y* or *yes* when shell asks you and you will get a new environment.

You can checkout the environments you created:  
```commandline
conda env list
# or
conda info --envs
```
When you have created a new environment, it will not be activated automatically. 
Instead, to activate it, you should input command as:  
```commandline
conda activate <environment you create>
```
If the strat of commandline turns to the name of the environment you created, it means you has activated it !   

Until now, all of work about conda has done, and remember that everytime you need to change or run your project, like installing some packages or modules, the corresponding visual environment should be activated correctly!
### Pycharm
Pycharm is one of the most popular Python IDLE in the world. Its setup is easy too.  
Search <https://www.jetbrains.com/pycharm/download> and there are Community version and Profeesional version.
The first one can satisfy the need of most daily cases, but the latter can help you connect to the server via SSH to run Python project, which is so important but unnecessary for a DL beginner.  

After setup finishing, open Set to choose the environment you create in Miniconda, and as to more details, you can search on Bilibili or Youtube, because different versions of Pycharm have some difference in setting, which is not a complex problem.  
### Labelimg
Labelimg is a tool to annotate RectBox for YOLO or Voc.  

Be careful that Labelming needs Python <= 3.8.20, or it will report error.
Because of that, you'd better create a new environment to run Labelimg, where Python=3.8.
After creating and activating your new environment, input on the commandline:`pip install labelimg -i https://pypi.tuna.tsinghua.edu.cn/simple`.

After setup finishing, input on the commandline to open it for checking:`labelimg`.

Also, you can prepare a txt file in advance. For example, create a new text named "label.txt", and then write in the labels you will annotate row by row, just like:
```text
cat
dog
human
```
And then, turn on you cmd commandline, input the command like:  
`labelimg <the picture or folder to be annotated> label.txt`

You can start annotating now.
***
## Step 2: Prepare Your Own Dataset
Dataset for YOLO is consist of two parts, which are figures and annotations, and they share the same file names.
As following the ask of Ultralytics, the data to be trained should be like:  
```text
# parent
# ├── ultralytics
# └── datasets
#     ├── iamges/train
#     └── images/val
```


## Log:
### 2025/2/24
The tested device is Surface Pro 5, only equipped with CPU intel i5-7300U, running on Windows 10, Pycharm Community.  
Caution that if the script is run on Win, the train.py must has `if __name__ == "__main__":` before your main training codes.  

The **1st** error report is: `OMP: Error #15: Initializing libiomp5md.dll, but found libiomp5md.dll already initialized.` It means that sth's wrong with your system's environment variable.   

To solve this problem, turn on the **cmd window**, activate the corresponding conda env if conda used,
run the command:  
```SET KMP_DUPLICATE_LIB_OK=TRUE```  
Make sure it valid:`echo %KMP_DUPLICATE_LIB_OK%` if output is TURE, it means the env variable has been changed successfully, and then run the py script.  

s