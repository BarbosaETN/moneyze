from utils.formatters import format_currency


def main():

    values = [
        0,
        50,
        1500,
        1234567.89,
        -300.5,
    ]

    for value in values:

        print(
            format_currency(value)
        )


if __name__ == "__main__":
    main()