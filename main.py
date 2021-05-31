from tester import Test
from src.string_length import string_length

Test(
    string_length,
    format_out=lambda out: int(out),
    path_to_cases='src/string_length'
)
