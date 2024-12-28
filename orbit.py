# orbit.py (Updated)
from engine.game_object import GameObject
from engine.draw import Draw
from engine.component.builtins import CircularColliderComponent
from random import randint

class Orbit(GameObject):
    def __init__(self, core, x_min, x_max, y_min, y_max, radius=10, lifetime=5000):
        x = randint(x_min, x_max)
        y = randint(y_min, y_max)
        super().__init__(core, x, y, radius * 2, radius * 2)
        self.radius = radius
        self.lifetime = lifetime
#         self.to_remove = False  # Mark for deletion when collected
    def on_start(self):
        self.add_component(CircularColliderComponent(self, self.radius))

    def on_update(self, delta_time):
        if self.lifetime > 0:
            self.lifetime -= delta_time
            if self.lifetime <= 0:
                self.to_remove = True  # Remove after lifetime expires

    def on_collision(self, player):
        # Trigger scoring event when player collects the orbit
        player.increase_score(10)  # Assuming player has an `increase_score` method
        self.to_remove = True

    def on_draw(self):
        Draw.change_color("#FFFF00")  # Yellow color
        Draw.circle(self.radius, 0, 0, False, 2)
