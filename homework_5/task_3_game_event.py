class GameEventException(Exception):
    """
    Game event exception
    """

    def __init__(self, event_type: str, details: dict) -> None:
        self.event_type = event_type
        self.details = details
        self.message = f"{self.event_type}: Details: {self.details}"
        super().__init__(self.message)


class Game:
    """
    Game class
    """

    def __init__(self, player_name: str = 'Player') -> None:
        """
        Constructor
        :param player_name: name of the player
        """
        self.player_name = player_name
        self.health = 100
        self.experience = 0
        self.level = 1

    def take_damage(self, damage: int, reason: str = "Black Magic") -> None:
        """
        Takes damage to the player
        :param damage: damage to take
        :param reason: reason of the damage
        """
        self.health -= damage
        if self.health <= 0:
            raise GameEventException("Wasted!", {"reason": reason})

    def _level_up(self) -> None:
        """
        Level up function
        """
        self.level += 1
        print(f"{self.player_name} new level: {self.level}")

    def gain_experience(self, points: int) -> None:
        """
        Functions that adds experience to the player's experience
        :param points: points to add
        """
        if not isinstance(points, int):
            raise GameEventException("Points", {"points": points, "type": type(points).__name__})
        if points > 100:
            raise GameEventException("Gaining experience", {"points": points,
                                                            "cheater suspected": True})
        if points < 0:
            raise GameEventException("Gaining experience", {"points": points})

        self.experience += points

        if self.experience >= 50:
            self._level_up()
            self.experience -= 50


if __name__ == "__main__":
    game = Game()
    try:
        game.gain_experience(50)
        # game.take_damage(100)
        # game.gain_experience(102)
        game.gain_experience('100')
    except GameEventException as e:
        print(e.message)
        print(e.event_type)
        print(e.details)
