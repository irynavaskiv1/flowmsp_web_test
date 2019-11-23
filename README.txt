This is a test case program that tests this site: https://app.flowmsp.com/my-profile .

1) Create environment
   python3 -m venv venv
   source venv/bin/activate

2) Run unit tests
   python -m unittest testing.test_unittest.test_main_page.BurgerMenuTestCase.testing_if_exist_burger_menu
   python -m unittest testing.test_unittest.test_profile_page.MyProfileTestCase.test_exist_my_profile_page


3) Run pytest tests
   py.test ./testing/test_pytest/test_main_page_pytest.py
   py.test ./testing/test_pytest/test_base_pytest.py
   pytest --durations=3


4) To use pdb
   from nose.tools import set_trace;set_trace()
   import pdb;pdb.set_trace()

5) Instalation on PC
   wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
   tar -zxvf geckodriver-v0.24.0-linux64.tar.gz
   chmod +x geckodriver
   sudo cp  geckodriver /usr/local/bin/

6) Load testing with locust
   locust --host=https://app.flowmsp.com
   locust --host=https://jsonplaceholder.typicode.com --locustfile tests/test_locust.py
   locust -f tests/test_locust.py --host=https://app.flowmsp.com