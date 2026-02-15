from prac_py_rapid_fuzz import main
import time


def test_perf():
    n_times = 100_000
    
    start_time = time.perf_counter()
    for _ in range(n_times):
        main("monster group", "monster_inc")


    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")
