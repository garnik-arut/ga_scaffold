"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         isqrt = ga_scaffold.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``isqrt`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This file can be renamed depending on your needs or safely removed if not needed.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import argparse
import logging
import sys
from ctypes import POINTER, byref, c_float, c_int32, cast

from ga_scaffold import __version__

__author__ = "Garnik-Arut"
__copyright__ = "Garnik-Arut"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


# ---- Python API ----
# The functions defined in this section can be imported by users in their
# Python scripts/interactive interpreter, e.g. via
# `from ga_scaffold.skeleton import isqrt`,
# when using this Python module as a library.


def isqrt(n):
    """Fast inverse square root
    based on John Carmack's algorythm in C
    https://en.wikipedia.org/wiki/Fast_inverse_square_root

    Args:
      n (float): float

    Returns:
      float: n ** (-2)
    """
    assert n > 0
    x2 = n * 0.5  # half the number
    y = c_float(n)  # cast to float (just in case its integer)

    i = cast(byref(y), POINTER(c_int32)).contents.value  # Cast to int
    i = c_int32(0x5F3759DF - (i >> 1))  # Memory hack
    y = cast(byref(i), POINTER(c_float)).contents.value  # Cast back

    y = y * (1.5 - (x2 * y * y))  # do the first Newton iteration
    return y


# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Just a Fast inverse square root demo")
    parser.add_argument(
        "--version",
        action="version",
        version=f"ga_scaffold {__version__}",
    )
    parser.add_argument(
        dest="n", help="number to fast inverse square root ", type=int, metavar="NUMBER"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    # good practice
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    # Seed for NN applications
    # parser.add_argument(dest="seed",
    #                       help="seed to stay sane",
    #                       type=int, metavar="SEED")
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    # Classical
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    # Later add IDEA logs format
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(args):
    """
    Wrapper allowing :func:`isqrt` to be called with string arguments in a CLI fashion

    Instead of returning the value from :func:`isqrt`, it prints the result to the
    ``stdout`` in a nicely formatted message.

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "42"]``).
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    print(f"The fast inverse square root of {args.n} is {isqrt(args.n)}")
    _logger.info("Script ends here")


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m ga_scaffold.skeleton 16
    #
    run()
