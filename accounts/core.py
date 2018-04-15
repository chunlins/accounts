# -*- coding: utf-8 -*-
""" Console app for managing accounts """


class Account(object):
    """ Store information of the account """

    def __init__(self, user, password, server, history=None):
        # base info format: username&password@server
        # history is list of modified account, account is dict of base info.
        self.user = user
        self.password = password
        self.server = server
        if history is None:
            self.history = []
        else:
            self.history = history

    def __eq__(self, other):
        if isinstance(other, Account):
            if (self.user == other.user and
                self.password == other.password and
                self.server == other.server):
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        return '{user} in {server}'.format(user=self.user, server=self.server)

    def dump(self):
        return dict(
            user=self.user,
            password=self.password,
            server=self.server,
            history=self.history
        )

    @staticmethod
    def load(account: dict):
        return Account(**account)


    def recode(self):
        pass

    def modify(self, user=None, password=None, server=None):
        pass

    def commit(self):
        pass

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
