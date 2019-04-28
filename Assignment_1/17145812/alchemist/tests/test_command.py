from pytest import raises

import yaml

from alchemist.command import check_ext, check_dict, check_keys

def test_yml_ext():
    with raises(TypeError) as exception:
        check_ext('alchemist.json')

def test_yml_format():
    with raises(TypeError) as exception:
        check_dict(yaml.load('wrongtype'))

def test_2_shelves():
    with raises(TypeError) as exception:
        check_keys(yaml.load("""
lower: [a, b]
upper: [c, d]
third: [e, f]
"""))
    with raises(TypeError) as exception:
        labdict = yaml.load('lower: [a, b]')
        check_keys(labdict)
