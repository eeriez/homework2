import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name) as f:
        for line in f:
            all_data.append(line.replace('\n', ''))
    return all_data


file_names = [f'file {i}.txt' for i in range(1, 5)]

linear_start_time = datetime.now()
for file in file_names:
    read_info(file)
linear_end_time = datetime.now()
print(linear_end_time - linear_start_time)

multi_start_time = datetime.now()
if __name__ == '__main__':
    with multiprocessing.Pool(processes=2) as pool:
        pool.map(read_info, file_names)
multi_end_time = datetime.now()
print(multi_end_time - multi_start_time)
