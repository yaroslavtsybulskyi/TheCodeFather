"""
Module: evolution_simulation
----------------------------
This module simulates the evolution of a population of organisms using multithreading.
Each organism can eat, reproduce, and its health changes over time.
If an organism's health reaches zero, it dies and is removed from the population.
New offspring are added to the population under specific conditions.
"""

import threading
import random
from typing import List, Optional


class Organism:
    """Represents an organism that eats, reproduces, and has health."""

    def __init__(self, name: str, health: int = random.randint(20, 60),
                 food: int = random.randint(5, 40)) -> None:
        """
        Initializes an organism with a name, random health, and food levels.
        :param name:  The name of the organism.
        :param health: The initial health of the organism (default: 20-60).
        :param food: The initial food level of the organism (default: 5-40).
        :raises TypeError: If name is not a string.
        :raises TypeError: If health is not an integer.
        :raises TypeError: If food is not an integer.
        """
        if not isinstance(name, str):
            raise TypeError('Name must be a string.')
        if not isinstance(health, int):
            raise TypeError('Health must be an integer.')
        if not isinstance(food, int):
            raise TypeError('Food must be an integer.')

        self.name = name
        self.health = health
        self.food = food
        self.lock = threading.Lock()

    def eat(self) -> None:
        """
        Increases the organism's food level. The maximum food level is 100.
        :return: None
        """
        with self.lock:
            self.food = min(self.food + random.randint(10, 20), 100)

    def reproduce(self) -> Optional["Organism"]:
        """
        Allows the organism to reproduce if it has sufficient food.
        The food level is reduced upon reproduction.
        :return: A new Organism instance (offspring) if reproduction is successful, otherwise None.
        """
        with self.lock:
            if self.food > 60:
                self.food -= 55
                return Organism(f"Offspring of {self.name}")
        return None

    def update_health(self) -> bool:
        """
        Updates the organism's health based on its food level.
        :return: True if the organism is still alive, False if it has died.
        """
        with self.lock:
            if self.food <= 50:
                self.health -= 15
            else:
                self.health = min(self.health + random.randint(0, 15), 100)
            return self.health > 0


def evolution(organism: Organism, population: List[Organism],
              population_lock: threading.Lock) -> None:
    """
    Simulates the evolution of an organism.
    :param organism: The organism being evolved.
    :param population: The shared population list.
    :param population_lock: A lock to safely modify the population list.
    :raises TypeError: If organism is not an instance of Organism.
    :raises TypeError: If population is not a list.
    :raises TypeError: If population_lock is not a lock.
    """
    if not isinstance(organism, Organism):
        raise TypeError('Organism must be an instance of Organism.')
    if not isinstance(population, list):
        raise TypeError('Population list must be an instance of list.')
    if not isinstance(population_lock, threading.Lock):
        raise TypeError('Population lock must be an instance of threading.Lock.')
    print(f"{organism.name} (Health: {organism.health} Food: {organism.food})")

    organism.eat()
    offspring = organism.reproduce()

    if not organism.update_health():
        print(f"Say bye to {organism.name}")
        with population_lock:
            population.remove(organism)
        return

    if offspring:
        print(f"New offspring of {organism.name}")
        with population_lock:
            population.append(offspring)


def main() -> None:
    """
    Runs the evolution simulation for 5 generations.
    Each generation runs multiple threads in parallel to evolve the organisms.
    Organisms may die or reproduce, changing the population size dynamically.
    :return: None
    """
    population_lock = threading.Lock()
    population = [Organism("Tiger"), Organism("Bat"), Organism("Lion")]

    for generation in range(5):
        print(f"\nGeneration {generation + 1}")

        threads = []
        for organism in list(population):
            thread = threading.Thread(target=evolution, args=(organism, population, population_lock))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        if not population:
            print("All organisms have died. Evolution ends.")
            return

    print("\nFinal population:")
    for organism in population:
        print(f"{organism.name} (Health: {organism.health}, Food: {organism.food})")


if __name__ == "__main__":
    main()
