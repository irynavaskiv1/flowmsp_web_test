1) Create environment
   python3 -m venv venv
   source venv/bin/activate

2) Run tests
   python -m unittest tests.tests_main_page.FilterTestCase.testing_if_filter_exist
   python -m unittest tests.tests_profile_page.MyProfileTestCase.testing_change_password_button
   python -m unittest tests.tests_main_page.BurgerMenuTestCase.testing_building_data_button
   python -m unittest tests.tests_filters.FilterTestCase.testing_if_work_back_button
   python -m unittest tests.tests_account_info.AccountInfoTestCase.testing_edit_account_info_button
   python -m unittest tests.tests_upload_data.UploadDataTestCase.testing_all_pages

2) To use pdb
   from nose.tools import set_trace;set_trace()

3) Instalation on PC
   wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
   tar -zxvf geckodriver-v0.24.0-linux64.tar.gz
   chmod +x geckodriver
   sudo cp  geckodriver /usr/local/bin/

4) Load testing with locust
   locust --host=https://app.flowmsp.com
   locust --host=https://jsonplaceholder.typicode.com --locustfile tests/test_locust.py
   locust -f tests/test_locust.py --host=https://app.flowmsp.com