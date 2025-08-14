MultiProcessing
Runs code in separate CPU processes. Useful for CPU-bound tasks (like heavy calculations) — better performance than threads.

Use case:
Image processing, data transformation, ML training.
Library
import multiprocessing
Also a mini project
#Image Auto Downloader using Python Multiprocessing Python project that demonstrates how to download multiple images **concurrently** using the `multiprocessing` module and `concurrent.futures.ProcessPoolExecutor`.
#Features

Downloads high-resolution random images from https://picsum.photos
Uses multiprocessing for parallel downloads
#Concepts Used

multiprocessing module
ProcessPoolExecutor from concurrent.futures
HTTP requests with requests
File handling and exception handling in Python