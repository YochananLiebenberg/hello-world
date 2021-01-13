def test(x):
    num = 0
    for i in x:
        i += num
    return num

def test_1():
    assert test([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_1()
    print("Everything passed")
