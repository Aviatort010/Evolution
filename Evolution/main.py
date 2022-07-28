# This is the Evolution electronic Board game.

import pygame as pg
from Cards_library import Library, Card


class Board:
    def __init__(self, window_dim: tuple, card_size: list):
        self.window_width = window_dim[0]
        self.main_color = [20, 12, 12]
        self.hand_color = [15, 9, 9]
        self.hand_polygon = [[0, 0], [0, card_size[1] + 40], [window_dim[0], card_size[1] + 40], [window_dim[0], 0]]
        self.card_size = card_size
        self.hand_cards_positions = []

    def give_hand_polygon(self):
        return self.hand_polygon

    def give_hand_positions(self):
        return self.hand_cards_positions

    def give_hand_color(self):
        return self.hand_color

    def give_main_color(self):
        return self.main_color


class Creature:
    def __init__(self):
        self.abilities = []
        self.hanger = 1
        self.food = 0


class Player:
    def __init__(self, name="New player"):
        self.name = name
        self.hand = []
        self.creatures = []

    def take_card(self, new_card: Card):
        self.hand.append(new_card)

    def give_hand(self):
        return self.hand

    def display_hand_cards(self, window_sizes, some_screen):
        # create hand cards positions
        cards_positions = []
        cards_number = len(self.hand)
        card_size = self.hand[0].give_sizes()
        if cards_number % 2 == 0:
            center = window_sizes[0] // 2
            for i in range(cards_number // 2):
                # to left from center
                cards_positions.append([(center + 5) - (i + 1) * (card_size[0] + 10), 20])
                # to right from center
                cards_positions.append([(center + 5) + i * (card_size[0] + 10), 20])
        else:
            pass

        # splitting cards with new positions
        for i in range(cards_number):
            self.hand[i].new_coordinates(cards_positions[i])

        # and now display a cards
        for some_card in self.hand:
            t_dots = true_dots(some_card.give_polygon(), window_sizes[1])
            pg.draw.polygon(some_screen, some_card.give_color(), t_dots)

            t_dots = true_dots(some_card.give_inner_polygon(), window_sizes[1])
            pg.draw.polygon(some_screen, some_card.give_inner_color(), t_dots)


def true_dots(dots, window_height):
    td = []
    for dot in dots:
        td.append([dot[0], -(dot[1] - window_height)])
    return td


def display_board(some_board: Board):
    t_dots = true_dots(some_board.give_hand_polygon(), wh)
    pg.draw.polygon(screen, some_board.give_hand_color(), t_dots)


# System settings
ww = 1600
wh = 1000
capt = "Evolution"
color_bkg = [5, 5, 5]

# Pygame settings
used_keys = [pg.K_q, pg.K_a, pg.K_w, pg.K_s, pg.K_e, pg.K_d,
             pg.K_UP, pg.K_DOWN]
pressed_keys = []

# Game settings
card_weight = 100
card_height = 150
board = Board((ww, wh), [card_weight, card_height])
cards_lib = Library()

player_one = Player()
for card in cards_lib.give_library():
    player_one.take_card(card)

# Initialization of Pygame
pg.init()

# Init screen (window of the game)
screen = pg.display.set_mode((ww, wh))
pg.display.set_caption(capt)

# Main cycle
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.KEYDOWN:
            if event.key in used_keys and event.key not in pressed_keys:
                pressed_keys += [event.key]
        elif event.type == pg.KEYUP:
            if event.key in pressed_keys:
                pressed_keys.remove(event.key)

    screen.fill(color_bkg)
    display_board(board)
    player_one.display_hand_cards((ww, wh), screen)
    pg.display.flip()
pg.quit()
