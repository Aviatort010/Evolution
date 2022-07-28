# This is the Biblary of cards for Evolution board game

import copy


class Card:
    def __init__(self, card_property="None", description="None",
                 start_pos=(0, 0), card_sizes=(100, 150)):
        self.property = card_property       # name of property
        self.description = description
        self.pos = start_pos
        self.additional_property = "None"

        self.x_size = int(round(card_sizes[0]))
        self.y_size = int(round(card_sizes[1]))

        # dots of edges of card (main dots), a start pos of card is a Left Down Angle
        self.dots = [start_pos,
                     [start_pos[0] + self.x_size, start_pos[1]],
                     [start_pos[0] + self.x_size, start_pos[1] + self.y_size],
                     [start_pos[0], start_pos[1] + self.y_size]]

        self.edges_width = self.x_size // 10

        # the external polygon of card
        self.color = [30, 50, 30]
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
                              [start_pos[0] + self.x_size - self.edges_width, start_pos[1] + self.y_size - self.edges_width],
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
                              [new_crd[0] + self.x_size - self.edges_width, new_crd[1] + self.y_size - self.edges_width],
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
