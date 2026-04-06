# The Nature of Code: Porting ~~from p5.js to Processing~~ from Processing to Mewnala

This repository is a collaborative effort to port the code examples from [Daniel Shiffman's book *The Nature of Code*](https://natureofcode.com/) ~~from the **Processing** programming language to python **Mewnala**.

Note: Our python library `mewnala` is very early and has missing functionality, so be prepared for things not working and to have to ask us lots of questions in the [#libprocessing discord](https://discord.com/channels/1076634729618624534/1473643112512491692).

We are going to work together to make all these examples work!

## Getting Started

You will want to set up your environment by following the instructions on the [libprocessing repo](https://github.com/processing/libprocessing).
But just incase, here you go:

```bash
# have python3 installed on your system

# create a sketch folder and go inside
mkdir my-sketch-folder && cd my-sketch-folder

# create a virtual env
python -m venv .venv

# activate virtual env
source .venv/bin/activate

pip install mewnala

python my_ported_sketch.py
```

## Repository Structure

The code examples are organized by chapters, starting from Chapter 0. Within each chapter, examples are numbered sequentially (e.g., `Example_0_1`, `Example_0_2`).  

```
/chapter0/
  Example_0_1/
  Example_0_2/
  ...
/chapter1/
  Example_1_1/
  Example_1_2/
  ...
```

Each example is contained in its respective folder to make navigation straightforward.
The names of the main sketche files should be the same as the folder they are in

## Contribution Guidelines

We welcome contributions from the community! If you'd like to help port examples to Processing, please follow these guidelines:

1. Ensure the ported code adheres to Processing's syntax yet stays in the same style conventions.
2. Keep the functionality and code structure as close to the original (p5.js -> Processing) example as possible.
3. Test your code to ensure it runs properly using `Mewnala`.
4. Make sure to change window size from (640,240) -> (640,360) and make sure everything is still centered and looks correct in the new window size
5. Replace the the Processing function `println()` to the python `print()` function 

all the code examples are available in the [*The Nature of Code* Website](https://natureofcode.com/).

Feel free to open a pull request or raise an issue if you have questions or suggestions!
