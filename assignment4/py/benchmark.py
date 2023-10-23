# GEO1000 - Assignment 4
# Authors:
# Student numbers:
import os
import statistics
import time
from typing import List
import matplotlib.pyplot as plt
import numpy as np

import psutil

python_command = "python assignment4/py/delaunay.py"
cpp_debug_command = "./assignment4/cpp/debug.exe"
cpp_release_command = "./assignment4/cpp/release.exe"

# POINTS_NUMS = [100]
POINTS_NUMS = [100, 200, 400, 800]


def main():
    ITER_NUM = 10
    for points_num in POINTS_NUMS:
        print(f"points num: {points_num}")
        [py_time_stats, py_cpu_stats, py_ram_stats] = benchmark(
            "{0} {1}".format(python_command, points_num), ITER_NUM
        )
        [cpp_debug_time_stats, cpp_debug_cpu_stats, cpp_debug_ram_stats] = benchmark(
            "{0} {1}".format(cpp_debug_command, points_num), ITER_NUM
        )
        [
            cpp_release_time_stats,
            cpp_release_cpu_stats,
            cpp_release_ram_stats,
        ] = benchmark("{0} {1}".format(cpp_release_command, points_num), ITER_NUM)

        plot_benchmarks(
            [py_time_stats, cpp_debug_time_stats, cpp_release_time_stats],
            ["Python", "C++ debug", "C++ release"],
            f"Time of execution ({points_num}points, {ITER_NUM} iterations)",
            f"{points_num}points_{ITER_NUM}iter",
        )


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

    return (Stats(time_diffs), Stats(cpu_usages), Stats(ram_usages))


class Stats:
    def __init__(self, lst, round_num=2):
        self.lst = lst
        self.round_num = round_num

    def __str__(self):
        return f"ave: {self.ave()}\nmedian: {self.median()}\nstdev: {self.stdev()}\nmin: {self.min()}\nmax: {self.max()}"

    def ave(self):
        return round(sum(self.lst) / len(self.lst), self.round_num)

    def median(self):
        return round(statistics.median(self.lst), self.round_num)

    def stdev(self):
        return round(statistics.stdev(self.lst), self.round_num)

    def min(self):
        return round(min(self.lst), self.round_num)

    def max(self):
        return round(max(self.lst), self.round_num)


def plot_benchmarks(
    stats_list: List[Stats], langs: List[str], title: str, filename: str
):
    stat_metrics = [
        "ave",
        "median",
    ]
    x = np.arange(len(stat_metrics))  # the label locations
    values = [
        [
            stats.ave(),
            stats.median(),
        ]
        for stats in stats_list
    ]

    _fig, ax = plt.subplots()

    width = 0.25
    multiplier = 0

    for i, value in enumerate(values):
        offset = width * multiplier
        rects = ax.bar(x + offset, value, width, label=langs[i])
        ax.bar_label(rects, padding=3)
        multiplier += 1

    ax.set_title(title, y=-0.15)
    ax.set_xticks(x + width, stat_metrics)
    ax.set_xticklabels(stat_metrics)
    ax.set_ylabel("time (s)")
    ax.legend(loc="upper right", bbox_to_anchor=(1, 1.15), ncols=len(langs))

    plt.savefig(f"{filename}.png", format="png", dpi=300, bbox_inches="tight")


def run_python():
    pass


if __name__ == "__main__":
    main()
