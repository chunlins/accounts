# -*- coding: utf-8 -*-
""" Console app for managing accounts """


class Password(object):
    """ 存储加密字符串，并提供加密和解密功能 """
    def __init__(self, password):
        if __name__ == '__main__':
            self.value = self.encrypt(password)

    @staticmethod
    def encrypt(password):
        value = password
        return value

    @staticmethod
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
        记录账户密码，加密存储
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
        #  init user
        if isinstance(user, list):
            self.user = user
        else:
            self.user = [user]
        # init password
        self.password = Password(password)
        # init server
        if isinstance(server, dict):
            self.server = server
        else:
            self.server = {'url': server}
        # init history
        if history is None:
            self.history = []
        else:
            self.history = history
        # init auth
        if auth is None:
            self.auth = {}
        else:
            self.auth = auth

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
        return '{user} login {server}'.format(user=self.user, server=self.server.get('url'))

    def todict(self):
        return dict(
            user=self.user,
            password=self.password.value,
            server=self.server,
            history=self.history
        )


    # 修改账户并保存改动
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

    @staticmethod
    def _load_from_json(filename):
        return 'load from json'

    def load(self, accounts, file='json'):
        if file == 'json':
            self._load_from_json(accounts)
