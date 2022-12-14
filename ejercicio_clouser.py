from __future__ import division


def make_division_by(n):
    def division(x):
        assert type(x) == int, "Debe ingresar solo numeros enteros"
        return int(x / n)
    return division


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18)) # el output es 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100)) # el output es 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54)) #el output es 3


if __name__ == "__main__":
    run() 