"""
Plot xy data from text file.
"""
from ._helpers import write


def main(argv=None):
    # Parse command line arguments.
    parser = _get_parser()
    args = parser.parse_args(argv)

    # plot
    write(args)
    print(args)
    return


def _get_parser():
    """Parse input options."""
    import argparse

    parser = argparse.ArgumentParser(
        description=("Make 2d pdf plot."), formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "--infile", "-i", default="all", type=str, help="text file to be read from"
    )

    parser.add_argument(
        "--outfile", "-o", default="output", type=str, help="mesh file to be written to"
    )

    parser.add_argument(
        "--x_label",
        "-x",
        default="Displacement (mm)",
        type=str,
        help="set x label",
    )

    parser.add_argument(
        "--y_label",
        "-y",
        default="Load (kN)",
        type=str,
        help="set y label",
    )

    return parser
