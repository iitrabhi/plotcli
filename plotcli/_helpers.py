import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import subprocess, os, platform
import sys

mpl.use("pdf")


def write(args):
    plotter = Plotter(args.infile, args.outfile)
    plotter.set_labels(args.x_label, args.y_label)
    plotter.plot()
    pass


class Plotter:
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
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
        plt.rcParams["mathtext.fontset"] = "stix"
        plt.rcParams["font.family"] = "STIXGeneral"
        plt.rc("xtick", labelsize=_size_secondary)
        plt.rc("ytick", labelsize=_size_secondary)
        plt.rc("axes", labelsize=_size_primary)
        plt.rc("legend", fontsize=_size_secondary)

        self.fig, self.ax = plt.subplots()
        self.fig.subplots_adjust(
            left=0.18, bottom=0.15 * ar, right=0.95, top=(1 - 0.05 * ar)
        )
        self.fig.set_size_inches(_width, _height)

    def set_labels(self, x_lable, y_lable):
        self.ax.set_xlabel(x_lable)
        self.ax.set_ylabel(y_lable)

    def plot(self):
        _linewidth = 2.0
        try:
            if self.infile == "all":  # ToDo: make a good qualifier
                for file in os.listdir(os.getcwd()):
                    if file.endswith(".txt"):
                        print(file[:-4])
                        x, y = np.loadtxt(file, unpack=True)
                        plt.plot(x, y, linewidth=_linewidth, label=file[:-4])
            else:
                x, y = np.loadtxt(self.infile, unpack=True)
                plt.plot(x, y, linewidth=_linewidth, label=self.infile[:-4])
        except:
            print("File not found 😱")
            sys.exit(1)
        plt.legend()
        plt.grid()
        # plt.show()
        try:
            self.fig.savefig(self.outfile + ".pdf")

            filepath = self.outfile + ".pdf"
            if platform.system() == "Darwin":  # macOS
                subprocess.call(("open", filepath))
            elif platform.system() == "Windows":  # Windows
                os.startfile(filepath)
            else:  # linux variants
                subprocess.call(("xdg-open", filepath))
            print("Image created! 🎉🥳")
        except:
            print("There was some error 😱")
