import matplotlib.pyplot as plt
import chart_studio
from . import general

def plot(lines, background = None):
    for line in lines:
        plt.plot([line.start_position[1],line.end_position[1]],
                [line.start_position[0],line.end_position[0]],
                linestyle = '-',
                linewidth = line.width,
                color = line.color)
    plt.axis('equal')
    plt.axis('off')
    #plt.facecolor(background)

def save_image(matplot_plt, filename):
    matplot_plt.savefig(f'output/{filename}.png')
    return f'output/{filename}.png'


def to_plotly(self, background = None):
    mpl_fig = plt.figure()
    return chart_studio.plotly.plot_mpl(mpl_fig)


def run_animation(system, iterations, interval, background = None):
    for i in range(iterations):
        system.step()
        system.plot(background)
        plt.show()
        plt.pause(interval)

def save_animation(system, filename, iterations, background = None):
    general.verify_or_create_folder(filename)
    for i in range(iterations):
        system.step()
        system.plot()
        plt.savefig(f'output/{filename}/{filename}_{i}.png', facecolor=background)
        plt.show()


def run(self, iterations, background = None):
    for i in range(iterations):
        self.step()
    self.plot(background)