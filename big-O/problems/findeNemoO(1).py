from time import perf_counter

arr = ["nemo"] * 10000000

def find_nemo(arr: list[str]):
    start = perf_counter()

    print(f"Found - {arr[0]}") # O(1)
    print(f"Found - {arr[1]}") # O(1)

    end = perf_counter()

    print(f"Time taken for execution = {end - start:.4f}")

find_nemo(arr)