# Installation

## Install requirements

`pip install -r requirements.txt`

## Add your LinkedIn session tokens

2 of them are necessary:
- `li_at`
- `JSESSIONID`

## Install a MongoDB database

- Create a MongoDB database called `qr2`
- Host it on `127.0.0.1:27017` (should be done by default)

# Usage

Run `python main.py`.

It will fill your MongoDB database with quant researchers profiles. It should take around 2.5 hours.
