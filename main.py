def on_button_multiplayer_right_pressed(player2):
    mp.get_player_sprite(player2).set_image(assets.image("""
        2
    """))
    if arrow.image.equals(assets.image("""
        2
    """)):
        mp.change_player_state_by(player2, MultiplayerState.score, 1)
mp.on_button_event(mp.MultiplayerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_right_pressed)

def on_button_multiplayer_down_pressed(player22):
    mp.get_player_sprite(player22).set_image(assets.image("""
        3
    """))
    if arrow.image.equals(assets.image("""
        3
    """)):
        mp.change_player_state_by(player22, MultiplayerState.score, 1)
mp.on_button_event(mp.MultiplayerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_down_pressed)

def on_button_multiplayer_left_pressed(player23):
    mp.get_player_sprite(player23).set_image(assets.image("""
        1
    """))
    if arrow.image.equals(assets.image("""
        1
    """)):
        mp.change_player_state_by(player23, MultiplayerState.score, 1)
mp.on_button_event(mp.MultiplayerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_left_pressed)

def on_button_multiplayer_up_pressed(player24):
    mp.get_player_sprite(player24).set_image(assets.image("""
        0
    """))
    if arrow.image.equals(assets.image("""
        0
    """)):
        mp.change_player_state_by(player24, MultiplayerState.score, 1)
mp.on_button_event(mp.MultiplayerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_up_pressed)

arrow: Sprite = None
arrow_list: List[Image] = []
scene.set_background_image(assets.image("""
    2pbg
"""))

def on_wrap1():
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.ONE),
        sprites.create(assets.image("""
            p1
        """), SpriteKind.player))
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE)).set_position(40, 90)
bundles.wrap1(on_wrap1)

def on_wrap2():
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.TWO),
        sprites.create(assets.image("""
            p2
        """), SpriteKind.player))
    mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO)).set_position(120, 90)
bundles.wrap2(on_wrap2)

def on_wrap3():
    global arrow_list, arrow
    arrow_list = [assets.image("""
            0
        """),
        assets.image("""
            1
        """),
        assets.image("""
            2
        """),
        assets.image("""
            3
        """)]
    arrow = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.player)
    arrow.set_position(80, 30)
bundles.wrap3(on_wrap3)

def on_wrap4():
    game.splash("Be the quickest to match", "arrow directions to win!")
    carnival.start_countdown_game(15, carnival.WinTypes.MULTI)
    music.play_sound_effect(music.create_sound_effect(WaveShape.TRIANGLE,
            4750,
            4783,
            255,
            0,
            449,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.UNTIL_DONE)
bundles.wrap4(on_wrap4)

def on_update_interval():
    arrow.set_image(arrow_list._pick_random())
game.on_update_interval(500, on_update_interval)
