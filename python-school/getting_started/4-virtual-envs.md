
# Projects with virtual environments


```{warning}

If these are your first steps with Python, you can skip this section.

You should read it if you have already done personal projects with Python that you want to avoid compromising, or when you want to make a project to ship to somebody.
```

When we start a new project with Python, we usually notice quickly that we need to extend Python with particular libraries, like for example to draw charts. Not only that, we might also want to install Python programs which are not written by us and they might as well need their peculiar libraries to work.

Now, we could install all these extra libraries in a unique cauldron for the whole computer, but each project may require its specific versions of each library, and sometimes it might not like versions already installed by other projects. Even worse, it might automatically update packages used by old projects, preventing old code from working anymore. So it is PRACTICALLY NECESSARY to separate well each project and its dependencies from those of other projects: for this purpose you can create a so-called _virtual environment_ .

## Creating virtual environments

* **If you installed Anaconda**, to create virtual environments you can use its package manager `conda`. Supposing we want to call our project `myprj` (but it could be any name), to put into a folder with the same name `myprj`, we can use this command to create a virtual environment:

    ```bash
    conda create -n myprj
    ```
    The command might require you to download packages, you can safely confirm.


* **If you** ***don't have*** **Anaconda installed**, to create virtual environments it's best to use the native Python module `venv`:

    ```bash
    python3 -m venv myprj
    ```

Both methods create the folder `myprj` and fill it with all required Python files to have a project completely isolated from the rest of the computer. But now, how can we tell Python  we want to work right with that project? We must _activate_  the environment as follows.

## Activate a virtual environment

To activate the virtual environment, we must use different commands according to our operating system (but always from the terminal)


**Activate environment in Windows with Anaconda**:

```bash
activate myprj
```

**Linux & Mac (without Anaconda)**:

```bash
source myprj/bin/activate
```

Once the environment is active, in the command prompt we should see the name of that environment (in this case `myprj`) between round parenthesis at the beginning of the row:

```
(myprj) some/current/folder >
```

The prefix lets us know that the environment `myprj` is currently active, so Python comands we will use all use the settings and libraries of that environment.

Note: inside the virtual environment, we can use the command `python` instead of `python3` and `pip` instead of `pip3`


**Deactivate an environment**:

Write in the console the command `deactivate`. Once the environment is deactivated, the environment name `(myprj)` at the beginning of the prompt should disappear.

## Executing environments inside Jupyter

As we said before, Jupyter is a system-level application, so there should be one and only one Jupyter. Nevertheless, during Jupyter execution, we might want to execute our Python commands in a particular Python environment. To do so, we must configure Jupyter so to use the desired environment. In Jupyter terminology, the configurations are called _kernel_: they define the programs launched by Jupyter (be they Python versions or also other languages like R). The current kernel for a notebook is visibile in the right-upper corner. To select a desired kernel, there are several ways:

### With Anaconda

Jupyter should be available in the Navigator. If in the Navigator you enable an environment (like for example Python 3), when you then launch Jupyter and create a notebook you should have the desired environment active, or at least be able to select a kernel with that environment.


### Without Anaconda

In this case, the procedure is a little more complex:


— 1 From the terminal þactivate your environment](#Activate-a-virtual-environment)


— 2 Create a Jupyter kernel:

```bash
    python3 -m ipykernel install --user --name myprj
```

NOTE: here `myprj` is the name of the _Jupter kernel._  We use the same name of the environment only for practical reasons.

— 3 Deactivate your environment, by launching

```bash
    deactivate
```



From now on, every time you run Jupyter, if everything went well under the `Kernel` menu in the notebook you should be able to select the kernel just created (in this example, it should have the name `myprj`)

```{note}

The passage to create the kernel must be done only once per project

```

```{note}

You don't need to activate the environment before running Jupyter!

During the execution of Jupyter simply select the desired kernel. Nevertheless, it is convenient to execute Jupyter from the folder of our virtual environment, so we will see all the project files in the Jupyter home.

```
