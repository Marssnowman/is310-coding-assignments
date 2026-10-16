from rich.console import Console
from rich.table import Table
import json
from pathlib import Path

console = Console()

example_games = [
    {
        "game_date": "2025-09-06",
        "home_team": "Example FBS University",
        "away_team": "Example FCS University",
        "home_level": "FBS",
        "away_level": "FCS",
        "payout_amount": "500000",
        "payout_source": "Example contract",
        "source_url": "https://example.com"
    }
]


def show_games(games, title):
    table = Table(title=title)

    table.add_column("Date")
    table.add_column("Home Team")
    table.add_column("Away Team")
    table.add_column("Home Level")
    table.add_column("Away Level")
    table.add_column("Payout")
    table.add_column("Source")

    for game in games:
        table.add_row(
            game["game_date"],
            game["home_team"],
            game["away_team"],
            game["home_level"],
            game["away_level"],
            game["payout_amount"],
            game["payout_source"]
        )

    console.print(table)


def get_level(prompt):
    while True:
        level = input(prompt).strip().upper()

        if level in ["FBS", "FCS"]:
            return level

        console.print("Please enter either FBS or FCS.", style="bold red")


def get_record():
    while True:
        console.print(
            "\nEnter information for a guarantee game:",
            style="bold cyan"
        )

        game = {
            "game_date": input("Game date (YYYY-MM-DD): ").strip(),
            "home_team": input("Home team: ").strip(),
            "away_team": input("Away team: ").strip(),
            "home_level": get_level("Home team level (FBS/FCS): "),
            "away_level": get_level("Away team level (FBS/FCS): "),
            "payout_amount": input("Payout amount: ").strip(),
            "payout_source": input("Payout source: ").strip(),
            "source_url": input("Source URL: ").strip()
        }

        show_games([game], "Review Your Entry")

        confirm = input("Is this information correct? (y/n): ").strip().lower()

        if confirm == "y":
            return game

        console.print("Please re-enter the record.", style="yellow")


console.print(
    "\nCollege Football Guarantee Game Data Entry Tool",
    style="bold green"
)

console.print(
    "\nHere is an example record:",
    style="bold cyan"
)

show_games(example_games, "Example Guarantee Game")

while True:
    try:
        number_of_games = int(
            input("\nHow many games would you like to enter? (minimum 2): ")
        )

        if number_of_games >= 2:
            break

        console.print("Please enter at least 2 games.", style="bold red")

    except ValueError:
        console.print("Please enter a whole number.", style="bold red")


new_games = []

for i in range(number_of_games):
    console.print(
        f"\nRecord {i + 1} of {number_of_games}",
        style="bold magenta"
    )

    new_games.append(get_record())


output_path = Path(__file__).parent / "sample_guarantee_games.json"

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(new_games, file, indent=4)


console.print(
    "\nData saved successfully!",
    style="bold green"
)

console.print(
    f"File location: {output_path.resolve()}",
    style="bold cyan"
)