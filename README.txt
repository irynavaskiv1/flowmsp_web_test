1) Run tests
   python3 -m venv venv
   source venv/bin/activate
   python -m unittest project.tests_main_page.py.MainPageTestCase

2) To use pdb ->
   from nose.tools import set_trace;set_trace()