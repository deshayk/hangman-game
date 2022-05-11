# Python Hangman 

![Hangman](/Hangman.png)

Game Name: Hangman
Version: 1.0
Contributors: DeShay K.

# Project Overview
Turning a classic paper and pencil game into one that you can play on your computer. Can you save the poor person from a grim fate?

# Project Description
The aim of this project is two fold: have a better understanding of the Python programming language and test that skill through application development. If you want a walkthrough of key concepts covered in this python program, make sure you read the [Medium article](https://medium.com/@deshayk/learn-by-doing-python-hangman-game-d24eee10f5a5) I wrote. Remember, friends, do or do not; there is no try!

# Installation Guide
In order to play this game, you need to use your terminal. If you aren't used to using your terminal, here is a step-by-step guide:

## Windows Instructions
### Step 1: Open your terminal
Click on the magnifying glass that allows you to search your computer for applications.
Type "terminal" and an application named "Command Prompt" should show.
Run Command Prompt Application

![Window Terminal](/instruction-img/find-terminal-app.jpg)

### Step 2: Check to see if Python is installed on your terminal
Type the following command in your terminal to see if Python is already installed:
```
python --version
```

The version of Python you have should be printed on the screen if it is installed.

![Check Python Installation](/instruction-img/check-python-installation.png)

#### Step 2a: Install Python
If Python is not installed on your computer, download the installer from the [official Python website](https://www.python.org/downloads/).

![Python Download Page](/instruction-img/python-downloads%20page.png)

Download Python Installer

![Python Installer](/instruction-img/install-python-1.png)

Make sure you allow Python to make changes to your computer. Once completed, you should see the screen below.

![Python Commands](/instruction-img/install-python-2.png)

### Step 3: Get Hangman Game Program File
In the [hangman-game](https://github.com/deshayk/hangman-game) GitHub repository, click the green "Code" button and copy either the HTTPS (web URL) or SSH (password protected) link.

![GitHub Link Copy](/instruction-img/game-download.png)

### Step 4: Download Hangman Game
Open your terminal.
Decide what folder you're going to use to host the folder (for this tutorial, I am going to save the "hangman-game" folder in my "Desktop" folder).
Change directories into the folder you are going to save the hangman game in using the following command:
```
cd Desktop
```
![Desktop Folder](/instruction-img/cd-desktop.png)

Clone the repository on your computer using the following command:
```
git clone (ssh link or HTTPs)
``` 
After you successfully cloned the repository, you should see a hangman folder on in the location you cloned the repository, in this case, you see the folder on your Desktop because it is saved in the Desktop folder.

![Git Clone](/instruction-img/git-clone.png)

### Step 4: Run Python Game
Once you have successfully cloned the file, change directories to enter the "hangman-game" folder using the following command: 
```
cd hangman-game
```

Once you are in the "hangman-game" folder, change directories to enter the "programFiles" folder using the following command: 
```
cd programFiles
```

Once you are in the programFiles folder, enter the following command to run the game file: 
```
python hangman.py
```
![Enter Hangman Game](/instruction-img/get-to-hangman.png)

You should now be able to play the hangman game as many times as you like. Once the game is over, run the following command to play another round:
```
python hangman.py
```

Enjoy the game!
