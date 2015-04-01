"""Program entry point!"""
import click


@click.command()
@click.argument('name')
def keymaker(name):
    """Greets ya!"""
    print("Hello, {}.".format(name))


if __name__ == '__main__':
    keymaker()
