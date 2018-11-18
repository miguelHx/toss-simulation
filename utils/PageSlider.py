import matplotlib.widgets
import matplotlib.patches
import mpl_toolkits.axes_grid1


class PageSlider(matplotlib.widgets.Slider):

    def __init__(self, ax, label, numpages = 10, valinit=0, valfmt='%1d',
                 closedmin=True, closedmax=True,
                 dragging=True, **kwargs):
        self.facecolor = kwargs.get('facecolor',"w")
        self.activecolor = kwargs.pop('activecolor',"b")
        self.fontsize = kwargs.pop('fontsize', 10)
        self.numpages = numpages

        super(PageSlider, self).__init__(ax, label, 0, numpages,
                            valinit=valinit, valfmt=valfmt, **kwargs)

        self.poly.set_visible(False)
        self.vline.set_visible(False)
        self.pageRects = []
        for i in range(numpages):
            facecolor = self.activecolor if i==valinit else self.facecolor
            r  = matplotlib.patches.Rectangle((float(i)/numpages, 0), 1./numpages, 1,
                                transform=ax.transAxes, facecolor=facecolor)
            ax.add_artist(r)
            self.pageRects.append(r)
            ax.text(float(i)/numpages+0.5/numpages, 0.5, str(i+1),
                    ha="center", va="center", transform=ax.transAxes,
                    fontsize=self.fontsize)
        self.valtext.set_visible(False)

        divider = mpl_toolkits.axes_grid1.make_axes_locatable(ax)
        bax = divider.append_axes("right", size="5%", pad=0.05)
        fax = divider.append_axes("right", size="5%", pad=0.05)
        self.button_back = matplotlib.widgets.Button(bax, label=r'<',
                        color=self.facecolor, hovercolor=self.activecolor)
        self.button_forward = matplotlib.widgets.Button(fax, label=r'>',
                        color=self.facecolor, hovercolor=self.activecolor)
        self.button_back.label.set_fontsize(self.fontsize)
        self.button_forward.label.set_fontsize(self.fontsize)
        self.button_back.on_clicked(self.backward)
        self.button_forward.on_clicked(self.forward)
        self.on_changed(self._update)

    def _update(self, event):
        if type(event).__name__ != 'int' and type(event).__name__ != 'float64':
            super(PageSlider, self)._update(event)
        i = int(self.val)
        if i >= self.valmax:
            return
        self._colorize(i)

    def _colorize(self, i):
        for j in range(self.numpages):
            self.pageRects[j].set_facecolor(self.facecolor)
        self.pageRects[i].set_facecolor(self.activecolor)

    def forward(self, event):
        current_i = int(self.val)
        i = current_i+1
        if (i < self.valmin) or (i >= self.valmax):
            return
        self._colorize(i)
        self.set_val(i)
        # self._update(event)

    def backward(self, event):
        current_i = int(self.val)
        i = current_i-1
        if (i < self.valmin) or (i >= self.valmax):
            return
        self._colorize(i)
        self.set_val(i)
        # self._update(event)


if __name__ == "__main__":
    import numpy as np
    from matplotlib import pyplot as plt

    t = 10
    num_pages = t
    data = np.random.rand(9, 9, num_pages)

    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.25)

    im = ax.imshow(data[:, :, 0], cmap='viridis', interpolation='nearest', origin="lower")

    ax_slider = fig.add_axes([0.1, 0.07, 0.8, 0.04])
    ax_slider2 = fig.add_axes([0.1, 0.02, 0.8, 0.04])
    slider = PageSlider(ax_slider, 'Page', num_pages, activecolor="orange")
    slider2 = PageSlider(ax_slider2, 'Size', data.shape[0], valinit=8, activecolor="yellow")

    def update(val):
        i = int(slider.val)
        j = int(slider2.val)
        im.set_data(data[:j+1,:j+1,i])
        im.set_extent([-0.5,j+0.5,-0.5,j+0.5])
        fig.canvas.draw()


    slider.on_changed(update)
    slider2.on_changed(update)

    plt.show()
