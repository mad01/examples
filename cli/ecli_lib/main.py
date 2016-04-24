#!/usr/bin/env python2
import click


@click.group(help='')
def ecli():
    pass


@click.command('thing')
@click.option('-t', '--thing', help='', required=True)
def bar(thing):
    click.echo(thing)


@click.command('stuff')
@click.option('-s', '--stuff', help='', required=True)
def foo(stuff):
    click.echo(stuff)


ecli.add_command(foo)
ecli.add_command(bar)


if __name__ == '__main__':
    ecli()
