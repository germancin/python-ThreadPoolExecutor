import numpy as np
import multiprocessing

def get_workers_count():
	return multiprocessing.cpu_count()

def main():
	print(get_workers_count())

if __name__ == '__main__':
	main()
