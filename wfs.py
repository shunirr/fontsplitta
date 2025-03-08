import click

from modules import split
from modules import test_server
from modules import google_fonts


@click.group()
def cli():
    pass


def main():
    cli.add_command(split.split)
    cli.add_command(test_server.test_server)
    cli.add_command(google_fonts.get_unicode_ranges_from_google_fonts)
    cli()


if __name__ == "__main__":
    main()
