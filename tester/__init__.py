import os


class Colors:
    GREEN = '\033[92m'
    FAIL = '\033[91m'
    END_COLOR = '\033[0m'


class Test:
    def __init__(self, fn, path_to_cases, format_in=lambda x: x, format_out=lambda x: x):
        self.fn = fn
        self.path_to_cases = path_to_cases
        self.format_in = format_in
        self.format_out = format_out

    def run(self):
        dirname = os.getcwd()

        path = f'{self.path_to_cases}/test.'

        test_number = 0
        succeed_number = 0
        failed_number = 0

        while True:
            in_file_name = os.path.join(dirname, f'{path}{test_number}.in')
            out_file_name = os.path.join(dirname, f'{path}{test_number}.out')
            is_in_file_exists = os.path.exists(in_file_name)
            is_out_file_exists = os.path.exists(out_file_name)

            if not is_in_file_exists or not is_out_file_exists:
                break

            with open(in_file_name) as in_file:
                with open(out_file_name) as out_file:
                    in_line = self.format_in(in_file.readline().rstrip('\n'))
                    out_line = self.format_out(out_file.readline())

                    result = self.fn(in_line)

                    if result == out_line:
                        succeed_number += 1
                        print(Colors.GREEN + 'Success' + Colors.END_COLOR)
                    else:
                        failed_number += 1
                        print(
                            Colors.FAIL + 'Failure:',
                            f'Expected {result} to be {out_line}' +
                            Colors.END_COLOR
                        )

            test_number += 1

        print(f'Succeeded: {succeed_number}. Failed: {failed_number}')


class Describe:
    def __init__(self, description, test):
        print('\n' + "\u0332".join(description))
        test.run()
