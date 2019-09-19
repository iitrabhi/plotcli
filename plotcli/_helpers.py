import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use("pdf")


def write(infile, outfile, label):
    plotter = Plotter(infile, outfile, label)
    plotter.set_labels()
    plotter.plot()
    pass


class Plotter:
    def __init__(self, infile, outfile, label):
        self.infile = infile
        self.outfile = outfile
        self.label = label
        self.initialize_plot()

    def initialize_plot(self):
        # width as measured in inches
        ar = 1.618  # aspect ratio
        _width = 3.5
        _height = _width / ar
        _size_primary = 12
        _size_secondary = 8
        mpl.font_manager._rebuild()

        plt.rcParams["font.family"] = "serif"
        plt.rcParams["font.serif"] = "Times"
        plt.rc("text", usetex=True)
        plt.rc("xtick", labelsize=_size_secondary)
        plt.rc("ytick", labelsize=_size_secondary)
        plt.rc("axes", labelsize=_size_primary)
        plt.rc("legend", fontsize=_size_secondary)

        self.fig, self.ax = plt.subplots()
        self.fig.subplots_adjust(
            left=0.18, bottom=0.15 * ar, right=0.95, top=(1 - 0.05 * ar)
        )
        self.fig.set_size_inches(_width, _height)

    def set_labels(self):
        self.ax.set_ylabel("Load (kN)")
        self.ax.set_xlabel("Displacement (mm)")

    def plot(self):
        _linewidth = 2.0
        x, y = np.loadtxt(self.infile, unpack=True)
        plt.plot(x, y, linewidth=_linewidth, label=self.label)
        plt.legend()
        plt.grid()
        self.fig.savefig(self.outfile + ".pdf")
