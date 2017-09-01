# -*- coding: utf-8 -*-

# 'good' subset exists iff 
# - 1 values among d_i can be changed to 0 / 1 so that \sum d_i is even

# if sum can only be odd, there is no solution obviously
# else find any spanning tree, and decide for each edge from leaves to root
