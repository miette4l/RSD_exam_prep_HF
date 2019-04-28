from pytest import raises

from alchemist.laboratory import update_shelves, can_react, Laboratory

TEST_LAB = Laboratory(['a', 'b', 'c'], ['antia', 'antic', 'd'])

def test_init():
    assert isinstance(TEST_LAB, Laboratory)
    assert TEST_LAB.lower_shelf == ['a', 'b', 'c']
    assert TEST_LAB.upper_shelf == ['antia', 'antic', 'd']

def test_init_shelf_type():
    with raises(TypeError) as exception:
        Laboratory(['a'], 'b')
        Laboratory(('a'), ['b'])

def test_init_no_empty_strings():
    with raises(ValueError) as exception:
        Laboratory(['a'], [''])
        Laboratory(['anti'], ['a'])

def test_init_antianti():
    with raises(ValueError) as exception:
        Laboratory(['antiantia'], ['a'])
        Laboratory(['a'], ['antiantia'])

def test_update_shelves():
    assert update_shelves(['a', 'b'], ['antia', 'c'], 'a', 0) == (['b'], ['c'])
    assert update_shelves(
        ['a', 'b', 'd'], ['antia', 'c', 'antia'], 'a', 2) == (['b', 'd'], ['antia', 'c'])

def test_update_shelves_shelf_type():
    with raises(TypeError) as exception:
        update_shelves(('a', 'b'), ['antia', 'antic', 'd'], 'a', 0)

def test_can_react():
    assert can_react('a', 'antia')
    assert can_react('antia', 'a')
    assert can_react('a', 'b') is False

def test_can_react_no_empty_strings():
    with raises(ValueError) as exception:
        can_react('anti', '')

def test_can_react_antianti():
    with raises(ValueError) as exception:
        can_react('antiantia', 'antia')

def test_do_a_reaction():
    assert TEST_LAB.do_a_reaction() == (['b', 'c'], ['antic', 'd'])

def test_random_selections():
    lower = ['antia']
    upper = ['a', 'b', 'a', 'c', 'a', 'c', 'a', 'd', 'a', 'b', 'a', 'c', 'a']
    testlab2 = Laboratory(lower, upper)
    answer = testlab2.do_a_reaction()
    assert answer[1].count('a') == 6
    for substance in answer[1]:
        if substance == 'a':
            answer[1].remove('a')
    assert answer[1] == ['b', 'c', 'c', 'd', 'b', 'c']

def test_do_a_reaction_shelf_type():
    with raises(TypeError) as exception:
        Laboratory.do_a_reaction(Laboratory, ('a', 'b'), ['antia', 'antic', 'd'])

def test_all_reactions():
    assert TEST_LAB.all_reactions() == (2, [['b'], ['d']])
