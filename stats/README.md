# stats

My first python program! Takes some integers as input and does some basic calculations, such as sum, mean and median.

## `random_ints.py`

Create some random integers:

```bash
$ python3 random_ints.py > integers.txt
```

## `stats.py`

Perform calculations on some integers.

Either enter input manually:

```bash
$ python3 stats.py
Do some math on some integers! Use ^D empty entry to end input.
Enter an integer: 3
Enter an integer: 4
Enter an integer: 5
Enter an integer: 3
Enter an integer:
Results:
	Count: 4
	Sum: 15
	Mean: 3.75
	Median: 3.5
	Mode: 3
```

Or provide a file with input generated from `random_ints.py`:

```bash
$ python3 stats.py < integers.txt
```

## Things I Learned

* Basic input (`input()`) and output (`print()`)
* `for in`, `if else`, and `while`
* Function `def`inition
* Error handling with `try` and `except`
* Lists and dictionaries
* String formatting

## Questions

* How does variable scope work?
