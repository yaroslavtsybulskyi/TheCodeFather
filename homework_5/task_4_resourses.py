class InsufficientResourcesException(Exception):
    """
    Exception raised when user does not have enough resources to spend resources.
    """

    def __init__(self, required_resource: str, required_amount: int | float, current_amount: int | float) -> None:
        """
        Constructor
        :param required_resource: resource to spend
        :param required_amount: amount of resource to spend
        :param current_amount: current amount of resource available for spending
        """
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount
        self.message = (f"More {self.required_resource} needed, my Lord! "
                        f"Raise taxes to get {self.required_amount - self.current_amount} "
                        f"{self.required_resource}.")
        super().__init__(self.message)


class Person:
    """
    Game class
    """

    def __init__(self, name: str, gold: int | float, silver: int | float) -> None:
        """
        Constructor
        :param name: name of the person
        :param gold: amount of gold available
        :param silver: amount of silver available
        """
        self.name = name
        self.gold = gold
        self.silver = silver

    def spend_gold(self, amount: int | float, target: str) -> None:
        """
        Method that checks if gold can be spent.
        :param amount: amount of gold to spend
        :param target: the reason of the transaction
        """
        if amount < 0:
            raise ValueError('Amount must be positive')

        if amount > self.gold:
            raise InsufficientResourcesException("Gold", amount, self.gold)

        self.gold -= amount

        print(f"{self.name} spent {amount} gold on {target}. Balance left: {self.gold}")

    def spend_silver(self, amount: int | float, target: str) -> None:
        """
        Method that checks if silver can be spent.
        :param amount: amount of silver to spend
        :param target: goods to spend silver for
        """
        if amount < 0:
            raise ValueError('Amount must be positive')

        if amount > self.silver:
            raise InsufficientResourcesException("Silver", amount, self.silver)
        self.silver -= amount

        print(f"{self.name} spent {amount} silver on {target}. Balance left: {self.silver}")


if __name__ == "__main__":
    try:
        kirk = Person("Kirk", 100, 100)
        kirk.spend_silver(100, "Alimonies for Milhouse")
        kirk.spend_silver(5, "Beer")
    except InsufficientResourcesException as e:
        print(e)

    try:
        milhouse = Person("Milhouse", 100.5, 100)
        milhouse.spend_gold(100, "Gifts for Bart")
        milhouse.spend_gold(5.5, "Beer")
    except (InsufficientResourcesException, ValueError) as e:
        print(e)
