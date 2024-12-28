from engine.component.builtins import RigidBodyComponent, PhysicsComponent, ColliderComponent
from engine.draw import Draw
from engine.game_object import GameObject
from engine.input import Keys
from engine.picocore import PicoCore
from bullet import Bullet
import time


class Player(GameObject):
    def __init__(self, core, x, y, width=30, height=80, debug=False):
        super().__init__(core, x, y, width, height, debug=debug)
        self.processing_click = False
        self.processing_clock = 0

        self.height = height
        self.width = width
        self.jump_counter = 0
        self.dead = False
        self.speed = 2

        self.abilities = {
            "double_jump": True,
            "dash": True,
        }
        self.health = 3
        self.score = 0
        self.last_dash = time.time()

    def jump(self, physics_component: PhysicsComponent, delta_time):
        self.jump_counter += 1
        if self.jump_counter > 1:
            self.abilities["double_jump"] = False

        if self.abilities["double_jump"]:
            physics_component.velocity_y += 50 * delta_time

    def dash(self, physics_component: PhysicsComponent, delta_time):
        if self.abilities["dash"]:
            self.last_dash = time.time()
            physics_component.velocity_x += 100 * delta_time
            self.abilities["dash"] = False

    def on_start(self):
        self.add_component(PhysicsComponent(self))
        self.add_component(RigidBodyComponent(self, gravity=2000))
        self.add_component(ColliderComponent(self, self.width, self.height))
        self.scene = self.core.get_scene_manager().get_current_scene()

    def handle_shooting(self, delta_time):
        if PicoCore.is_pressed(Keys.LMB) and not self.processing_click:
            self.processing_click = True
            self.scene.add_game_object(Bullet(self.core, self.x + 30, self.y))

        if self.processing_click:
            self.processing_clock += delta_time

        if self.processing_clock >= 500:
            self.processing_click = False
            self.processing_clock = 0

    def handle_controls(self, physics_component: PhysicsComponent, delta_time):
        if PicoCore.is_pressed(Keys.d):
            physics_component.velocity_x += self.speed * delta_time
        elif PicoCore.is_pressed(Keys.a):
            physics_component.velocity_x -= self.speed * delta_time
        if PicoCore.is_pressed(Keys.SPACE, hold=False):
            self.jump(physics_component, delta_time)
        if PicoCore.is_pressed(Keys.e, hold=False):
            self.dash(physics_component, delta_time)

    def on_update(self, delta_time):
        physics_component: PhysicsComponent = self.get_component(PhysicsComponent)
        collider_component: ColliderComponent = self.get_component(ColliderComponent)

        if self.y < -50:
            self.health = 0

        if self.health <= 0:
            self.dead = True
            self.scene.paused = True

        if physics_component is not None:

            if time.time() - self.last_dash > 1:
                self.abilities["dash"] = True

            self.handle_controls(physics_component, delta_time)
            self.handle_shooting(delta_time)

    # def on_draw(self):
    #     Draw.change_color("#808080")  # Gray color for robot body
    #     if self.dead:
    #         Draw.change_color("#FF0000")  # Red color for dead robot
        
    #     # Body (rectangle)
    #     Draw.rect(20, 40, 0, 0, False, 2)
        
    #     # Head (circle)
    #     Draw.circle(10, 0, -20, False, 2)
        
    #     # Eyes (small circles)
    #     Draw.circle(2, -5, -25, False, 2)  # Left eye
    #     Draw.circle(2, 5, -25, False, 2)   # Right eye
        
    #     # Antennae (lines)
    #     Draw.line(0, -25, 0, -35)  # Left antennae
    #     Draw.line(0, -25, 0, -35)  # Right antennae
        
    #     # Arms (rectangles)
    #     Draw.rect(10, 20, -15, -30, False, 2)  # Left arm
    #     Draw.rect(10, 20, 15, -30, False, 2)   # Right arm
        
    #     # Hands (small rectangles)
    #     Draw.rect(5, 10, -20, -50, False, 2)  # Left hand
    #     Draw.rect(5, 10, 20, -50, False, 2)   # Right hand
        
    #     # Legs (rectangles)
    #     Draw.rect(10, 20, -15, -60, False, 2)  # Left leg
    #     Draw.rect(10, 20, 15, -60, False, 2)   # Right leg
        
    #     # Feet (small rectangles)
    #     Draw.rect(5, 10, -20, -80, False, 2)  # Left foot
    #     Draw.rect(5, 10, 20, -80, False, 2)   # Right foot
        

    def on_draw(self):
        Draw.change_color("#ffc0cb")
        if self.dead:
            Draw.change_color("#FF0000") 
        Draw.circle(10, 0, 0, False, 2)
        
        # Body (single straight line)
        Draw.line(0, -10, 0, -40)
        
        # Arms
        Draw.line(0, -15, -15, -25)  # Left arm
        Draw.line(0, -15, 15, -25)   # Right arm
        
        # Joints at shoulders
        Draw.circle(3, 0, -15, False, 2)  # Center shoulder joint
        Draw.circle(3, -15, -25, False, 2)  # Left arm joint
        Draw.circle(3, 15, -25, False, 2)   # Right arm joint
        
        # Legs
        Draw.line(0, -40, -15, -60)  # Left leg
        Draw.line(0, -40, 15, -60)   # Right leg
        
        # Joints at hips and feet
        Draw.circle(3, 0, -40, False, 2)    # Hip joint
        Draw.circle(3, -15, -60, False, 2)  # Left foot joint
        Draw.circle(3, 15, -60, False, 2)   # Right foot joint

