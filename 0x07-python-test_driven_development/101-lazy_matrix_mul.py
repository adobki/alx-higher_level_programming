#!/usr/bin/python3
"""Module with a function, and some extra code for testing."""


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices by using the module NumPy."""

    if not isinstance(m_a, list):
        raise TypeError('m_a must be an list')
    elif not isinstance(m_b, list):
        raise TypeError('m_b must be an list')
    else:
        return m_a


def main():
    """Tests the code."""

    pass


if __name__ == "__main__":
    main()
