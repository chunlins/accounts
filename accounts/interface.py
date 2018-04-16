#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Command Line Interface for project accounts
    
    Usage:
        
        # 添加账户基本信息
        accounts add [username, password, server]

        # 从文件中添加多个账户信息
        # --type : 指定读取的文件类型
        accounts load [file] --type='json'
"""

import click
from .core import Account, AccountManager


@click.group()
def accounts():
    pass


@click.command()
def new():
    """ 引导用户创建新的账户记录 """
    pass


@click.command()
@click.argument('user')
@click.argument('password')
@click.argument('server')
# @click.option('--auth', defaul=None)
def add(user, password, server):
    """ Accept user input from console, and add it into accounts
    Usage:
        accounts add user password server --auth=<auth-account>
    """
    manager = AccountManager()
    # input may be valid or not and now i choose to believe user
    account = Account(user, password, server)
    manager.add(account)
    click.echo(account)


@click.command()
@click.argument('file', type=click.File('r'))
@click.option('--file-type', default='json')
def load(file, file_type):
    if file_type == 'json':
        import json
        dataset = json.load(file)
    else:
        dataset = []

    manager = AccountManager()
    for data in dataset:
        account = Account(
            data.get('user'), data.get('password'), data.get('server'))
        manager.add(account)
    click.echo('accounts info has loaded.')


accounts.add_command(new)
accounts.add_command(add)
accounts.add_command(load)


if __name__ == '__main__':
    accounts()
