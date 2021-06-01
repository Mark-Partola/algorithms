from tester import Test, Describe
from src.string_length import string_length
from src.lucky_tickets.solutions import calc_lucky_tickets_count

Describe(
    'Length of String',
    Test(
        string_length,
        format_out=lambda it: int(it),
        path_to_cases='src/string_length'
    )
)

Describe(
    'Lucky Tickets',
    Test(
        calc_lucky_tickets_count,
        format_in=lambda it: int(it),
        format_out=lambda it: int(it),
        path_to_cases='src/lucky_tickets'
    )
)
