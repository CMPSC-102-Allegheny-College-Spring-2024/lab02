# Quadratic Roots

## Assigned: Monday, 29 Jan 2024

## Due: Monday, 5 Feb, 2024, 1:30pm

## Project Goals

This lab assignment invites you to combine what you learned about the basics of Python programming and mathematical functions to implement a useful program that can use an equation to find the roots for a quadratic equation. The program will have a command-line interface that accepts as input the values `a`, `b`, and `c` for a quadratic equation of the form $f(x) = a \times x^2 + b \times x + c$. As you learn more about to translate mathematical equations into Python functions, you will implement and test a complete Python program while using tools such as the VS Code text editor, a terminal window, and the Poetry package manager.

## Project Access

You can access this assignment by clicking the link provided to you in Discord or in a course schedule. Once you click this link it will create a GitHub repository that you can clone to your computer by using the `git clone` command to download the project from GitHub to your computer. Now you are ready to add source code and documentation to the project!

## Expected Output

This assignment invites you to implement a quadratic root finding program called `rootfinder`. To learn more about the equations for finding the roots of a quadratic equation, please try out the [quadratic formula calculator](https://www.calculatorsoup.com/calculators/algebra/quadratic-formula-calculator.php). For instance, input `a=1`, `b=2`, and `c=1` into this calculator and see what answer it produces. 

After repairing your program, as explained in the next step of this assignment, it will also be possible for you to run the provided Python program by first typing `poetry install` in the `rootfinder/` directory. Once all necessary dependancies have been loaded, you will be ready to run the next command, `poetry run rootfinder --a 1 --b 2 --c 1` in your terminal window to observe the following output:

```
⭐ Calculating the roots of a quadratic equation with:
   a = 1.0
   b = 2.0
   c = 1.0

⭐ Finished computing the roots of the equation as:
   x_one = -1.0
   x_two = -1.0
```

Does the Python program produce the same output as the quadratic formula calculator site suggests it should? If it does, then try to run the program with different inputs by typing `poetry run rootfinder --a 1 --b 1 --c 1`. In this case, your program should produce the following output:

```
⭐ Calculating the roots of a quadratic equation with:
   a = 1.0
   b = 1.0
   c = 1.0

⭐ Finished computing the roots of the equation as:
   x_one = (-0.49999999999999994+0.8660254037844386j)
   x_two = (-0.5-0.8660254037844386j)
```

Is this output the same as what the web-based quadratic formula calculator produces? Please note that the output of this program includes numbers like `-0.5-0.8660254037844386j`, which means that this is a program that has an "imaginary" component. If you would like to learn more about "imaginary" numbers and how you can intuitively and geometrically interpret them, please read the [visual and intuitive guide to imaginary numbers](https://betterexplained.com/articles/a-visual-intuitive-guide-to-imaginary-numbers/), bearing in mind that the referenced article uses the variable `i` and Python programs always use the variable `j` to mean the same thing. Finally, please make sure that you try your program with several additional inputs, always confirming that it works correctly by using the web-based quadratic formula calculator.


Special note:
Remember, if you want to run `rootfinder` you must use your terminal to go into the GitHub repository containing this project and then go into the `rootfinder` directory that contains the project's source code. Finally, remember that before running the program you must run `poetry install` to add the dependencies. If you run into errors when using a `poetry run` command you can often resolve them by deleting the `.venv` directory and the `poetry.lock` file and then trying `poetry install` again.

Use a `gatorgrade --config config/gatorgrade.yml` command to run GatorGrader to check your work. You may also use the output from running GatorGrader in GitHub Actions.

## Adding Functionality

If you study the file `rootfinder/rootfinder/main.py` you will see that it has many `TODO` markers that designate the parts of the program that you need to implement before `rootfinder` will produce correct output. If you run the provided test suite with the command `poetry run task test` you will see that it produces output like the following:

```
================================= FAILURES =================================
__________________ test_calculate_x_values_non_imaginary ___________________

    def test_calculate_x_values_non_imaginary():
        """Check that the calculation of x values works if they are not imaginary."""
        a = 1
        b = 2
        c = 1
>       x_one, x_two = rootfind.calculate_quadratic_equation_roots(a, b, c)
E       TypeError: cannot unpack non-iterable NoneType object

tests/test_rootfind.py:20: TypeError
```

Alternatively, running the program with a command like `poetry run rootfinder --a 1 --b 2 --c 1` will not produce any output! This is due to the fact that the required source code does not yet exist inside of the `rootfinder` program. One function that you need to implement is specified by the following signature.

```python linenums="1"
def calculate_quadratic_equation_roots(
    a: float, b: float, c: float
) -> Tuple[Union[float, complex], Union[float, complex]]:
```

This function's type annotations on line `2` suggest that each of its three inputs are variables of type `float`. On line `3`, the notation `Union[float, complex]` means that one of the outputs of `calculate_quadratic_equation_roots` can either be a floating-point value of type `float` or an imaginary number of type `complex`. The complete annotation of `Tuple[Union[float, complex], Union[float, complex]]` means that the return value of `calculate_quadratic_equation_roots` will be a two-tuple of values, with each component of the two-tuple being either a `float` or a `complex` number. This function should return values for `x_one` and `x_two` according to the following equations:

$$
x_1=\frac{-b+\sqrt{b^2-4ac}}{2a}
$$

$$
x_2=\frac{-b-\sqrt{b^2-4ac}}{2a}
$$

To provide a command-line interface to your program, you should also implement a main function that has the following signature:

```python linenums="1"
def main(
    a: float = typer.Option(1),
    b: float = typer.Option(2),
    c: float = typer.Option(2)
):
```

This function signature shows that `rootfinder` accepts as input three parameters called `a`, `b`, and `c` that respectively have default values of `1`, `2`, and `2`, as seen on lines `2` through `4`. If you run `poetry run rootfinder` if should produce this output:

``` bash
⭐ Calculating the roots of a quadratic equation with:
   a = 1.0
   b = 2.0
   c = 2.0

⭐ Finished computing the roots of the equation as:
   x_one = (-0.9999999999999999+1j)
   x_two = (-1-1j)
```

## Running Checks

As you continue to add and confirm the correctness of `rootfinder`'s functionality, you also study the source code in the `pyproject.toml` file. This file contains the specification of several tasks that will help you to easily run checks on your Python source code. Now, you can run commands like `poetry run task lint` to automatically run all of the linters designed to check the Python source code in your program and its test suite. You can also use the command `poetry run task black` to confirm that your source code adheres to the industry-standard format defined by the `black` tool. If it does not adhere to the standard then you can run the command `poetry run black rootfinder tests` and it will automatically reformat the source code.

```toml
[tool.taskipy.tasks]
black = { cmd = "black rootfinder tests --check", help = "Run the black checks for source code format" }
flake8 = { cmd = "flake8 rootfinder tests", help = "Run the flake8 checks for source code documentation" }
mypy = { cmd = "poetry run mypy rootfinder", help = "Run the mypy type checker for potential type errors" }
pydocstyle = { cmd = "pydocstyle rootfinder tests", help = "Run the pydocstyle checks for source code documentation" }
pylint = { cmd = "pylint rootfinder tests", help = "Run the pylint checks for source code documentation" }
test = { cmd = "pytest -x -s", help = "Run the pytest test suite" }
test-silent = { cmd = "pytest -x --show-capture=no", help = "Run the pytest test suite without showing output" }
all = "task black && task flake8 && task pydocstyle && task pylint && task mypy && task test"
lint = "task black && task flake8 && task pydocstyle && task pylint"
```

Along with running tasks like `poetry run task lint`, you can run `gatorgrade --config config/gatorgrade.yml` to check your work. If `gatorgrade` tool shows that all checks pass, you will know that you made progress towards correctly implementing and writing about `rootfinder`. If your program has all of the anticipated functionality, you can run the command `poetry run task test` and see that the test suite produces output like the following. Notice that the current test suite only has three test cases! If you are looking for an additional challenge, consider using the [quadratic formula calculator](https://www.calculatorsoup.com/calculators/algebra/quadratic-formula-calculator.php) to guide you as you create new test cases for `calculate_quadratic_equation_roots` that run in [Pytest](https://docs.pytest.org/).

``` bash
collected 3 items

tests/test_rootfind.py ...
```

## Project Reflection

Once you have finished both of the previous technical tasks, you can use a text editor to answer all of the questions in the `writing/reflection.md` file. For instance, you should provide the output of the Python program in a fenced code block, explain the meaning of the Python source code segments that you implemented and used, and answer all of the other questions about your experiences in completing this project. For instance, your technical writing in the `writing/reflection.md` file should make it clear that you understand the concept of an "imaginary" number and the notation that the Python programming language uses to express these numbers.

## Submission

As you are working on your lab, you are to commit and push regularly. The commands are the following.

 ``` bash
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Project Assessment

The grade that a student receives on this assignment will have the following components.

- **GitHub Actions CI Build Status [up to 50%]:**: For the lab02 repository associated with this assignment students will receive a checkmark grade if their last before-the-deadline build passes. This is checking some baseline writing and commit requirements as well as correct running of the program. An additional reduction will given if the commit log shows a cluster of commits at the end clearly used just to pass this requirement. An addition reduction will also be given if there is no commit during lab work times. All other requirements are evaluated manually.

- **Mastery of Technical Writing [up to 25%]:**: Students will also receive a checkmark grade when the responses to the writing questions presented in the `reflection.md` reveal a proficiency of both writing skills and technical knowledge. To receive a checkmark grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

- **Mastery of Technical Knowledge and Skills [up to 25%]**: Students will receive a portion of their assignment grade when their program implementation reveals that they have mastered all of the technical knowledge and skills developed during the completion of this assignment. As a part of this grade, the instructor will assess aspects of the programming including, but not limited to, the completeness and the correctness of the program and the use of effective source code comments.

---

## GatorGrade

### Checks for GatorGrade

For immediate feedback on submissions, we will be using Gator Grade to inform the of missing components in the submission. As you submit, you will notice that there is a thick red X that will change to a green check mark when all components have been included in the submission. You are encouraged to click on the red X to find a listing of the components to address.

You can check the baseline writing and commit requirements for this lab assignment by running department's assignment checking `gatorgrade` tool. To use `gatorgrade`, you first need to make sure you have Python3 installed (type `python --version` to check). If you do not have Python installed, please see:

- [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
- [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
- [How to Install Python 3 and Set Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

Then, if you have not done so already, you need to install `gatorgrade`:

- First, [install `pipx`](https://pypa.github.io/pipx/installation/)
- Then, install `gatorgrade` with `pipx install gatorgrade`

Finally, you can run `gatorgrade`: `gatorgrade --config config/gatorgrade.yml`

## Seeking Assistance

* Extra resources for using markdown include;
  + [Markdown Tidbits](https://www.youtube.com/watch?v=cdJEUAy5IyA)
  + [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* Do not forget to use the above git commands to push your work to the cloud for the instructor to grade your assignment. You can go to your GitHub repository using your browser to verify that your files have been submitted. Please see the TL’s or the instructor if you have any questions about assignment submission.

Students who have questions about this project outside of the lab time are invited to ask them in the course's Discord channel or during instructor's or TL's office hours.
