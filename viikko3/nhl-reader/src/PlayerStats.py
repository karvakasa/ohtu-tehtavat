class PlayerStats:

    def __init__(self, PlayerStats):
        self.players = PlayerStats.get_players()

    def top_scorers_by_nationality(self, nationality):
        nationality_filtered_players = filter(
            lambda x: x.nationality == nationality, self.players
            )
        return sorted(
            nationality_filtered_players,
            key = lambda x: -(x.goals + x.assists)
            )