# -*- coding: utf-8 -*-
""" Console app for managing accounts """
import json


def encrypt(password):
    value = password
    return value


def deciphering(value):
    password = value
    return password


class Account(object):
    """ 存储账户信息

    不验证输入信息的正确性，由用户自己确认和核实输入

    Parameters
    ----------
    user: list or str
        记录用户基本信息，至少是必须的，而且可入是多个登陆名
    password: str
        记录加密后的账户密码
    server: dict or str
        记录提供该账户服务的公司或机构，登陆时使用的服务地址是必须的
    auth: dict of authentications, optional
        记录在注册该账户时使用的认证方式，例如注册时的邮箱和电话号码，信息存放在字典中，
        可接受键包括： ['phone', 'email', 'qq', 'wechat']
    history: list of dict, optional
        记录账户的改动，在每次对账户进行修改后，将改动前的账户信息记录其中

    Notes
    -----
    Account:
        base info format: username&password@server
        base: [user.name, password, server.url, auth]
        user: dict - {'name': 'log_in_name', 'option' = 'other_log_in_name' ...}
        password: Password
        server: dict - {'name': 'verbose_name', 'url': 'https://example.org' ...}
        auth: list - [authentications]
        authentications: {'email': 'username@example.com' ... }
        history: list - [account.base]

    """

    def __init__(self, user, password, server, auth=None, history=None):
        self.user = user if isinstance(user, list) else [user]
        self.password = password
        self.server = server if isinstance(server, dict) else {'url': server}
        self.history = history if history else list()
        self.auth = auth if auth else dict()

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
        return '{user} login {server}'.format(user=' '.join(self.user),
                                              server=self.server.get('url'))

    def todict(self):
        return dict(
            user=self.user,
            password=self.password,
            server=self.server,
            history=self.history,
            auth=self.auth
        )


    # 修改账户并保存改动
    def recode(self):
        pass

    def modify(self, user=None, password=None, server=None):
        pass

    def commit(self):
        pass


class AccountManager(object):
    """ Collections contains Account instances

    Parameters
    ----------
    _data : list
        Store account data

    """

    def __init__(self):
        self._data = []

    def __iter__(self):
        return (account for account in self._data)

    def __str__(self):
        return str(self._data)

    @property
    def amount(self):
        return len(self._data)

    def add(self, account):
        self._data.append(account)

# Data Persistent: load from and dump to file(json)

    def _load_from_json(self, file):
        account_data = json.load(file)
        for data in account_data:
            self.add(Account(**data))

    def load(self, filename, format='json'):
        # TODO: test and verify filename
        file = open(filename, 'r', encoding='utf-8')

        if format == 'json':
            self._load_from_json(file)

    def _dump_to_json(self, file):
        account_data = [account.todict() for account in self._data]
        json.dump(account_data, file)

    def dump(self, filename, format='json'):
        # TODO: test and verify filename
        file = open(filename, 'w', encoding='utf-8')

        if format == 'json':
            self._dump_to_json(file)
