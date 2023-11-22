"""
Guitar
Estimate: 60 minutes
Actual:   82 minutes
"""

CURRENT_YEAR = 2023
VINTAGE_AGE = 50


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Initialise Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string with Guitar attributes."""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        """Calculate age of the Guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if guitar is vintage based on age."""
        return self.get_age() >= VINTAGE_AGE
