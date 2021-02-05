import numpy as np
import multiprocessing

def get_workers_count():
	return multiprocessing.cpu_count()

def main():
	print("You have " + str(get_workers_count()) + " worker(s) available.")

if __name__ == '__main__':
	main()
