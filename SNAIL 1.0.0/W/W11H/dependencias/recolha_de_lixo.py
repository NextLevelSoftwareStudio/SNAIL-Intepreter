import memória
counter = 7
def código():
    try:
        for i in range(1, counter + 1):
            memória.mem.apagar(i)
    except MemoryError as e:
        print(f"Error 5: Memory error. ({e})")
    except Exception as e:

        print(f"Something has gone wrong. ({e})")
