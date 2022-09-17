# if A*B is perfect square and B*C is perfect square
# then A*C is perfect square

# https://discuss.codechef.com/questions/8577/amballs-editorial

# DP[x][y] := The number of ways of inserting balls of the first 'x' colors in such a way that there are exactly 'y' bad spaces.

# Filling in values of DP[x][y] from values DP[x-1][y]
# for(int ij = 0; ij <= C[x]; ij++)   //ij = i+j as described
#     for(int y = 0; y <= spaces[x-1]; y++)
#         if(DP[x-1][y] > 0)
#             for(int j = 0; j <= min(ij, y); j++)
#                 i = ij-j;
#                 z = spaces[x-1] - b;
#                 DP[x][(y-j) + (C[x]-ij)] += DP[x-1][y] * Comb[y][j] * Comb[z][i] * Comb[C[x]-1][ij-1]; 
# (Remember to calculate Modulo 1E9 + 7)
