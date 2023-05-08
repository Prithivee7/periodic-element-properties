from periodic_element_properties import __version__
from periodic_element_properties.elements import Functions


def test_version():
    assert __version__ == "0.2.0"


def test_atomic_number_function():
    f = Functions()
    assert f.get_element_details_based_on_atomic_number(2)[
        'Element'] == "Helium"
