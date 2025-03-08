# Installing Python

There are varioues ways to install Python 3 and its modules: there is the official 'plain' Python distribution but also package managers (i.e. Anaconda) or preset environments (i.e. Python(x,y)) which give you Python plus many packages. Once completed the installation, Python 3 contains a command `pip` (sometimes called `pip3` in Python 3), which allows to install afterwards other packages you may need.

The best way to choose what to install depends upon which operating system you have and what you intend to do with it. In this book we will use Python 3 and scientific packages, so we will try to create an environment to support this scenario.


Given the wide variety of installation methods and the fact Python is available in already many programs, it might be you already have installed Python without even knowing it, maybe in version 2, but we need the 3! Overlaying several Python environments with the same version may cause problems, so in case of doubt ask somebody who knows more!


## Windows installation


For Windows, we suggest to install the distribution [Anaconda for Python 3](https://www.anaconda.com/download/success) or greater, which, along with the native Python package manager `pip`, also offers the  more generic command line package manager `conda`.

Once installed, verify it is working like this:

1. click on the Windows icon in the lower left corner and search for 'Anaconda Prompt'. It should appear a console where to insert commands, with written something like `C:\Users\David> `. NOTE: to launch Anaconda commands, only use this special console. If you use the default Windows console (`cmd`), Windows will not be able to find Python.

2. In Anaconda console, type:

```bash
conda list
```

It should appear a list of installed packages, like

```
# packages in environment at C:\Users\Jane\AppData\Local\Continuum\Anaconda3:
#
alabaster                 0.7.7                    py35_0
anaconda                  4.0.0               np110py35_0
anaconda-client           1.4.0                    py35_0
...
numexpr                   2.5                 np110py35_0
numpy                     1.10.4                   py35_0
odo                       0.4.2                    py35_0
...
yaml                      0.1.6                         0
zeromq                    4.1.3                         0
zlib                      1.2.8                         0

```

3. Try Python3 by typing in the Anaconda console:

```bash
C:>  python
```
It should appear something like:

```
Python 3.6.3 (default, Sep 14 2017, 22:51:06)
MSC v.1900 64 bit (Intel)[GCC 5.4.0 20160609] on win64
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

```{warning}

With Anaconda, you must write `python` instead of `python3`!

If you installed Anaconda for Python3, it will automatically use the correct Python version by simply writing `python`. If you write `python3` you will receive an error of file not found!

```


```{warning}

If you have Anaconda, always use `conda` to install Python modules! So if in next tutorials you se written `pip3 install whatever`, you will instead have to use `conda install whatever`

```

## Mac installation

To best manage installed app on Mac independently from Python, usually it is convenient to install a so called _package manager_. There are various, and one of the most popular is [Homebrew](https://brew.sh/). So we suggest to first install Homebrew and then with it you can install Python 3, plus eventually other components you might need. As a reference, for installation we took and simplified this [guide by Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos)


```{warning}

Check if you already have a package manager!

If you already have installed a package manager like for example Conda (in _Anaconda_ distribution), _Rudix,_ _Nix,_ _Pkgsrc,_ _Fink,_ o _MacPorts,_ maybe Homebrew is not needed and it's better to use what you already have. In these cases, it may be worth asking somebody who knows more! If you already have _Conda/Anaconda_, it can be ok as long as it is for Python 3.

```

1. Open the Terminal

MacOS terminal is an application you can use to access command line. As any other application, it's available in _Finder_, navigation in _Applications_ folder, and the in the folder _Accessories_. Frotm there, double click on the _Terminal_ to open it as any other app. As an alternative, you can use _Spotlight_ by pressing _Command_ and _Space_ to find the Terminal typing the name in the bar that appears.

2. Install Homebrew by executing in the terminal this command:

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```


3. Add `/usr/local/bin` to `PATH`

    In this passage with an unsettling name, once Homebrew installation is completed, you will make sure that apps installed with Homebrew shall always be used instead of those Mac OS X may automatically select.

    1. Open a new Terminal.

    2. From within the terminal, digit the command

        ```bash
        ls -a
        ```

        You will see the list of all files present in the home folder. In these files, verify if a file exists with the following name: `.profile` (note the dot at the beginning):

        - If it exists, go to following step
        - If it doesn't exist, to create it type the following command:

            ```bash
            touch  $HOME/.profile
            ```

    3. Open with text edit the just created file `.profile` giving the command:

        ```bash
        open -e  $HOME/.profile
        ```

    4. In text edit, add to the end of the file the following line:

        ```bash
        export PATH=/usr/local/bin:$PATH
        ```

    5. Save and close both Text Edit and the Terminal


4. Verify Homebrew is correctly installed, by typing in a new Terminal:

    ```bash
    brew doctor
    ```

    If there aren't updates to do, the Terminal should show:

    ```bash
    Your system is ready to brew.
    ```

    Otherwise, you might see a warning which suggest to  execute another command like `brew update` to ensure the Homebrew installation is updated.

5. Install python3 (Remember the '3'!):


    ```bash
    brew install python3
    ```

    Along with python 3, Homebrew will also install the internal package manager of Python `pip3` which we will use in the following.

6. Verify Python3 is correctly installed. By executing this command the writing `"/usr/local/bin/python3"` should appear:

    ```bash
    which python3
    ```

    After this, try to launch

    ```bash
    python3
    ```

    You should see something similar:

    ```bash
    Python 3.6.3 (default, Nov 17 2016, 17:05:23)
    [GCC 5.4.0 20160609] on mac
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```

    To exit Python, type `exit()` and press Enter.


## Linux installation

Luckily, all Linux distributions are already shipped with package managers to easily install applications.

- If you have Ubuntu, you may need to install `python3-venv`:
    ```bash
    sudo apt-get install python3-venv
    ```

- If you _don't_ have Ubuntu, you probably already know how to install Python and pip, but feel free to ask the course instructor for help.

To verify the installation, try to run from the terminal

```bash
python3
```

You should see something like this:

```bash
Python 3.6.3 (default, Nov 17 2016, 17:05:23)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
