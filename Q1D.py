MOD = 10**9

def amoeba_divisions(N):
    dp = {}
    dp[(0, 0, 0)] = 1
    
    for _ in range(N):
        new_dp = {}
        for (x, y, z), count in dp.items():
            for dx, dy, dz in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
                new_pos = (x + dx, y + dy, z + dz)
                if new_pos not in new_dp:
                    new_dp[new_pos] = 0
                new_dp[new_pos] = (new_dp[new_pos] + count) % MOD
        dp = new_dp
    
    return sum(dp.values()) % MOD

# Example usage
N = 10000
result = amoeba_divisions(N)
print(f"The last nine digits of D({N}) are: {result}")
