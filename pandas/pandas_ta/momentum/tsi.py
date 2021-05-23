# -*- coding: utf-8 -*-
from pandas_ta.overlap import ema
from pandas_ta.utils import get_drift, get_offset, verify_series


def tsi(close, fast=None, slow=None, scalar=None, drift=None, offset=None, **kwargs):
    """Indicator: True Strength Index (TSI)"""
    # Validate Arguments
    fast = int(fast) if fast and fast > 0 else 13
    slow = int(slow) if slow and slow > 0 else 25
    # if slow < fast:
    #     fast, slow = slow, fast
    scalar = float(scalar) if scalar else 100
    close = verify_series(close, max(fast, slow))
    drift = get_drift(drift)
    offset = get_offset(offset)
    if "length" in kwargs: kwargs.pop("length")

    if close is None: return

    # Calculate Result
    diff = close.diff(drift)
    slow_ema = ema(close=diff, length=slow, **kwargs)
    fast_slow_ema = ema(close=slow_ema, length=fast, **kwargs)

    abs_diff = diff.abs()
    abs_slow_ema = ema(close=abs_diff, length=slow, **kwargs)
    abs_fast_slow_ema = ema(close=abs_slow_ema, length=fast, **kwargs)

    tsi = scalar * fast_slow_ema / abs_fast_slow_ema

    # Offset
    if offset != 0:
        tsi = tsi.shift(offset)

    # Handle fills
    if "fillna" in kwargs:
        tsi.fillna(kwargs["fillna"], inplace=True)
    if "fill_method" in kwargs:
        tsi.fillna(method=kwargs["fill_method"], inplace=True)

    # Name and Categorize it
    tsi.name = f"TSI_{fast}_{slow}"
    tsi.category = "momentum"

    return tsi


tsi.__doc__ = \
"""True Strength Index (TSI)

The True Strength Index is a momentum indicator used to identify short-term
swings while in the direction of the trend as well as determining overbought
and oversold conditions.

Sources:
    https://www.investopedia.com/terms/t/tsi.asp

Calculation:
    Default Inputs:
        fast=13, slow=25, scalar=100, drift=1
    EMA = Exponential Moving Average
    diff = close.diff(drift)

    slow_ema = EMA(diff, slow)
    fast_slow_ema = EMA(slow_ema, slow)

    abs_diff_slow_ema = absolute_diff_ema = EMA(ABS(diff), slow)
    abema = abs_diff_fast_slow_ema = EMA(abs_diff_slow_ema, fast)

    TSI = scalar * fast_slow_ema / abema

Args:
    close (pd.Series): Series of 'close's
    fast (int): The short period. Default: 13
    slow (int): The long period. Default: 25
    scalar (float): How much to magnify. Default: 100
    drift (int): The difference period. Default: 1
    offset (int): How many periods to offset the result. Default: 0

Kwargs:
    fillna (value, optional): pd.DataFrame.fillna(value)
    fill_method (value, optional): Type of fill method

Returns:
    pd.Series: New feature generated.
"""
