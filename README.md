# Introduction
This project helps in automatically pulling the monthly reports from harvest api's and also calculating the summary report as per the Techwave organization requirement.

This project works based on a config file. The project is written in Python. Don't worry, Below steps will explain the steps needed to run the automation without any hassle.

# Steps required:

1. Environment Setup
2. Harvest Token
3. Config File
4. Run the automation

## 1. Environment Setup
1. First, go to the official Python website and download the latest version of Python. Make sure to choose the correct version for your operating system: https://www.python.org/downloads/

2. Once you have downloaded the installer, run it and follow the instructions to install Python on your computer. During the installation, you will be asked to choose the installation location and select additional features to install.

3. After the installation is complete, you will need to add Python to your system's environment path. This will allow you to run Python commands from any directory in your command prompt or terminal.

Here are the steps to add Python to the environment path:

#### For Windows:

* Open the Start menu and search for "Environment Variables".
* Select "Edit the system environment variables".
* Click on the "Environment Variables" button.
* Under "System variables", scroll down and select "Path", then click "Edit".
* Click "New" and add the path to your Python installation directory. It should look something like this: "C:\Python39" (without quotes).
* Click "OK" to close all the windows.
#### For Mac/Linux:

* Open your terminal.
* Type "nano ~/.bash_profile" (without quotes) and hit Enter.
* Add the following line to the file: "export PATH="/Library/Frameworks/Python.framework/Versions/3.9/bin:$PATH"" (without quotes). Make sure to replace "3.9" with the version of Python you installed.
* Press Ctrl+O to save the file and then Ctrl+X to exit nano.
* Run the command "source ~/.bash_profile" (without quotes) to update your terminal. 

#### Test if the environment is setup correctly:
You should now be able to run Python commands from any directory in your command prompt or terminal. You can test this by opening a new command prompt or terminal window and typing "python" (without quotes) to start the Python interpreter.

## 2. Harvest Token and Account ID
You will need a harvest token from you account to run the automation. Follow the below steps to extract the token
1. Login into harvest
2. Open this link: https://id.getharvest.com/oauth2/access_tokens/new
3. Enter a token name of your choice. For eg: harvest-personal-token
4. Click on: Create personal token
5. Copy your token value and store it safely. 
6. Also copy the Account ID and store it for later usage.


## 3. Clone the repo
    1. Clone the repo from this link:

## 4. Update the config
 1. Open config.ini in src/conf/ folder
 2. Update account_id value
 3. Update bearer_token value with token value from previous step
 4. Update the start date, end date.

## 5. Execute the Automation
 1. Run the bat file.
 2. Check the output folder for exported report.
