from caesar_cipher import __version__
from  caesar_cipher.caesar_cipher import *

def test_version():
    assert __version__ == '0.1.0'


def test_encrypt():
    actual = encrypt('12@ live word',27)
    expect = '12@ MJWF XPSE'
    assert actual == expect
    assert decrypt(expect,27) == '12@ live word'.upper()


def test_hacker():
    actual = hacker(encrypt('It was the best of times, it was the worst of times.',5))
    expect = 'It was the best of times, it was the worst of times.'.upper()
    assert actual==expect