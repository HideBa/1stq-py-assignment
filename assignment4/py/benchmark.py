# GEO1000 - Assignment 4
# Authors:
# Student numbers:


import os
import statistics
import time

import psutil

python_command = "python assignment4/py/delaunay.py"
cpp_debug_command = "./assignment4/cpp/debug_exe"
cpp_release_command = "./assignment4/cpp/release_exe"

POINTS_NUMS = [100, 200, 400, 800]


def main():
    # 1. run python
    # 2. run cpp debug
    # 3. run cpp release
    # 4. print results
    # 5. plot results

    for points_num in POINTS_NUMS:
        print(f"points num: {points_num}")
        [python_times, python_cpus, python_rams] = benchmark(
            "{0} {1}".format(python_command, points_num), 100
        )
        # cpp_debug_times = benchmark(cpp_debug_command)
        # cpp_release_times = benchmark(cpp_release_command)

        py_time_stats = Stats(python_times)
        py_cpu_stats = Stats(python_cpus)
        py_ram_stats = Stats(python_rams)
        # cpp_debug_stats = Stats(cpp_debug_times)
        # cpp_release_stats = Stats(cpp_release_times)

        print("python: {0}points time\n".format(points_num), py_time_stats)
        print("python: {0}points CPU\n".format(points_num), py_cpu_stats)
        print("python: {0}points RAM\n".format(points_num), py_ram_stats)
    # print("cpp debug: ", cpp_debug_stats)
    # print("cpp release: ", cpp_release_stats)


def benchmark(command, iter_num=100):
    time_diffs = []
    cpu_usages = []
    ram_usages = []
    for _ in range(iter_num):
        start_time = time.perf_counter()
        initial_cpu = psutil.cpu_percent(interval=1)
        initial_ram = psutil.Process().memory_info().rss / 1024**2  # in MB
        os.system(command)

        end_time = time.perf_counter()
        final_cpu = psutil.cpu_percent(interval=1)
        final_ram = psutil.Process().memory_info().rss / 1024**2  # in MB

        # Calculate the difference
        time_diff = end_time - start_time
        cpu_usage = final_cpu - initial_cpu
        ram_usage = final_ram - initial_ram
        time_diffs.append(time_diff)

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


def run_python():
    pass


if __name__ == "__main__":
    main()
