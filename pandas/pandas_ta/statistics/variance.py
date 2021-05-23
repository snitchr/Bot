# -*- coding: utf-8 -*-
from pandas_ta.utils import get_offset, verify_series


def variance(close, length=None, ddof=None, offset=None, **kwargs):
    """Indicator: Variance"""
    # Validate Arguments
    length = int(length) if length and length > 1 else 30
    ddof = int(ddof) if ddof and ddof >= 0 and ddof < length else 0
    min_periods = int(kwargs["min_periods"]) if "min_periods" in kwargs and kwargs["min_periods"] is not None else length
    close = verify_series(close, max(length, min_periods))
    offset = get_offset(offset)

    if close is None: return

    # Calculate Result
    variance = close.rolling(length, min_periods=min_periods).var(ddof)

    # Offset
    if offset != 0:
        variance = variance.shift(offset)

    # Handle fills
    if "fillna" in kwargs:
        variance.fillna(kwargs["fillna"], inplace=True)
    if "fill_method" in kwargs:
        variance.fillna(method=kwargs["fill_method"], inplace=True)

    # Name & Category
    variance.name = f"VAR_{length}"
    variance.category = "statistics"

    return variance


variance.__doc__ = \
"""Rolling Variance

Sources:

Calculation:
    Default Inputs:
        length=30
    VARIANCE = close.rolling(length).var()

Args:
    close (pd.Series): Series of 'close's
    length (int): It's period. Default: 30
    ddof (int): Delta Degrees of Freedom.
                The divisor used in calculations is N - ddof,
                where N represents the number of elements. Default: 0
    offset (int): How many periods to offset the result. Default: 0

Kwargs:
    fillna (value, optional): pd.DataFrame.fillna(value)
    fill_method (value, optional): Type of fill method

Returns:
    pd.Series: New feature generated.
"""
