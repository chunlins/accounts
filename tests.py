# -*- coding = utf-8 -*-

import unittest
from accounts.core import Account, AccountManager


class TestAccount(unittest.TestCase):

    def test_dump_init_account_to_dict(self):
        expect = {'user': 'example', 'password': 'password',
                  'server': 'example.com', 'history': []}
        account = Account(**expect)
        result = account.dump()

        self.assertEqual(expect, result)

    def test_dump_modified_account_to_dict(self):
        expect = {'user': 'user', 'password': 'password', 'server': 'example.com',
                  'history': [{'user': 'user', 'password': 'modified', 'server': 'example.com'}]}
        account = Account(**expect)
        result = account.dump()

        self.assertEqual(expect, result)

    def test_load_from_dict(self):
        example = {'user': 'user', 'password': 'password', 'server': 'example.com',
                   'history': [{'user': 'user', 'password': 'modified', 'server': 'example.com'}]}
        expect = Account(**example)
        result = Account.load(example)

        self.assertEqual(expect, result)
        self.assertEqual(expect.history, result.history)

    def test_load_from_dict_dumped(self):
        example = {'user': 'user', 'password': 'password', 'server': 'example.com',
                   'history': [{'user': 'user', 'password': 'modified', 'server': 'example.com'}]}
        expect = Account(**example)
        dumped = expect.dump()
        result = Account.load(dumped)

        self.assertEqual(expect, result)
        self.assertEqual(expect.history, result.history)
