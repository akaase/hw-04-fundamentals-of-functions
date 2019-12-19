# Assignment: FUNdamentals of FUNctions

**Due:** XXX

In this homework, you will practice these concepts we've covered in class:

* Defining FUNctions
* Calling/Executing FUNctions
* Arguments
* Return values

## Deliverables

1. **Fork** the assignment repo
1. **Clone** your fork of the assignment repo
1. **Commit** any changes
1. **Push** to Github when you are done

## Submitting

To submit this assignment:

1. Go to the **assignment's main repo** (not your fork)
1. Click the **Issues** tab
1. Click the **New Issue** button
1. In the Title field, fill in your name
1. In the comment field, paste the URL to your assignment repo
1. Click **Submit new issue** and you're done!

---

# Exercise 1: Short Exercises

Create a file called `exercise1.py` and write your solution code in there.

Don't forget to commit your progress as you go along.

## Part 1

Write a FUNction called `double` that accepts an argument called `my_number` and **returns** that number multiplied by 2.

Try calling it multiple times and pass in different numbers each time.

## Part 2

Write a FUNction called `negative` that accepts a number as an argument and **returns** a boolean (true/false) indicating whether that number is negative or not.

Try calling it multiple times, passing in different numbers each time.

* What should the FUNction return if the number is exactly 0? (**Hint:** 0 is not a negative number)

## Part 3

Write a FUNction that accepts a string as an argument and **returns** `False` if the word is less than 8 characters long. (This time, you make up a name for the FUNction!)

* What should the FUNction return if the word is longer than 8 characters long?
* What should the FUNction return if the word is exactly 8 characters long?

---

# Exercise 2: Temperature Conversion

Create a file called `exercise2.py` and write your solution code in there.

Write a FUNction that converts Celsius temperatures to Fahrenheit. This will be useful the next time you travel to another country!

Start with prompting the user for a temperature in Celsius. Then call your FUNction and pass in the user input as an argument.

Your FUNction should:

* Have one argument: The temperature in Celsius
* Do the conversion with this formula: F = C x 9/5 + 32
* Ensure that the argument you pass in is a number by converting it with `int()`

For example, a temperature of 21 Celcius would be `21 x 9/5 + 32 = 69.8` (room temperature!)

Output the result in a full sentence using string interpolation.

Don't forget to commit your progress as you go along.

---

# Exercise 3: DRY Up Some Code

Create a file called `exercise3.py` and write your solution code in there.

Read the following Python code that violates the principle of *don't repeat yourself* (DRY).

```python
print('How far did person 1 run (in feet)?')
distance1 = float(input())
print(f'How many minutes did person 1 run take to run {distance1} feet?')
mins1 = float(input())

print('How far did person 2 run (in feet)?')
distance2 = float(input())
print(f'How many minutes did person 2 run take to run {distance2} feet?')
mins2 = float(input())

print('How far did person 3 run (in feet)?')
distance3 = float(input())
print(f'How many minutes did person 3 run take to run {distance3} feet?')
mins3 = float(input())

secs1 = mins1 * 60
speed1 = distance1/secs1

secs2 = mins2 * 60
speed2 = distance2/secs2

secs3 = mins3 * 60
speed3 = distance3/secs3

# Award Ceremonies
if speed3 > speed2 and speed3 > speed1:
    print(f'Person 3 was the fastest at {speed3} f/s')
elif speed2 > speed3 and speed2 > speed1:
    print(f'Person 2 was the fastest at {speed2} f/s')
elif speed1 > speed3 and speed1 > speed2:
    print(f'Person 1 was the fastest at {speed1} f/s')
elif speed1 == speed2 and speed2 == speed3:
    print(f'Everyone tied at {speed1} m/s')

print('Well done everyone!')
```

* Rewrite it to use FUNctions instead of repeating code
* Consider what your arguments and return values should be
* This one can be tricky, try working together with a classmate!
* Don't forget to commit your progress as you go along
* There can be multiple possible ways to solve this problem! But if you're stuck, some **hints** are provided below
* Try to open only one hint at a time!

#### For the purposes of this this assignment, do not use a list!

### (Spoiler Alert)

<details>
<summary>Hint 1</summary>
There is no need to re-write the "Awards Ceremonies" part of the code, because it's not repeated!
</details>

<details>
<summary>Hint 2</summary>
Start by writing a FUNction to ask for the distance that a person has run. e.g. `ask_for_distance`

What argument(s) does this FUNction need?

What should be the return value of this FUNction?
</details>

<details>
<summary>Hint 3</summary>
Try writing another FUNction to ask for the minutes that a person has run. e.g. `ask_for_minutes`

What argument(s) does this FUNction need? Just one or more than one?

What should be the return value of this FUNction?
</details>

<details>
<summary>Hint 4</summary>
Try writing another FUNction to compute the speed in terms of feet per second. e.g. `compute_speed`

What argument(s) does this FUNction need? Just one or more than one?

What should be the return value of this FUNction?
</details>

<details>
<summary>Hint 5</summary>
Try writing another FUNction that uses all of the previous 3 FUNctions that we wrote. e.g. `run`

This FUNction should ask for that particular runner's distance, ask for that particular runner's minutes, and then compute the speed.

What argument(s) does this FUNction need? Just one or more than one?

What should be the return value of this FUNction?
</details>

<details>
<summary>Hint 6</summary>
That's all I got for ya!!!!
</details>

---

# (STRETCH) Exercise 4: Challenge Yourself

_Exercise 4 is **optional** if you would like to challenge yourself. You are **not expected** to complete this part. Difficulty: Medium/Hard_

Create a file called `exercise4.py` and write your solution code in there.

## Part 1

Write a FUNction called `is_even` that accepts a number as an argument and returns a boolean (true/false) indicating whether that number is even or not even (that is, odd).

**Hint**: use the `%` operator.

Be sure to try calling it with different numbers.

## Part 2

Let's write a FUNction `wrap_text` that wraps text in symbols of our choice.

For example:

```python
wrap_text('hello', '===')
```

should return:

```
===hello===
```

Now that this FUNction works, how can we use it (**without modifying the FUNction**) to generate the following string?

```
---===###new message###===---
```

**Important**: Your function `wrap_text` needs to **return** a value rather than **print** one.

**Hints**:

* You'll have to call the same FUNction multiple times
* Try breaking down the problem into smaller pieces that you know `wrap_text` can solve!
* This is a hard one, to challenge those who are a bit more advanced. It's OK if you don't get how to solve it right now. You can come back and solve it another day!

---

# All Done!

I bet you've had enough of FUNctions by now, go have some real fun!

![](https://media.giphy.com/media/xT0BKiK5sOCVdBUhiM/source.gif)
