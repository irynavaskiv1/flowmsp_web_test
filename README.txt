1) Create environment
   python3 -m venv venv
   source venv/bin/activate

2) Run tests
   python -m unittest tests.tests_main_page.BurgerMenuTestCase

2) To use pdb
   from nose.tools import set_trace;set_trace()

3) Instalation on pc
   wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
   tar -zxvf geckodriver-v0.24.0-linux64.tar.gz
   chmod +x geckodriver
   sudo cp  geckodriver /usr/local/bin/
