from app.players import Player
from app.players import Elf
from app.players import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    result = 0
    for user in players:
        result += user.get_rating()
    return result


def elves_concert(elfs: list[Elf]) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list[Dwarf]) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
