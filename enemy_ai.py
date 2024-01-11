class EnemyAI:
    def __init__(self, player_position, enemy_position):
        # Initialize with player and enemy positions
        self.player_position = player_position
        self.enemy_position = enemy_position

    def update_positions(self, player_position, enemy_position):
        # Update positions each frame
        self.player_position = player_position
        self.enemy_position = enemy_position

    def calculate_movement(self):
        # Logic to move towards player while maintaining a distance
        # Include evasion logic and boundary checks

    def decide_attack(self):
        # Decide when to attack based on distance and line of sight

    def perform_evasion(self):
        # Implement evasion maneuvers

    def execute(self):
        # Main method to be called each frame
        # Combine movement, attack, and evasion logic
