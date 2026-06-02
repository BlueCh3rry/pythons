import functools
import operator
from collections.abc import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation == 'add':
        return functools.reduce(lambda x, y: operator.add(x, y), spells)
    if operation == 'multiply':
        return functools.reduce(operator.mul, spells)
    if operation == 'max':
        return functools.reduce(max, spells)
    if operation == 'min':
        return functools.reduce(min, spells)
    raise ValueError(f'Invalid operation : ({operation})')


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'Fire_enc': functools.partial(
            base_enchantment, power=50, element='fire'),

        'Ice_enc': functools.partial(
            base_enchantment, power=50, element='ice'),

        'Lightning_enc': functools.partial(
            base_enchantment, power=50, element='lightning'),
    }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @functools.singledispatch
    def default(arg) -> str:
        return "Unknown spell type"

    @default.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @default.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @default.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"
    return default


def main() -> None:
    spells = [40, 10, 6]
    print('\nTesting Spell Reducer...')
    print("Sum:", spell_reducer(spells, 'add'))
    print("Product:", spell_reducer(spells, 'multiply'))
    print("Max:", spell_reducer(spells, 'max'))
    # print("Min:", spell_reducer(spells, 'min'))
    print()

    # print('Testing Partial Enchantment...')
    # def base_enchantment(power, element, target) -> str:
    #     return f"Attack {target} with {element} ({power} DMG)"

    # enchants = partial_enchanter(base_enchantment)
    # print(enchants['Fire_enc'](target='Wyvern'))
    # print(enchants['Ice_enc'](target='Dragon'))
    # print()

    print('Testing memoized fibonacci...')
    print(f"Fibo({0}) :", memoized_fibonacci(0))
    print(f"Fibo({1}) :", memoized_fibonacci(1))
    print(f"Fibo({10}) :", memoized_fibonacci(10))
    print(f"Fibo({15}) :", memoized_fibonacci(15))
    print()
    print(memoized_fibonacci.cache_info())
    print()

    print('Testing spell dispatcher...')
    disp = spell_dispatcher()
    print(disp(42))
    print(disp("fireball"))
    print(disp(["fire", "water", "wind"]))
    print(disp(None))
    print()


if __name__ == '__main__':
    main()
