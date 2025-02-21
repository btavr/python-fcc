def arithmetic_arranger(problems, show_answers=False):
    arranged_problems = ''
    if len(problems) > 5:
        return "Error: Too many problems."

    # list of all operations in str format
    operations = list(map(lambda x: x.split()[1], problems))
    if not all(op in ['+', '-'] for op in operations):
        return "Error: Operator must be '+' or '-'."

    numbers = []  # list of all operands in str format
    for i in problems:
        p = i.split()
        numbers.extend([p[0], p[2]])

    if not all(map(lambda x: x.isdigit(), numbers)):
        return "Error: Numbers must only contain digits."

    if not all(map(lambda x: len(x) < 5, numbers)):
        return "Error: Numbers cannot be more than four digits."

    top_row = ''
    bottom_row = ''
    dashes = ''
    solutions = ''
    for idx, problem in enumerate(problems):
        num1, operator, num2 = problem.split()
        space_width = max(len(num1), len(num2)) + 2

        # Build rows
        top_row += num1.rjust(space_width)
        bottom_row += operator + num2.rjust(space_width - 1)
        dashes += '-' * space_width

        # Calculate solution if required
        if show_answers:
            solution = str(eval(problem))
            solutions += solution.rjust(space_width)

        # Add spaces between problems
        if idx < len(problems) - 1:
            top_row += ' ' * 4
            bottom_row += ' ' * 4
            dashes += ' ' * 4
            if show_answers:
                solutions += ' ' * 4

    # Combine rows into final output
    if show_answers:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes, solutions))
    else:
        arranged_problems = '\n'.join((top_row, bottom_row, dashes))

    return arranged_problems


# Example usage
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
