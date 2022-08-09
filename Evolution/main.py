# This is the Evolution electronic Board game.

import pygame as pg
import copy


class Card:
    def __init__(self, card_property="None", description="None",
                 start_pos=(0, 0), card_sizes=(120, 150)):
        self.property = card_property  # name of property
        self.description = description
        self.pos = start_pos
        self.additional_property = "None"

        self.x_size = int(round(card_sizes[0]))
        # self.y_size = int(round(card_sizes[1]))
        self.y_size = int(round(card_sizes[0] / 2 * 3))

        # dots of edges of card (main dots), a start pos of card is a Left Down Angle
        self.dots = [start_pos,
                     [start_pos[0], start_pos[1] + self.y_size],
                     [start_pos[0] + self.x_size, start_pos[1] + self.y_size],
                     [start_pos[0] + self.x_size, start_pos[1]]]

        self.edges_width = self.x_size // 18

        # the external polygon of card
        self.color = [10, 30, 10]
        self.card_polygon = [[start_pos[0] + self.edges_width, start_pos[1]],
                             [start_pos[0], start_pos[1] + self.edges_width],
                             [start_pos[0], start_pos[1] + self.y_size - self.edges_width],
                             [start_pos[0] + self.edges_width, start_pos[1] + self.y_size],
                             [start_pos[0] + self.x_size - self.edges_width, start_pos[1] + self.y_size],
                             [start_pos[0] + self.x_size, start_pos[1] + self.y_size - self.edges_width],
                             [start_pos[0] + self.x_size, start_pos[1] + self.edges_width],
                             [start_pos[0] + self.x_size - self.edges_width, start_pos[1]]]
        # the inner "light" polygon of card
        self.inner_color = [50, 70, 50]
        self.inner_polygon = [[start_pos[0] + self.edges_width, start_pos[1] + self.edges_width],
                              [start_pos[0] + self.edges_width, start_pos[1] + self.y_size - self.edges_width],
                              [start_pos[0] + self.x_size - self.edges_width,
                               start_pos[1] + self.y_size - self.edges_width],
                              [start_pos[0] + self.x_size - self.edges_width, start_pos[1] + self.edges_width]]

    def add_additional_property(self, some_add_prop: str):
        self.additional_property = some_add_prop

    def give_dots(self):
        return self.dots

    def give_polygon(self):
        return self.card_polygon

    def give_color(self):
        return self.color

    def give_inner_polygon(self):
        return self.inner_polygon

    def give_inner_color(self):
        return self.inner_color

    def give_sizes(self):
        return [self.x_size, self.y_size]

    def give_text_property(self):
        return self.property

    def give_text_prop_coord(self):
        return [self.dots[0][0] + self.x_size // 2, self.dots[0][1] + int(round((self.y_size * 0.85)))]

    def move(self, x, y):
        for dot in self.dots:
            dot[0] += x
            dot[1] += y

    def new_coordinates(self, new_crd: list):
        self.dots = [new_crd,
                     [self.x_size + new_crd[0], new_crd[1]],
                     [self.x_size + new_crd[0], self.y_size + new_crd[1]],
                     [new_crd[0], self.y_size + new_crd[1]]]

        self.card_polygon = [[new_crd[0] + self.edges_width, new_crd[1]],
                             [new_crd[0], new_crd[1] + self.edges_width],
                             [new_crd[0], new_crd[1] + self.y_size - self.edges_width],
                             [new_crd[0] + self.edges_width, new_crd[1] + self.y_size],
                             [new_crd[0] + self.x_size - self.edges_width, new_crd[1] + self.y_size],
                             [new_crd[0] + self.x_size, new_crd[1] + self.y_size - self.edges_width],
                             [new_crd[0] + self.x_size, new_crd[1] + self.edges_width],
                             [new_crd[0] + self.x_size - self.edges_width, new_crd[1]]]

        self.inner_polygon = [[new_crd[0] + self.edges_width, new_crd[1] + self.edges_width],
                              [new_crd[0] + self.edges_width, new_crd[1] + self.y_size - self.edges_width],
                              [new_crd[0] + self.x_size - self.edges_width,
                               new_crd[1] + self.y_size - self.edges_width],
                              [new_crd[0] + self.x_size - self.edges_width, new_crd[1] + self.edges_width]]

    def new_sizes(self, new_s):
        self.x_size = int(round(new_s[0]))
        self.y_size = int(round(new_s[1]))

        self.edges_width = self.x_size // 10

        center = self.dots[0]
        self.dots = [center,
                     [self.x_size + center[0], center[1]],
                     [self.x_size + center[0], self.y_size + center[1]],
                     [center[0], self.y_size + center[1]]]

        self.card_polygon = [[center[0] + self.edges_width, center[1]],
                             [center[0], center[1] + self.edges_width],
                             [center[0], center[1] + self.y_size - self.edges_width],
                             [center[0] + self.edges_width, center[1] + self.y_size],
                             [center[0] + self.x_size - self.edges_width, center[1] + self.y_size],
                             [center[0] + self.x_size, center[1] + self.y_size - self.edges_width],
                             [center[0] + self.x_size, center[1] + self.edges_width],
                             [center[0] + self.x_size - self.edges_width, center[1]]]

        self.inner_polygon = [[center[0] + self.edges_width, center[1] + self.edges_width],
                              [center[0] + self.edges_width, center[1] + self.y_size - self.edges_width],
                              [center[0] + self.x_size - self.edges_width, center[1] + self.y_size - self.edges_width],
                              [center[0] + self.x_size - self.edges_width, center[1] + self.edges_width]]


class Library:
    def __init__(self):
        self.library = []

        camouflage = Card("КАМУФЛЯЖ", "@ может быть атаковано только хищником со свойством ОСТРОЕ ЗРЕНИЕ.")
        camouflage.add_additional_property("ЖИРОВОЙ ЗАПАС")
        for i in range(4):
            self.library.append(copy.copy(camouflage))

        burrowing = Card("НОРНОЕ", "Когда @ НАКОРМЛЕНО, оно не может быть атаковано хищником.")
        burrowing.add_additional_property("ЖИРОВОЙ ЗАПАС")
        for i in range(4):
            self.library.append(copy.copy(burrowing))

        sharp_vision = Card("ОСТРОЕ ЗРЕНИЕ", "Хищник с этим свойством может атаковать @ со свойством камуфляж.")
        sharp_vision.add_additional_property("ЖИРОВОЙ ЗАПАС")
        for i in range(4):
            self.library.append(copy.copy(sharp_vision))

    def give_library(self):
        return self.library


class Board:
    def __init__(self, window_dim: tuple, card_size: list):
        self.window_width = window_dim[0]
        self.main_color = [20, 12, 12]
        self.hand_color = [70, 65, 65]
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

            font = pg.font.Font(None, 18)
            prop_text = font.render(some_card.give_text_property(), True, some_card.give_color())
            prop_text_place = prop_text.get_rect(center=true_dots([some_card.give_text_prop_coord()], window_sizes[1])[0])
            some_screen.blit(prop_text, prop_text_place)


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
