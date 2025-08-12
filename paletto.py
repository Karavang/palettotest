from functools import lru_cache
import subprocess


def read_lz4_file(filename):

    result = subprocess.run(
        ["lz4", "-d", "-c", filename], check=True, capture_output=True
    )
    return result.stdout.decode()


@lru_cache
def task1(search: tuple, data: str):

    lines = data.split("\n")
    keys = lines[0].split(",")
    values = [line.split(",") for line in lines[1:]]
    searchKeys = [k for k, v in search]
    searchVals = [v for k, v in search]
    print(searchVals)
    if all(k in keys for k in searchKeys):
        indexes = [keys.index(k) for k in searchKeys]
        if all(
            any(row[idx] == val for row in values)
            for idx, val in zip(indexes, searchVals)
        ):
            return 1
        else:
            return -1
    else:
        raise ValueError("Key mismatch")


if __name__ == "__main__":

    data1 = "side,currency,value\nIN,PLN,1\nIN,EUR,2\nOUT,ANY,3"
    search1 = {"side": "IN", "currency": "PLN"}
    searchT1 = tuple(search1.items())
    print(task1(searchT1, data1))
