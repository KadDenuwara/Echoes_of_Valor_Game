# game setup
WIDTH = 1280
HEIGTH = 720
FPS = 60
TILESIZE = 64

HITBOX_OFFSET = {
    "player": -26,
    "object": -40,
    "grass": -10,
    "invincible": 0
}

#user interface
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = "Game/graphics/font/joystix.ttf"
TITLE_SCREEN_FONT = "Game/graphics/font/ThaleahFat.ttf"
UI_FONT_SIZE = 18

#colors
WATER_COLOR = "#71ddee"
UI_BG_COLOR = "#222222"
UI_BORDER_COLOR = "#111111"
TEXT_COLOR = "#EEEEEE"

#ui colors
HEALTH_COLOR = "Red"
ENERGY_COLOR = "Blue"
UI_COLOR_BORDER_ACTIVE = "Gold"

#upgrade menu
TEXT_COLOR_SELECTED = "#111111"
BAR_COLOR = "#EEEEEE"
BAR_COLOR_SELECTED = "#111111"
UPGRADE_BG_COLOR_SELECTED = "#EEEEEE"

#weapons
weapon_data = {
    "sword": {"cooldown": 100, "damage": 15, "graphic": "Game/graphics/weapons/sword/full.png"},
    "lance": {"cooldown": 400, "damage": 30, "graphic": "Game/graphics/weapons/lance/full.png"},
    "axe": {"cooldown": 300, "damage": 20, "graphic": "Game/graphics/weapons/axe/full.png"},
    "rapier": {"cooldown": 50, "damage": 8, "graphic": "Game/graphics/weapons/rapier/full.png"},
    "sai": {"cooldown": 80, "damage": 10, "graphic": "Game/graphics/weapons/sai/full.png"}
}

#magic
magic_data = {
    "flame": {"strength": 5, "cost": 20, "graphic": "Game/graphics/particles/flame/fire.png"},
    "heal": {"strength": 20, "cost": 10, "graphic": "Game/graphics/particles/heal/heal.png"}
}

#enemy
monster_data = {
    "squid": {"health": 100, "exp": 100, "damage": 20, "attack_type": "slash", "attack_sound": "Game/audio/attack/slash.wav", "speed": 3, "resistance": 3, "attack_radius": 80, "notice_radius": 360},
    "raccoon": {"health": 1300, "exp": 250, "damage": 40, "attack_type": "claw", "attack_sound": "Game/audio/attack/claw.wav", "speed": 3, "resistance": 3, "attack_radius": 120, "notice_radius": 400},
    "spirit": {"health": 100, "exp": 110, "damage": 8, "attack_type": "thunder", "attack_sound": "Game/audio/attack/fireball.wav", "speed": 3, "resistance": 3, "attack_radius": 60, "notice_radius": 350},
    "bamboo": {"health": 70, "exp": 120, "damage": 6, "attack_type": "leaf_attack", "attack_sound": "Game/audio/attack/slash.wav", "speed": 3, "resistance": 3, "attack_radius": 50, "notice_radius": 300}
}