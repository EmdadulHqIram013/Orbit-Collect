from back_button import BackButton
from block import Block
from engine.label import Label
from enemy import EnemyOne, EnemyTwo, EnemyThree
from engine.button import Button
from engine.draw import Draw
from engine.label import Label
from engine.picocore import PicoCore
from engine.scene.scene import Scene
from player import Player
from random import randint, choice, getrandbits
from engine.input import Keys
from score_system import ScoreSystem
#####################
from orbit import Orbit
###############################
enemy_types = [EnemyOne, EnemyTwo, EnemyThree]


class PlayPauseButton(Button):
    def __init__(self, core, x, y):
        super().__init__(core, x, y, width=25, height=25)
        self.paused = False

    def on_click(self):
        PicoCore.get_scene_manager().current_scene.paused = not PicoCore.get_scene_manager().current_scene.paused
        self.paused = PicoCore.get_scene_manager().current_scene.paused

    def on_draw(self):
        Draw.change_color("#2FF518")

        if self.paused:
            Draw.line(0, 0, 0, -25, width=2)
            Draw.line(0, 0, 20, -12, width=2)
            Draw.line(0, -25, 20, -12, width=2)
        else:
            Draw.line(0, 0, 0, -25, width=2)
            Draw.line(20, 0, 20, -25, width=2)


class Ability(Label):
    def __init__(self, core, text, x, y, ability, player):
        super().__init__(core, text, x, y, size=2)
        self.ability = ability
        self.text = text
        self.player = player
        self.status = player.abilities[ability]

    def on_start(self):
        pass

    def on_click(self):
        pass

    def on_update(self, delta_time):
        self.status = self.player.abilities[self.ability]

    def on_draw(self):
        if self.status:
            Draw.change_color("#00FF00")
        else:
            Draw.change_color("#FF0000")
        Draw.text(self.text, 0, 0, size=20)
        Draw.change_color("#FFFFFF")


class GameOverLabel(Label):
    def __init__(self, core, player):
        super().__init__(
            core,
            "GAME OVER",
            (core.width / 2),
            (core.height / 2) + 100,
            visible=False,
            color="#FF0000",
            size=30,
            alignment="center"
        )
        self.player = player
        self.game_over = False
        self.saved_score = False

    def on_update(self, delta_time):
        if self.player.health <= 0:
            self.game_over = True
            self.visible = True

            if not self.saved_score:
                self.saved_score = True
                ScoreSystem().add_score(PicoCore.get_state("score"))


class FPSLabel(Label):

    def on_update(self, delta_time):
        super().on_update(delta_time)
        self.text = str(round(1000 / delta_time))


class HealthLabel(Label):

    def on_update(self, delta_time):
        super().on_update(delta_time)
        self.text = str(PicoCore.get_state("lives")) + " LIVES"


class ScoreLabel(Label):

    def on_update(self, delta_time):
        super().on_update(delta_time)
        self.text = "SCORE " + str(PicoCore.get_state("score"))


# def get_level_scene(engine: PicoCore) -> Scene:
#     level = Scene(engine)

#     player = Player(engine, 200, 500)

#     PicoCore.set_state("lives", player.health)
#     PicoCore.set_state("score", player.score)

#     play_pause_button = PlayPauseButton(engine, engine.width / 2, engine.height - 50)
#     double_jump_ability = Ability(engine, "JUMP", 50, 90, "double_jump", player)
#     dash_ability = Ability(engine, "DASH", 200, 90, "dash", player)

#     for i in range(100):
#         x_space = randint(100, 200)
#         y_space = randint(100, 200)
#         falling_chance = randint(0, 10)  # first block should not fall
#         level.add_game_object(
#             Block(engine, (i * 300) + x_space, y_space, width=200, height=50, falling=falling_chance < 4 and i != 0))
#         if i % 8 == 0 and i > 4:
#             enemy = choice(enemy_types)(engine, (i * 200) + x_space, y_space + 50, 100, 100)
#             level.add_game_object(enemy)
    
#     level.add_ui_object(play_pause_button)
#     level.add_ui_object(BackButton(engine, 40, engine.height - 50))
#     level.add_ui_object(FPSLabel(engine, "0", engine.width - 80, engine.height - 50))
#     level.add_ui_object(double_jump_ability)
#     level.add_ui_object(dash_ability)
#     level.add_ui_object(ScoreLabel(engine, str(PicoCore.get_state("score")), 40, 40))
#     level.add_ui_object(HealthLabel(engine, str(PicoCore.get_state("lives")), engine.width - 120, 40))
#     level.add_ui_object(GameOverLabel(engine, player))

#     level.add_game_object(player)

#     level.camera.follow(player, 300, 300)
#     return level

def get_level_scene(engine: PicoCore) -> Scene:
    level = Scene(engine)

    player = Player(engine, 200, 500)

    PicoCore.set_state("lives", player.health)
    PicoCore.set_state("score", player.score)

    play_pause_button = PlayPauseButton(engine, engine.width / 2, engine.height - 50)
    double_jump_ability = Ability(engine, ".", 50, 90, "double_jump", player)
    dash_ability = Ability(engine, ".", 200, 90, "dash", player)

    for i in range(100):
        x_space = randint(100, 200)
        y_space = randint(100, 200)
        falling_chance = randint(0, 10)
        level.add_game_object(
            Block(engine, (i * 300) + x_space, y_space, width=200, height=50, falling=falling_chance < 4 and i != 0))
        if i % 8 == 0 and i > 4:
            enemy = choice(enemy_types)(engine, (i * 200) + x_space, y_space + 50, 100, 100)
            level.add_game_object(enemy)

    # Add UI Objects
    level.add_ui_object(play_pause_button)
    level.add_ui_object(BackButton(engine, 40, engine.height - 50))
    level.add_ui_object(FPSLabel(engine, "0", engine.width - 80, engine.height - 50))
    level.add_ui_object(double_jump_ability)
    level.add_ui_object(dash_ability)
    level.add_ui_object(ScoreLabel(engine, str(PicoCore.get_state("score")), 40, 40))
    level.add_ui_object(HealthLabel(engine, str(PicoCore.get_state("lives")), engine.width - 120, 40))
    level.add_ui_object(GameOverLabel(engine, player))

    # Add Player to Level
    level.add_game_object(player)

    # Add Camera to Follow Player
    level.camera.follow(player, 300, 300)

    # Add Spawning Logic for Orbits
    def spawn_objects(delta_time):
        if randint(0, 100) < 5:  # 5% chance to spawn Orbit
            level.add_game_object(Orbit(engine, 0, 800, 0, 600))

    # Override the update function to include spawning logic
    original_update = level.update

    def custom_update(delta_time):
        spawn_objects(delta_time)  # Spawn orbits
        original_update(delta_time)  # Call the original update logic

    level.update = custom_update

    return level
