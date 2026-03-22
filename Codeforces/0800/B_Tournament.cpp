// Problem: B. Tournament
// URL: https://codeforces.com/contest/2123/problem/B
// Tag: Greedy

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
 
void solve() {
    int n, j_idx, k;
    std::cin >> n >> j_idx >> k;
    --j_idx; // Adjust to 0-based indexing
 
    std::vector<int> a(n);
    int max_strength = 0;
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
        if (a[i] > max_strength) {
            max_strength = a[i];
        }
    }
 
    // Case 1: Player j has the maximum strength.
    // If player j's strength is the highest, they can always win against strictly weaker players.
    // Against players of equal strength, the problem implies we can assume player j wins ("might defeat").
    // Therefore, player j can never be eliminated by a stronger player and can always defeat or get lucky against equal-strength players.
    // This means player j can always ensure their survival until they are among the last k players.
    if (a[j_idx] == max_strength) {
        std::cout << "YES\n";
        return;
    }
 
    // Case 2: Player j does not have the maximum strength.
    // This means there is at least one player stronger than player j.
    // Player j can be eliminated if chosen against any player strictly stronger than them.
    // To be among the last k players, player j needs to survive $n-k$ eliminations.
    // Consider the most favorable scenario for player j:
    // 1. Player j always wins against players with strength less than or equal to a[j_idx].
    //    This means player j can effectively "eliminate" all players with strength less than or equal to a[j_idx] (except themselves).
    // 2. Players strictly stronger than player j eliminate each other or other weaker players (not player j).
    // In the most favorable scenario, all players with strength <= a[j_idx] (except j) are eliminated by j or by stronger players.
    // This reduces the player pool to player j and all players with strength > a[j_idx].
    // If player j is to be among the last k players, and there is at least one player stronger than j,
    // then j cannot be the sole survivor (k=1), because the stronger player would eliminate j if they were the last two.
    // However, if k >= 2, then player j and at least one stronger player can both survive.
    // The 'stronger' players can eliminate each other until only one of them remains (the strongest).
    // If k >= 2, then player j and this one strongest player can both be among the last k players.
    // Example: Initial players A(5), B(3), C(2). j=C(2). k=2.
    // A(5) vs B(3) -> A(5) wins. B(3) eliminated. Remaining: A(5), C(2).
    // k=2, and C(2) is among A(5), C(2). So YES.
    // This relies on the "any way" interpretation: we can assume matches are chosen (or randomly result in) the most favorable outcomes for player j.
    // Specifically, if there are at least two players remaining, a match can be chosen such that player j isn't immediately eliminated by a stronger player.
    // As long as there are at least 2 players in the final k spots, player j could potentially take one of them, provided all players stronger than j play against each other until at most one of them remains. This uses (count_stronger - 1) eliminations.
    // The players weaker than j can be eliminated by j or by stronger players.
    // If k=1 and a[j_idx] is not the max, then player j cannot be the unique survivor. There is always a player strictly stronger than j who would eliminate j if they faced each other in the final match.
    // If k >= 2, it is always possible.
    if (k >= 2) {
        std::cout << "YES\n";
    } else { // k == 1
        std::cout << "NO\n";
    }
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int t;
    std::cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}