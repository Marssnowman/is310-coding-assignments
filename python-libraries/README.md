# College Football Guarantee Game Data Entry Tool

## Overview

This project is a data-curation tool for collecting information about college football guarantee games. A guarantee game is a game in which one school pays another school to play.

The project is related to my semester project about the financial relationships behind college football games.

## Data Collected

The tool collects the following fields:

- Game date
- Home team
- Away team
- Home team level (FBS or FCS)
- Away team level (FBS or FCS)
- Payout amount
- Payout source
- Source URL

## Python CLI Version

The Python CLI uses the Rich library to display example data and review records.

The user can enter multiple guarantee game records. Each record is displayed for review before it is saved. The completed data is saved as:

`sample_guarantee_games.json`

### Setup

Create and activate a Python virtual environment, then install the required packages:

```powershell
python -m pip install -r requirements.txt