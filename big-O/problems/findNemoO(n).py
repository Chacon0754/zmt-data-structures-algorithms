
from time import perf_counter

nemo = ["nemo"]
everyone = ["dory", "bruce", "marlin", "nemo", "gill", "bloat", " nigel", "squirt", "darla"]
large_arr = ["nemo"] * 10000

def find_nemo(arr: list[str]) -> None:
    start = perf_counter()

    for name in arr:
        if name  == "nemo":
            print(f"Found - {name}")
    
    end = perf_counter()

    print(f"Time taken for execution = {end - start:.3f}")

find_nemo(nemo)
find_nemo(everyone)
find_nemo(large_arr)