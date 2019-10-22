from locust import HttpLocust, TaskSet


def login(l):
    l.client.post('/login', {'username': 'aa@aa.aa',
                             'password': 'aaaaaa'})


def logout(l):
    l.client.post('/logout', {'username': 'aa@aa.aa',
                              'password': 'aaaaaa'})


def index(l):
    l.client.get('/')


def profile(l):
    l.client.get('/my-profile')


class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000
