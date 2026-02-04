# Simple Calculator

Honestly just needed a quick calculator for when I'm too lazy to open the system calculator app. Yeah I know that sounds dumb but whatever, it was fun to make.

## What it does

Basic math operations. You give it two numbers and then you can keep doing different operations on those same numbers until you quit. Addition, subtraction, multiplication, division - the usual stuff.

## How to use

```bash
python calculator.py
```

It'll ask for two numbers first. Then you keep entering which operation you want:
- `+` for addition
- `-` for subtraction  
- `*` for multiplication
- `/` for division
- `q` to quit

## Example run

```
Enter first num: 10
Enter second num: 5
Enter the sign(+,-,*,/ or q to quit): +
your sum is:  15
Enter the sign(+,-,*,/ or q to quit): *
your product is:  50
Enter the sign(+,-,*,/ or q to quit): /
your result is:  2.0
Enter the sign(+,-,*,/ or q to quit): q
closed
```

## How it works

Nothing complicated:
- Takes two numbers at the start
- Loops forever asking what operation you want
- Does the math based on your choice
- Shows the result
- Keeps going until you type 'q'

The loop thing is kinda nice because you can try different operations without restarting the program each time.

## Issues I know about

Yeah there's definitely some problems lol:
- If you divide by zero it crashes (should probably catch that)
- No way to change the numbers once you enter them, you have to restart
- Input validation is basically nonexistent - type letters and it'll explode
- The "from random import choice" at the top is actually useless, I was testing something and forgot to remove it oops

## Why I kept it simple

Could've added a ton of features like:
- More operations (exponents, square root, modulo, etc)
- Ability to chain calculations (use the result as next input)
- History of all calculations
- Better error messages
- Decimal/float input validation
- Scientific calculator stuff

But honestly this does what I needed for basic quick math. Sometimes simple is enough you know?

## Improvements if I ever update this

Things on my mental todo list:
- Fix the divide by zero crash
- Remove that random import that does nothing
- Add option to enter new numbers without restarting
- Maybe make it so you can do more than 2 numbers at once
- Better input handling so it doesn't break when you type garbage
- Prettier output formatting

But yeah we'll see if I actually get around to any of that. Works fine for now.

## Learning purposes

If you're learning Python this is a decent beginner project. Shows you:
- Basic input/output
- Type conversion (string to int)
- If-elif-else chains
- While loops
- How to break out of loops

Not super complicated but covers the fundamentals.

---

That's pretty much it. Use it if you want, change whatever you feel like changing. No strings attached.
