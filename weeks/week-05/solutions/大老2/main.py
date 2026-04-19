"""Main entry point for Big Two game"""

from game.ui.app import BigTwoApp


def main():
    """Run the game"""
    # Create app with mixed human/AI players
    player_names = ['Player1', 'AI_1', 'AI_2', 'AI_3']
    app = BigTwoApp(player_names)
    app.run()


if __name__ == '__main__':
    main()
