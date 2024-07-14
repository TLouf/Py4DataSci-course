# Course setup


## Getting the course content

Download the course content from [this link](https://github.com/TLouf/Py4DataSci-course/archive/refs/heads/main.zip), and then move the file to wherever you'd like to put the courses contents, and extract it.


## Installing packages


### For the course

Navigate to the directory you just extracted, and run

```bash
pip install -r requirements.txt
```


### Install other packages (if needed)

You can extend Python by installing several free packages. The best way to do it varies according to the operating system and the installed package manager.

```{warning}

We will be using _system commands_. If you see `>>>` in the command line, it means you are inside Python interpreter and you must first exit: to do it, type `exit()` and press Enter.
```

In what follows, to check if everything is working, you can substitute `PACKAGENAME` with `requests` which is a module for the web.


If you have Anaconda:

- click on Windows icon in the lower left corner and search `Anaconda Prompt`. A console should appear where to insert commands, with something written like `C:\Users\David>`. (NOTE: to run commands in Anaconda, use only this special console. If you use the default Windows console (cmd), Windows, will not be able to find Python)

- In the console type `conda install PACKAGENAME`

If you have Linux/Mac open the Terminal and give this command (`--user` install in your home):

```
python3 -m pip install --user PACKAGENAME
```

```{note}
If you receive errors which tell you the command `python3` is not found, remove the `3` after `python`

```


```{note}

There is also a system command `pip` (or `pip3` according to your system). You can directl call it with  `pip install --user PACKAGENAME`

Instead, we install instead with commands like `python3 -m pip install --user PACKAGENAME` for uniformity and to be sure to install packages for Python 3 version

```
