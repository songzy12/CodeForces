// p[l][r] is the maximum k such that the substring built from characters from l to r is k-palindrome.
// if s[l] ≠ s[r] or dp[l + 1][r - 1] = 0, dp[l][r] = 0. 
// Otherwise dp[l][r] = dp[l][m] + 1, where .