import pytest
from profiles import *

@pytest.fixture(scope="module")
def profiles():
    profiles = {
        'getter': ProfileGetter(),
        'cleaner': Cleaner('    All User Profile     : ')
    }
    yield profiles


def test_get_raw_profiles_txt(profiles):
    assert isinstance(profiles['getter']._get_raw_profiles_txt(), str)


def test_clean_profile(profiles):
    assert 'orenmerav' == profiles['cleaner']._clean('    All User Profile     : orenmerav\r')


def test_extract_profiles(profiles):
    assert 'orenmerav' in profiles['getter'].extract_profiles()


@pytest.fixture(scope="module")
def password_getter():
    profiles = ProfileGetter()
    yield PasswordGetter(profiles.extract_profiles())

def test_raw_text(password_getter):
    assert isinstance(password_getter._raw_text('orenmerav'), str)

def test_get_key(password_getter):
    assert '0546660009' == password_getter._get_key("Mainfeld")





