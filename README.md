This is our repo for the finance stocks app. 
Please follow below steps in order to get the app running:

step1: 
- Open your terminal and run the command: git clone https://github.com/danpopaa/itschool_myfinance.git 

step2: 
- Create a new virtual environment:
   File -> Settings -> Create a folder with your Project "Name" -> Python Interpreter -> Add new -> Select project folder -> Make a subdirectory called venv -> Apply and OK 

step3: 
- Install python packages required to be able to run the app using the command line in terminal: pip install - r requirements.txt
- Make sure you are executed the command while in directory Project "Name"

step4:
- Start uvicorn server: uvicorn my_finance.index:app --reload --port 7777
- Open in browser page: http://127.0.0.1:7777/docs