# from engine.component.builtins import RigidBodyComponent, PhysicsComponent, ColliderComponent
# from engine.draw import Draw
# from engine.game_object import GameObject
# from engine.input import Keys
# from engine.picocore import PicoCore
# from bullet import Bullet
# from orbit import Orbit
# import time


# class Player(GameObject):
#     def __init__(self, core, x, y, width=30, height=80, debug=False):
#         super().__init__(core, x, y, width, height, debug=debug)
#         self.processing_click = False
#         self.processing_clock = 0
#         self.jump_counter = 0
#         self.dead = False
#         self.speed = 2
#         self.abilities = {"double_jump": True, "dash": True}
#         self.health = 3
#         self.score = 0
#         self.last_dash = time.time()

#     def jump(self, physics_component: PhysicsComponent, delta_time):
#         self.jump_counter += 1
#         if self.jump_counter > 1:
#             self.abilities["double_jump"] = False
#         if self.abilities["double_jump"]:
#             physics_component.velocity_y += 50 * delta_time

#     def dash(self, physics_component: PhysicsComponent, delta_time):
#         if self.abilities["dash"]:
#             self.last_dash = time.time()
#             physics_component.velocity_x += 100 * delta_time
#             self.abilities["dash"] = False

#     def collect_orbit(self):
#         """Increase score when collecting an orbit."""
#         self.score += 10
#         print(f"Score: {self.score}")

#     def on_start(self):
#         self.add_component(PhysicsComponent(self))
#         self.add_component(RigidBodyComponent(self, gravity=2000))
#         self.add_component(ColliderComponent(self, self.width, self.height))
#         self.scene = self.core.get_scene_manager().get_current_scene()

#     def handle_controls(self, physics_component: PhysicsComponent, delta_time):
#         if PicoCore.is_pressed(Keys.d):
#             physics_component.velocity_x += self.speed * delta_time
#         elif PicoCore.is_pressed(Keys.a):
#             physics_component.velocity_x -= self.speed * delta_time
#         if PicoCore.is_pressed(Keys.SPACE, hold=False):
#             self.jump(physics_component, delta_time)
#         if PicoCore.is_pressed(Keys.e, hold=False):
#             self.dash(physics_component, delta_time)

#     def check_collisions(self):
#         player_collider = self.get_component(ColliderComponent)
#         if player_collider is None:
#             return
#         collisions = []
#         for obj in self.scene.get_game_objects():
#             obj_collider = obj.get_component(ColliderComponent)
#             if obj_collider and player_collider.collides_with(obj_collider):
#                 if isinstance(obj, Orbit):  # Check for Orbit collision
#                     self.collect_orbit()
#                     collisions.append(obj)
#         for obj in collisions:
#             self.scene.remove_game_object(obj)

#     def on_update(self, delta_time):
#         physics_component: PhysicsComponent = self.get_component(PhysicsComponent)
#         if self.y < -50:
#             self.health = 0
#         if self.health <= 0:
#             self.dead = True
#             self.scene.paused = True
#         if physics_component is not None:
#             if time.time() - self.last_dash > 1:
#                 self.abilities["dash"] = True
#             self.handle_controls(physics_component, delta_time)
#             self.check_collisions()

#     def on_draw(self):
#         Draw.change_color("#ffc0cb")
#         if self.dead:
#             Draw.change_color("#FF0000")

#         Draw.circle(10, 0, 0, False, 2)

#         # Body (single straight line)
#         Draw.line(0, -10, 0, -40)

#         # Arms
#         Draw.line(0, -15, -15, -25)  # Left arm
#         Draw.line(0, -15, 15, -25)   # Right arm

#         # Joints at shoulders
#         Draw.circle(3, 0, -15, False, 2)  # Center shoulder joint
#         Draw.circle(3, -15, -25, False, 2)  # Left arm joint
#         Draw.circle(3, 15, -25, False, 2)   # Right arm joint

#         # Legs
#         Draw.line(0, -40, -15, -60)  # Left leg
#         Draw.line(0, -40, 15, -60)   # Right leg

#         # Joints at hips and feet
#         Draw.circle(3, 0, -40, False, 2)    # Hip joint
#         Draw.circle(3, -15, -60, False, 2)  # Left foot joint
#         Draw.circle(3, 15, -60, False, 2)   # Right foot joint
