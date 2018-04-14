# -*- coding: utf-8 -*-

""" Console app for managing accounts """


# use dict or Account class to store accounts message.
class Account(object):
    """ Store information of the account """

    # base info format: username&password@server
    def __init__(self, user, password, server):
        self.user = user
        self.password = password
        self.server = server
        # todo to record account's history by collect every change
        self.history = {password: None}

    def __str__(self):
        return ' '.join([self.user, self.server])

    def todict(self):
        return dict(user=self.user, password=self.password, server=self.server)


class AccountManager(object):
    """ Collections contains Account instances """

    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.data)

    def add(self, account):
        self.data.append(account)

    def _load_from_json(self, filename):
        return 'load from json'

    def load(self, accounts, file='json'):
        if file == 'json':
            self._load_from_json(accounts)
