#!/usr/bin/env python

"""
================================================
AB Electronics UK IO Zero 32 Tests | set_port_polarity

Requires python smbus to be installed
For Python 2 install with: sudo apt-get install python-smbus
For Python 3 install with: sudo apt-get install python3-smbus

run with: python3 set_port_polarity.py
================================================

This test validates the set_port_polarity function in the IOZero32 class.

Hardware Required: Logic Analyser on I2C Pins

=== Expected Result ============================

> Console Output:

port low boundary check: PASSED
port high boundary check: PASSED
value low boundary check: PASSED
value high boundary check: PASSED
Logic output Started
Logic output Ended

> Logic Analyser Output:

W 0x20 0x04 0x00
W 0x20 0x05 0x00

looping to

W 0x20 0x04 0xFF
W 0x20 0x05 0xFF


"""
from __future__ import absolute_import, division, print_function, \
                                                    unicode_literals

try:
    import sys
    sys.path.append("..")
    from IOZero32 import IOZero32
except ImportError:
    raise ImportError("Failed to import IOZero32 library")


def main():
    """
    Main program function
    """

    passed = True

    iobus = IOZero32(0x20)  # new iobus object

    # Check set_port_polarity port for low out of bounds
    try:
        iobus.set_port_polarity(-1, 0)
        pass
    except ValueError:
        print("port low boundary check: PASSED")
        pass
    except IOError:
        passed = False
        print("I2C IOError")
    else:
        passed = False
        print("port low boundary check: FAILED")
        pass

    # Check set_port_polarity port for high out of bounds
    try:
        iobus.set_port_polarity(2, 0)
        pass
    except ValueError:
        print("port high boundary check: PASSED")
        pass
    except IOError:
        passed = False
        print("I2C IOError")
    else:
        passed = False
        print("port high boundary check: FAILED")
        pass

    # Check set_port_polarity value for low out of bounds
    try:
        iobus.set_port_polarity(0, -1)
        pass
    except ValueError:
        print("value low boundary check: PASSED")
        pass
    except IOError:
        passed = False
        print("I2C IOError")
    else:
        passed = False
        print("value low boundary check: FAILED")
        pass

    # Check set_port_polarity value for high out of bounds
    try:
        iobus.set_port_polarity(0, 256)
        pass
    except ValueError:
        print("value high boundary check: PASSED")
        pass
    except IOError:
        passed = False
        print("I2C IOError")
    else:
        passed = False
        print("value high boundary check: FAILED")
        pass

    # Logic Analyser Check
    print("Logic output Started")

    for x in range(0, 256):
        iobus.set_port_polarity(0, x)
        iobus.set_port_polarity(1, x)

    print("Logic output Ended")

    if passed is False:
        print("Test Failed")


if __name__ == "__main__":
    main()
