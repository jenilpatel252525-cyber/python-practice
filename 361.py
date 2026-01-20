from collections import defaultdict

class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        n = len(votes[0])
        dp = defaultdict(lambda: [0] * n)

        # build DP
        for vote in votes:
            for i, team in enumerate(vote):
                dp[team][i] += 1

        # sort teams by DP vectors
        teams = list(dp.keys())
        teams.sort(key=lambda t: ([-x for x in dp[t]], t))

        return "".join(teams)
