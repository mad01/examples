import click
from prom_exporter.handler import falcon_app


@click.group(help='')
def cli():
    pass


@click.command()
@click.option('-s', '--service', help='service name', required=True, type=str)
@click.option('-u', '--url', help='url to collect from', required=True, type=str)
@click.option('-p', '--port', help='', required=True, type=int)
@click.option('-e', '--exclude', help='exclude metrics named', multiple=True)
def start(service, url, port, exclude):
    falcon_app(url, service, port=port, exclude=list(exclude))


cli.add_command(start)


if __name__ == '__main__':
    cli()
