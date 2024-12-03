# 🎄 Advent of Code 2024

This repository contains my solutions for the [Advent of Code 2024](https://adventofcode.com) challenge. I will be using
Python for all the solutions.

## 🚀 Usage

If you want to run any of the solutions, they can just be run as python scripts. For example, to run the solution for
day 1 part 2, you can run the following command:

```bash
cd aoc2024-solutions
python ./solutions/day01/part2.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENCE](LICENCE) file for details. You can do whatever you
want with this code.

## 🧩 Solutions

Now the fun part, the solutions! Below you can find a list of all the solutions I have written for the Advent of Code
2024 and maybe some thoughts on them.


### 🌟 Day 1

| Type            | Link                                                             |
|-----------------|------------------------------------------------------------------|
| Exercises       | [Advent of Code 2024 Day 1](https://adventofcode.com/2024/day/1) |
| Part 1 Solution | [Day 1 Part 1](solutions/day01/part1.py)                         |
| Part 2 Solution | [Day 1 Part 2](solutions/day01/part2.py)                         |

The first day of the Advent of Code 2024 was a nice warm-up. The first part was quite easy, but I think it offers some 
nice opportunities to write pythonic code. For example, I used the zip function to iterate over the two lists at the same
time. Also, this was one of the first times I used map. to convert the strings to integers.

In the second part, I needed to compute a 'similarity score'. I used the same read_input function as in the previous
part, which I just copied over. This is probably not the best way to do this, but I want the single solutions to be just
one file so that you can run and copy them easily. Again, I saw some opportunities to experiment with Python's features.
For example, I used the collections.Counter to count the number of values easily.

### 🔢 Day 2

| Type            | Link                                                             |
|-----------------|------------------------------------------------------------------|
| Exercises       | [Advent of Code 2024 Day 2](https://adventofcode.com/2024/day/2) |
| Part 1 Solution | [Day 1 Part 1](solutions/day02/part1.py)                         |
| Part 2 Solution | [Day 1 Part 2](solutions/day02/part2.py)                         |

The second day of the Advent of Code 2024 was a bit more challenging. I reused some ideas from the first day, like 
`map(int, ...)` to convert the strings to integers. In my opinion, I found a really nice way to check whether the values
strictly increasing or decreasing (`is_monotonic` function) where I just compared the sorted list with the original list.

In the second part, you were asked to check whether you could just remove one value to make the report valid. In my code
where I computed the different options, I had some issues because my solution was like not readable at all. With the
way I did it, I also ran into some issues as I forgot to copy the list before removing certain values. Following the old
code:

```python
levels_options = [levels.copy()]
for level in levels:
    new_option = levels.copy()
    new_option.remove(level)
    levels_options.append(new_option)
```

It works, but man, this looks ugly. With some help from a friend called claude.ai, I found the current way of doing it
quickly. Programming with an AI at your side is really helpful!

```python
levels_options = [levels.copy()]
levels_options.extend(
    [levels[:i] + levels[i + 1 :] for i in range(len(levels))]
)
```

What a beauty (-: This is why I love programming. You can always learn new things and improve your code.

### 🧮 Day 3

| Type            | Link                                                             |
|-----------------|------------------------------------------------------------------|
| Exercises       | [Advent of Code 2024 Day 3](https://adventofcode.com/2024/day/3) |
| Part 1 Solution | [Day 1 Part 1](solutions/day03/part1.py)                         |
| Part 2 Solution | [Day 1 Part 2](solutions/day03/part2.py)                         |

The third day of the Advent of Code 2024 was a nice challenge, as I decided to use regexes to parse the input. And I
challenged myself to not use AI. This journey remembered me again why I don't like regexes. They are powerful (I also
saw that), but man they are painful to write and hard to read. Also, in my first version of the code, I tried to fit
everything into one generator expression in a sum, which was just pain. I managed to do it and used the `operator.mul`
function on the way (which I never thought I'd use), but it was just not readable. So I decided to split it up into a
loop without using the `sum` function. This made the code much more readable and understandable. Following a comparison:

```python
# Old code
total_sum = sum(
    mul(*map(int, match.groups()))
    for match
    in MUL_REGEX.finditer(file.read())
)

# New code
total_sum = 0
for match in MUL_REGEX.finditer(text):
    a, b = map(int, match.groups())
    total_sum += a * b
```

The second part was a bit more challenging, but it made me appreciate the power of regexes. I extended the regex to also
match `do()` and `don't()`. Still, the regex is completely unreadable, but a comment should explain it.