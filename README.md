# Installation

## Install requirements

`pip install -r requirements.txt`

## Add your LinkedIn session tokens

Create a `.env` file at the root of the project and add these 2 fields:
- `li_at`
- `JSESSIONID`
You can find their value at linkedin.com by logging into your account

## Install a MongoDB database

- Create a MongoDB database called `qr2`
- Host it on `127.0.0.1:27017` (should be done by default)

# Usage

Run `python main.py`.

It will fill your MongoDB database with quant researchers profiles. It should take around 2.5 hours.
