"""SRIFFS - machine-learning-production

Usage:
    sriffs-cli lorem <iterations> [--text-size=<text_size>]
    sriffs-cli data <data-url> <data-location>
    sriffs-cli (-h | --help)

Arguments:
    <data-location>         Location to save the data file
    <data-url>              Location of the data file to download
    <iterations>            Number of times the text will be repeated

Options:
    --text-size=<text_size>    Lorem ipsum text size. [default: 50]
    -h --help                   Show this screen.
"""

from docopt import docopt

from sriffs.operator.data import get_data
from sriffs.operator.generator import generate


def main():
    arguments = docopt(__doc__)

    if arguments['lorem']:
        print(generate(arguments['<iterations>'], arguments['--text-size']))
    elif arguments['data']:
        get_data(arguments['<data-url>'], arguments['<data-location>'])


if __name__ == '__main__':
    main()
