# GEO1000 - Assignment 4
# Authors:
# Student numbers:
import os
import statistics
import time
from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np

import psutil

python_command = "python assignment4/py/delaunay.py"
cpp_debug_command = "./assignment4/cpp/debug_exe"
cpp_release_command = "./assignment4/cpp/release_exe"

POINTS_NUMS = [100]
# POINTS_NUMS = [100, 200, 400, 800]


def main():
    # 1. run python
    # 2. run cpp debug
    # 3. run cpp release
    # 4. print results
    # 5. plot results
    ITER_NUM = 10
    for points_num in POINTS_NUMS:
        print(f"points num: {points_num}")
        [python_times, python_cpus, python_rams] = benchmark(
            "{0} {1}".format(python_command, points_num), ITER_NUM
        )
        [cpp_debug_times, cpp_debug_cpus, cpp_debug_rams] = benchmark(
            "{0} {1}".format(cpp_debug_command, points_num), ITER_NUM
        )
        # cpp_debug_times = benchmark(cpp_debug_command)
        # cpp_release_times = benchmark(cpp_release_command)

        py_time_stats = Stats(python_times)
        # py_cpu_stats = Stats(python_cpus)
        # py_ram_stats = Stats(python_rams)
        cpp_debug_stats = Stats(cpp_debug_times)
        # cpp_release_stats = Stats(cpp_release_times)

        plot_benchmarks(
            [py_time_stats, cpp_debug_stats],
            ["Python", "C++ debug"],
            f"{points_num}points time, {ITER_NUM} iterations",
        )
        print("python: {0}points time\n".format(points_num), py_time_stats)
        print("C++ Debug: {0}points time\n".format(points_num), cpp_debug_stats)
        # print("python: {0}points CPU\n".format(points_num), py_cpu_stats)
        # print("python: {0}points RAM\n".format(points_num), py_ram_stats)
    # print("cpp debug: ", cpp_debug_stats)
    # print("cpp release: ", cpp_release_stats)


def benchmark(command, iter_num=100):
    time_diffs = []
    cpu_usages = []
    ram_usages = []
    for _ in range(iter_num):
        start_time = time.perf_counter()
        os.system(command)
        end_time = time.perf_counter()
        # Calculate the difference
        time_diff = end_time - start_time
        time_diffs.append(time_diff)

        # start_time = time.perf_counter()
        # initial_cpu = psutil.cpu_percent(interval=1)
        # initial_ram = psutil.Process().memory_info().rss / 1024**2  # in MB
        # os.system(command)

        # end_time = time.perf_counter()
        # final_cpu = psutil.cpu_percent(interval=1)
        # final_ram = psutil.Process().memory_info().rss / 1024**2  # in MB

        # # Calculate the difference
        # time_diff = end_time - start_time
        # cpu_usage = final_cpu - initial_cpu
        # ram_usage = final_ram - initial_ram
        # time_diffs.append(time_diff)
        # cpu_usages.append(cpu_usage)
        # ram_usages.append(ram_usage)

    return (time_diffs, cpu_usages, ram_usages)


class Stats:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return f"ave: {self.ave()}\nmean: {self.mean()}\nmedian: {self.median()}\nstdev: {self.stdev()}\nmin: {self.min()}\nmax: {self.max()}"

    def ave(self):
        return sum(self.lst) / len(self.lst)

    def mean(self):
        return statistics.mean(self.lst)

    def median(self):
        return statistics.median(self.lst)

    def stdev(self):
        return statistics.stdev(self.lst)

    def min(self):
        return min(self.lst)

    def max(self):
        return max(self.lst)


def plot_benchmarks(stats_list: List[Stats], langs: List[str], title: str):
    metrics = ["ave", "mean"]
    x = np.arange(len(metrics))  # the label locations
    values = [
        [
            stats.ave(),
            stats.mean(),
            # stats.median(),
            # stats.stdev(),
            # stats.min(),
            # stats.max(),
        ]
        for stats in stats_list
    ]

    fig, ax = plt.subplots()

    width = 0.25
    multiplier = 0

    for i, value in enumerate(values):
        offset = width * multiplier
        rects = ax.bar(x + offset, value, width, label=langs[i])
        ax.bar_label(rects, padding=3)
        multiplier += 1

    ax.set_title(title)
    # ax.set_xticks(x + width, len(labels))
    ax.set_xticklabels(metrics)
    ax.set_ylabel("time (s)")
    ax.legend(loc="upper right", ncol=2)
    plt.savefig(f"{title}.png", format="png", dpi=300)
    plt.show()


def run_python():
    pass


if __name__ == "__main__":
    main()
