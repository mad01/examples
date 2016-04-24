#!/usr/bin/env python2
import click


@click.group(help='')
def ecli():
    pass


@ecli.group(help='')
def cmd1():
    pass


@ecli.group(help='')
def cmd2():
    pass


@cmd1.group(help='')
def foo():
    pass


@cmd2.group(help='')
def bar():
    pass


ecli.add_command(cmd1)
ecli.add_command(cmd2)

cmd1.add_command(foo)
cmd2.add_command(bar)


@foo.command('do_thing')
@click.option('-t', '--thing', help='', required=True)
def foo_do_thing(thing):
    click.echo(thing)


@bar.command('do_stuff')
@click.option('-s', '--stuff', help='', required=True)
def bar_do_stuff(stuff):
    click.echo(stuff)


if __name__ == '__main__':
    ecli()
