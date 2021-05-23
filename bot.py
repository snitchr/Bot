# import os
import sys
import asyncio
import time
sys.path.append('../../')

from bfxapi import Client

bfx = Client(
  logLevel='DEBUG',
)

days = 1
now = int(round(time.time() * 1000))
then = now - (1000 * 60 * 60 * 24 * days)
allDay = (60 * 24 * days)

#orschloch

async def log_ticker():
  ticker = await bfx.rest.get_public_ticker('tBTCUSD')
  print("Ticker:")
  print(ticker)

async def log_historical_candles():
  candles = await bfx.rest.get_public_candles('tBTCUSD', 0, then, section='hist', tf='1m', limit=allDay, sort=-1)
  print ("Candles:")
  [ print (c) for c in candles ]

#
async def run():
  await log_ticker()
  await log_historical_candles()


t = asyncio.ensure_future(run())
asyncio.get_event_loop().run_until_complete(t)