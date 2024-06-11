#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == '__main__':
    player = Player("Nick") 
    player_2 = Player("Ari")
    player_3 = Player("Saaammmm")
    player_4 = Player(4)
    game_1 = Game("Skribbl.io")
    game_2 = Game("Jenga")
    game_3 = Game(3)
    Result(player, game_1, 5000)
    Result(player_2, game_2, 4999)
    
    ipdb.set_trace()
