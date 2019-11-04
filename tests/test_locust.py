from locust import HttpLocust, TaskSet, task
import json


class UserBehavior(TaskSet):

    def __init__(self, parent):
        super(UserBehavior, self).__init__(parent)

        self.token = 'eyJhbGciOiJIUzI1NiJ9.eyIkaW50X3Blcm1zIjpbXSwic3ViIjoib' \
                     '3JnLnBhYzRqLmNvcmUucHJvZmlsZS5Db21tb25Qcm9maWxlIzIwN2N' \
                     'kNWVmLTJmM2MtNDJmYS1iODc1LTczMzNiYTRhZTQ0NSIsImxpY2Vuc' \
                     '2VUeXBlIjoiUHJldmlldyIsImN1c3RvbWVySWQiOiI0MDcxNjZmMC1' \
                     'jZTYzLTQxZjgtOTE5MC03ZjUyMGVjZDM1NGIiLCIkaW50X3JvbGVzI' \
                     'jpbIkFETUlOIl0sImlhdCI6MTU3MTc2OTAzMSwic2x1ZyI6ImFhYWF' \
                     'hYSIsInVzZXJuYW1lIjoiYWFAYWEuYWEifQ.bOvsNMjT0K6SxH1zrE' \
                     'Zc4qH86MiUn2np2WmmrPO1odg'
        self.headers = {json}

    def on_start(self):
        self.token = self.login()
        self.headers = {'Authorization': 'Token ' + self.token}

    def login(self):
        response = self.client.post('/login', data={'email': 'aa@aa.aa',
                                                    'password': 'aaaaaa',
                                                    'Login': 'Login'})
        return json.loads(response._content)['key']

    @task(2)
    def index(self):
        self.client.get("/login", headers=self.headers)

    @task(1)
    def profile(self):
        self.client.get("/my-profile/", headers=self.headers)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
