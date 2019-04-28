from pytest import raises
from simplemaths.simplemaths import SimpleMaths as sm

class TestSimpleMaths():

    def test_constructor_input(self):
        """ Check that some non-integer inputs will fail """
        with raises(TypeError) as exception:
            sm(1.0)
        with raises(TypeError) as exception:
            sm("string")

    def test_constructor_input_empty(self):
        """ Check that an empty input will fail """
        with raises(TypeError) as exception:
            sm()

    def test_constructor_number(self):
        """ Check that the .number attribute returns the inputted integer """
        twelve = sm(12)
        assert twelve.number == 12

    def test_constructor_type(self):
        """ Check that the constructor creates an 'sm'-type object """
        twelve = sm(12)
        assert type(twelve) == sm

    def test_square(self):
        twelve = sm(12)
        assert sm.square(twelve) == 12**2

    def test_factorial_0(self):
        zero = sm(0)
        assert zero._factorial(0) == 1

    def test_factorial_proper(self):
        twelve = sm(12)
        assert sm.factorial(twelve) == 479001600
        zero = sm(0)
        assert sm.factorial(zero) == 1

    def test_power(self):
        """ Check result for int inputs to power """
        twelve = sm(12)
        assert twelve.power(0) == 1
        minustwo = sm(-2)
        assert minustwo.power(2) == 4

    def test_power_default(self):
        """ Check that the power defaults to 3 """
        twelve = sm(12)
        assert twelve.power() == 12**3

    def test_power_inputs(self):
        """ Check result for float input to power """
        twelve = sm(12)
        assert twelve.power(3.0) == 12**3.0

    def test_power_inputs(self):
        """ Check that a non-int/float input will fail """
        twelve = sm(12)
        with raises(TypeError) as exception:
            twelve.power('three')

    def test_odd_or_even(self):
        """ Check that 0 returns as Even and other positive cases """
        zero = sm(0)
        assert zero.odd_or_even() == 'Even'
        one = sm(1)
        assert one.odd_or_even() == 'Odd'
        two = sm(2)
        assert two.odd_or_even() == 'Even'
        minusone = sm(-1)
        assert minusone.odd_or_even() == 'Odd'

    def test_square_root(self):
        """ Positive tests for 0, int result, float result and complex result """
        zero = sm(0)
        assert zero.square_root() == 0.0
        four = sm(4)
        assert four.square_root() == 2
        twelve = sm(12)
        assert twelve.square_root() == 3.4641016151377544
        minusfour = sm(-4)
        assert minusfour.square_root() == (1.2246467991473532e-16+2j)
        assert type(minusfour.square_root()) == complex
