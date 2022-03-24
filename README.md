# nop_auto_demo
This for auto demo only
- This framework using python, pytest and selenium to automate for the site
- The scenario is below: 
  - script will open site, click on register page and click Register
  - After that test will check register successful or not based on sucessfull message back
How to run test:
- Install python 3: https://www.python.org/downloads/
- Install pipenv: https://pipenv-fork.readthedocs.io/en/latest/install.html
- clone repo and then run: pipenv shell
- Then to install required packages: pipenv install
- Check packages are installed successfully and listed in virtual env by: pip list, sample as below:
- <img width="541" alt="image" src="https://user-images.githubusercontent.com/32532761/159877513-f0b7b7a9-c0e8-450b-9cd9-0253972bfa02.png">
- Setup python interpreter for you IDE, I'm using VS code so, click Shift + cmd + P -> select virtualenv of previous step
- Setup test by select Shift + CMD + P: select pytest
- Then run command: python -m pytest tests/
-> this will run test with scenario, and I use Faker to generate data test -> everytime, tests run, it will use a unique input

- How to run html report:
  python -m pytest tests/ --html report.html -> there will be a html report in root folder


