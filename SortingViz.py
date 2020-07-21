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
    yield from array


if __name__ == '__main__':
    # Setup plot and randomly shuffled array of numbers
    fig, ax = plt.subplots()
    ax.set_title('Sorting')
    N = 300
    array = [num for num in range(N)]
    random.shuffle(array)
    bars = ax.bar(x=range(len(array)), height=array, width=1, align='edge')
    array_gen = selection_sort(array)
    bars = list(bars)
    bars.reverse() # want to sort least to greatest


    def update(array_val, plt_bars):  # create the updating func for animation
        """
        :param array_val: next value of frames in our case it will just be next value in array
        :param plt_bars: list of bars we are modifying
        """
        cur_bar = plt_bars.pop()
        cur_bar.set_height(array_val)

ani = ani.FuncAnimation(plt.gcf(), func=update, fargs=(bars,), frames=array_gen, interval=8, repeat=False)
plt.show()
