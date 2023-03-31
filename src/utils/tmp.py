if __name__ == "__main__":
    ner = [[1, 2], [3, 4], [5, 6]]
    print(ner)

    for i, n in enumerate(ner):
        print(i, n)
        n[0] = 66

    print(ner)
