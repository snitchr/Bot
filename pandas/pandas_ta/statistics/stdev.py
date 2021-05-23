# -*- coding: utf-8 -*-
from numpy import sqrt as npsqrt
from .variance import variance
from pandas_ta.utils import get_offset, verify_series


def stdev(close, length=None, ddof=None, offset=None, **kwargs):
    """Indicator: Standard Deviation"""
    # Validate Arguments
    length = int(length) if length and length > 0 else 30
    ddof = int(ddof) if ddof and ddof >= 0 and ddof < length else 1
    close = verify_series(close, length)
    offset = get_offset(offset)

    if close is None: return

    # Calculate Result
    stdev = variance(close=close, length=length, ddof=ddof).apply(npsqrt)

    # Offset
    if offset != 0:
        stdev = stdev.shift(offset)

    # Handle fills
    if "fillna" in kwargs:
        stdev.fillna(kwargs["fillna"], inplace=True)
    if "fill_method" in kwargs:
        stdev.fillna(method=kwargs["fill_method"], inplace=True)

    # Name & Category
    stdev.name = f"STDEV_{length}"
    stdev.category = "statistics"

    return stdev


stdev.__doc__ = \
"""Rolling Standard Deviation

Sources:

Calculation:
    Default Inputs:
        length=30
    VAR = Variance
    STDEV = variance(close, length).apply(np.sqrt)

Args:
    close (pd.Series): Series of 'close's
    length (int): It's period. Default: 30
    ddof (int): Delta Degrees of Freedom.
                The divisor used in calculations is N - ddof,
                where N represents the number of elements. Default: 1
    offset (int): How many periods to offset the result. Default: 0

Kwargs:
    fillna (value, optional): pd.DataFrame.fillna(value)
    fill_method (value, optional): Type of fill method

Returns:
    pd.Series: New feature generated.
"""
