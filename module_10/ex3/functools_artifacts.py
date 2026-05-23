#!/usr/bin/python3

import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    # Function lambda in reduce:
    # First element is accumulator, second is the current item in the list
    # Accumulator keeps its value, item iterate through the list
    # last arg is the list to iterate
    if operation == 'add':
        return functools.reduce(
            lambda accumulator, item: operator.add(accumulator, item), spells
        )
    if operation == 'multiply':
        return functools.reduce(
            lambda accumulator, item: operator.mul(accumulator, item), spells
        )
    if operation == 'max':
        return functools.reduce(
            lambda accumulator, item: item if item > accumulator
            else accumulator, spells
        )
    if operation == 'min':
        return functools.reduce(
            lambda accumulator, item: item if item < accumulator
            else accumulator, spells
        )
    raise ValueError(f'Invalid operation : ({operation})')


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': functools.partial(
            base_enchantment, power=50, element='fire'),

        'ice_enchant': functools.partial(
            base_enchantment, power=50, element='ice'),

        'lightning_enchant': functools.partial(
            base_enchantment, power=50, element='lightning'),
    }


@functools.lru_cache  # Memoization decorator for recursive opti
def memoizied_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoizied_fibonacci(n - 1) + memoizied_fibonacci(n - 2)


def spell_dispatcher() -> callable:

    @functools.singledispatch
    def default(arg) -> str:
        return f"Unknown type ({type(arg).__name__})"

    @default.register(int)
    def _(arg: int) -> str:
        return f"Dealing {arg} damages"

    @default.register(str)
    def _(arg: str) -> str:
        return f"Enchant: {arg}"

    @default.register(list)
    def _(arg: list) -> str:
        return f"Casting every spells : {str.join(' | ', arg)}"

    return default


def main() -> None:
    spells = [40, 6]
    print('=== Testing Spell Reducer ===')
    print("Sum:", spell_reducer(spells, 'add'))
    print("Product:", spell_reducer(spells, 'multiply'))
    print("Max:", spell_reducer(spells, 'max'))
    print("Min:", spell_reducer(spells, 'min'))
    print('')

    print('=== Testing Base Enchantment ===')

    def base_enchantment(power, element, target) -> str:
        return f"Attack {target} with {element} (power of {power})"

    enchants = partial_enchanter(base_enchantment)
    print(enchants['fire_enchant'](target='killer bunny'))
    print(enchants['ice_enchant'](target='Laurent'))
    print('')

    print('=== Testing memoized fibonacci ===')
    n1 = 38
    n2 = 37
    print(f"Fibonacci of {n1} ->", memoizied_fibonacci(n1))
    print(f"Fibonacci of {n2} ->", memoizied_fibonacci(n2))
    print('Try restarting the program without the '
          '@functools.lru_cache decorator :)')
    print('')

    print('=== Testing memoized fibonacci ===')
    disp = spell_dispatcher()
    print("List of spells ->\t\t", disp(['42 spell', 'Paco curse',
                                         'Napoleon\'s rage']))
    print("One string enchantment ->\t", disp("Curse of Evil Laurent"))
    print("One damage int ->\t\t", disp(50))
    return None


if __name__ == '__main__':
    main()
