import matplotlib.animation as ani
import matplotlib.pyplot as plt
import random


def selection_sort(array):
    for cur_idx in range(len(array)):
        min_idx = cur_idx
        for next_idx in range(cur_idx + 1, len(array)):
            if array[min_idx] > array[next_idx]:
                min_idx = next_idx
        # once/if the minimum index has been found swap
        array[cur_idx], array[min_idx] = array[min_idx], array[cur_idx]
        yield array


if __name__ == '__main__':
    # Setup plot and randomly shuffled array of numbers
    fig, ax = plt.subplots()
    ax.set_title('Sorting')
    N = 100
    array = [num for num in range(N)]
    random.shuffle(array)
    bars = ax.bar(x=range(len(array)), height=array, width=1, align='edge')
    array_gen = selection_sort(array)

    def update(array, plt_bars):  # create the updating func for animation
        """
        :param array: next value of frames in our case it will just be a copy of the array
        :param plt_bars: list of bars we are modifying
        """
        for height_val, bar in zip(array, plt_bars):
            bar.set_height(height_val)

ani = ani.FuncAnimation(plt.gcf(), func=update, fargs=(bars,), frames=array_gen, interval=10, repeat=False)
plt.show()
