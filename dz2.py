arg = ["my", "name", "is", "Masha"]
result = ["Masha", "is", "name", "my"]

arg = ["a", "ab", "abc"]
result = 2.0

arg = ["her", "name", "is", "Masha", "Masha", "is", "a", "sister", "of", "Zhenya"]
result = {
    "her": 0,
    "name": 1,
    "is": [2, 5],
    "Masha": [3, 4],
    "a": 6,
    "sister": 7,
    "of": 8,
    "Zhenya": 9,
}

arg1 = ["my", "name", "is", "Masha"]
arg2 = ["my", "name", "is", "Zhenya"]
result = ["my", "name", "is"]

arg = ["aaa", "aaa", "bbb", "ccc", "bbb"]
result = {
    "aaa": 2,
    "bbb": 2,
    "ccc": 1,
}

arg = ["abcd", "a", "ab", "abc", "bazinga", "bar"]
result = ["a", "ab", "abc", "bar", "abcd", "bazinga"]
