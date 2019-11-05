1) Create environment
   python3 -m venv venv
   source venv/bin/activate

2) Run unit tests
   python -m unittest testing.tests_unittest.tests_profile_page.MyProfileTestCase.testing_change_password_button


3) Run pytest tests
   pytest -k "MainPageTestCase"
   pytest testing::test_unittest::test_main_page_pytest.py::MainPageTestCase::test_if_login_works



4) To use pdb
   from nose.tools import set_trace;set_trace()

5) Instalation on PC
   wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
   tar -zxvf geckodriver-v0.24.0-linux64.tar.gz
   chmod +x geckodriver
   sudo cp  geckodriver /usr/local/bin/

6) Load testing with locust
   locust --host=https://app.flowmsp.com
   locust --host=https://jsonplaceholder.typicode.com --locustfile tests/test_locust.py
   locust -f tests/test_locust.py --host=https://app.flowmsp.com