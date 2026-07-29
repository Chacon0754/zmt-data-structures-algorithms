from time import perf_counter

everyone = ["nemo"] * 1000000
def find_nemo(arr: list[str]):
    start = perf_counter()
    
    for i in range(len(arr)):
        if arr[i] == "nemo" :
            print(f"Found {i+1}.- {arr[i]}")
    
    end = perf_counter()

    print(f"Time {end - start:.4f}")

find_nemo(everyone)