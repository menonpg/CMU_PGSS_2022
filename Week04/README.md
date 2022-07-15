# L6, 7/15/2022 Topics:

- Low code, no-code modeling from Images 
    - Learning from Images using Teachable Machine  ( Google )
    - Learning from Images using Lobe.ai ( Microsoft )

- Review of concepts relating to local code development
    - Using miniconda to set up a local python environment 
    - Managing python environments locally using Conda
    - Managing python environments using venv / pip 


# Using Conda for package management:

1. Install conda:
    ## Setting  up miniconda in Mac:
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
    bash Miniconda3-py39_4.12.0-Linux-x86_64.sh

    ## Setting up miniconda in Linux:
    wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh
    bash Miniconda3-py39_4.12.0-Linux-x86_64.sh

2. Create an environment with a name of your choice:
    conda create --name pgss2022_py38 python=3.8

3. Activate your conda environment
    conda activate pgss2022_py38

4. Install  requirements:
    pip install -r requirements.txt 

# Use pip venv for package management:
    python3 -m venv myLocalPythonVENV 
    source myLocalPythonVENV/bin/activate



#  The woes of windows users:  Setting up WSL for a subsystem made of Ubuntu that integrates with your Windows 10 machine:
## Windows Subsystem for Linux (WSL)

Windows subsystem for Linux, or WSL, is a feature built into the Windows operating system which allows you to run Linux-based applications without having to leave Windows.

There are two methods to install WSL, depending on which version of Windows you are using:

- Express Installation. This method of installing WSL [requires](https://docs.microsoft.com/en-us/windows/wsl/install#prerequisites) Windows 10 version 2004 and higher, or Windows 11.
- Manual Installation. If you are running a version of Windows older than Windows 10 version 2004, you will need to follow the Manual Installation instructions.


### Express Installation

 Open a Windows PowerShell prompt as an administrator and run the following command:

```
wsl --install -d Ubuntu-20.04
```

This performs all of the steps outlined in the Manual Installation section.

### Manual Installation

 The following steps are a condensed version of [Microsoft's manual WSL installation instructions](https://docs.microsoft.com/en-us/windows/wsl/install-manual).

**Step 1: Enable Windows Features**

WSL requires two optional Windows features to be enabled:
- Windows Subsystem for Linux
- Virtual Machine Platform

To enable these features, open PowerShell as Administrator  (Start menu > PowerShell > right-click > Run as Administrator) and run the following two commands:


```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

```
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

Then restart your computer before moving to the next step. 

**Step 2: Install the Linux kernel package**

[Download the Linux kernel update package](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi). Then run the update package by double clicking on the file. When the installation is complete move to the next step.

**Step 3: Set WSL 2 as the default WSL version**

Open PowerShell as Administrator and run the following command:

```
wsl --set-default-version 2
```