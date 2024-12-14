

def main():
    print(calculate_price('**o*Z'))
    print(calculate_price('#@'))
    print(calculate_price('*#'))
    print(calculate_price('#@z'))
    pass

"""
Values:
    *: Snowflake - Value: 1
    o: Christmas Ball - Value: 5
    ^: Decorative Tree - Value: 10
    #: Shiny Garland - Value: 50
    @: Polar Star - Value: 100
"""

def calculate_price(ornaments: str) -> int:
    prices = {'*': 1,'o': 5,'^': 10,'#': 50,'@': 100}
    actual = -1
    prev = -1
    result = 0
    for ornament in reversed(ornaments):
        try:
            actual = prices[ornament]
        except KeyError:
            return 'undefined'
        result += actual if prev <= actual else -actual
        prev = actual
    return result


if __name__ == '__main__':
    main()