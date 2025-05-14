import random

class Player:
    def __init__(self, id, name, icon, position=1):
        self.id = id              # accept id explicitly
        self.name = name
        self.icon = icon
        self.position = position  # Start at cell 1 (zigzag numbering)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'icon': self.icon,
            'position': self.position,
        }

    @classmethod
    def deserialize(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            icon=data['icon'],
            position=data.get('position', 1),
        )

class Game:
    ICONS = ["🎩", "🐱", "🧙‍♂️", "🐶", "🦊", "🐼", "🐸", "🐵", "🐧", "🦄"]

    LADDERS = {
        2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84,
        36: 44, 51: 67, 78: 98, 71: 91, 87: 94,
    }
    SNAKES = {
        16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53,
        89: 68, 92: 88, 95: 75, 99: 80,
    }

    def __init__(self, num_players):
        self.num_players = num_players
        # Pass id, name, icon correctly
        self.players = [Player(i, f"Player {i+1}", self.ICONS[i]) for i in range(num_players)]
        self.current_turn = 0
        self.messages = []
        self.last_move = None

    def roll_dice(self):
        return random.randint(1, 6)

    def next_turn(self):
        player = self.players[self.current_turn]
        dice = self.roll_dice()
        old_position = player.position
        new_position = old_position + dice

        if new_position > 100:
            new_position = old_position  # Can't move beyond 100

        move_msg = f"{player.icon} rolled a 🎲 {dice} and moved from {old_position} to {new_position}"

        # Check ladders
        if new_position in self.LADDERS:
            destination = self.LADDERS[new_position]
            move_msg += f" 🚀 Climbed a ladder to {destination}"
            new_position = destination

        # Check snakes
        elif new_position in self.SNAKES:
            destination = self.SNAKES[new_position]
            move_msg += f" 🐍 Bitten by a snake down to {destination}"
            new_position = destination

        player.position = new_position
        self.messages.append(move_msg)
        self.last_move = {
            'player_name': player.name,
            'old_position': old_position,
            'new_position': new_position,
            'player_icon': player.icon,
            'dice_roll': dice,
            'message': move_msg,
        }

        self.current_turn = (self.current_turn + 1) % len(self.players)

    def get_winner(self):
        for player in self.players:
            if player.position == 100:
                return {
                    'name': player.name,
                    'icon': player.icon,
                    'position': player.position,
                }
        return None

    def is_finished(self):
        return self.get_winner() is not None

    def serialize(self):
        return {
            'players': [player.serialize() for player in self.players],
            'current_turn': self.current_turn,
            'messages': self.messages,
            'last_move': self.last_move,
            'winner': self.get_winner(),  # call method, not reference
            'num_players': self.num_players,
        }

    @classmethod
    def deserialize(cls, data):
        num_players = data.get('num_players', len(data['players']))
        game = cls(num_players)
        game.players = [Player.deserialize(p) for p in data['players']]
        game.current_turn = data.get('current_turn', 0)
        game.messages = data.get('messages', [])
        game.last_move = data.get('last_move')
        return game
