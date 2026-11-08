# Least Cost Bracket Sequence

https://codeforces.com/contest/3/problem/D

## Problem Statement

You are given a string of parentheses and question marks. For each question mark, you are given the cost of replacing it with `'('` and the cost of replacing it with `')'`. Replace every question mark so that the resulting string is a regular bracket sequence, minimizing the total replacement cost. A regular bracket sequence has no prefix with more closing than opening parentheses, and has equal numbers of opening and closing parentheses overall. If no valid sequence can be formed, report that it is impossible.

## Greedy Solution

Initially replace every `?` with `')'`. Add its closing-parenthesis cost to the answer, and store the cost difference `cost('(') - cost(')')` in a min-heap along with its position. This difference is the extra cost of changing that question mark from `')'` to `'('`.

Scan the string from left to right while tracking the current bracket balance (`'('` adds one and `')'` subtracts one). Whenever the balance becomes negative, the current prefix is invalid. Fix it by taking the question mark with the smallest cost difference seen so far, changing it to `'('`, adding that difference to the answer, and increasing the balance by two. If the heap is empty, no assignment can make this prefix valid.

After scanning all characters, the balance must be zero. If it is not, no valid bracket sequence can be formed; otherwise, the accumulated cost and the chosen replacements give an optimal answer. The heap ensures each required opening parenthesis is assigned at the lowest possible incremental cost, while repairing a prefix also improves every later prefix. The running time is $O(n \log n)$ and the space usage is $O(n)$.

## Proof of Correctness

To prove that this "regret greedy" (also known as lazy greedy / matroids with prefix constraints) produces an optimal solution, we can use an **exchange argument**.

### 1. Formal Formulation

Let the string have length $n$. For any character at index $i$:

* Let $x_i = +1$ if the final character is `'('`, and $x_i = -1$ if it is `')'`.
* Fixed characters have their $x_i$ predetermined.
* For each question mark $i \in Q$, we must choose $x_i \in \{+1, -1\}$.

A sequence is valid if and only if:

1. **Prefix Condition:** For all $1 \le k \le n$, the prefix sum $P_k = \sum_{i=1}^k x_i \ge 0$.
2. **Total Balance:** $P_n = 0$.

If we initially set all $i \in Q$ to $x_i = -1$, the baseline cost is $\sum_{i \in Q} b_i$. Converting index $i$ to `'('` ($x_i = +1$) increases the prefix sums $P_k$ (for all $k \ge i$) by $+2$, and incurs an additional cost of:


$$d_i = a_i - b_i$$

Thus, the problem is equivalent to:

> Select a subset $S \subseteq Q$ of indices to flip to `'('` such that the resulting prefix sums satisfy $P_k \ge 0$ for all $k$, and $P_n = 0$, minimizing:
> 
> $$\sum_{i \in S} d_i$$


### 2. The Nature of the Constraints

Notice two critical properties:

1. **Necessity of Flips:** Since each step changes $P_k$ by $\pm 1$, the first time $P_k$ drops below $0$, it will be exactly $P_k = -1$. To make the sequence valid, **at least one** element from $Q \cap \{1, \dots, k\}$ must be chosen into $S$ to boost all subsequent balances by $+2$.
2. **Monotonicity of Benefits:** Choosing an element $i \in S$ raises $P_t$ by $+2$ for all $t \ge i$. It never decreases any prefix balance.

### 3. The Exchange Argument

Consider any valid solution $S^*$. We show inductively that it can be transformed, without increasing its cost or losing validity, to include every index chosen by the greedy algorithm.

Suppose the greedy algorithm has already chosen the same indices as $S^*$ at its earlier repair steps. At a repair step, let $k$ be the current position where the balance becomes $-1$, and let $g$ be the question mark with the smallest difference $d$ among all question marks seen so far that have not already been chosen. If $g \in S^*$, no change is needed. Otherwise, since $S^*$ is valid at prefix $k$ and includes all earlier greedy choices, it must contain some additional unchosen question mark $u \le k$. Choose any such $u$. Both $u$ and $g$ are available to the greedy choice, so $d_g \le d_u$.

Replace $u$ by $g$ in $S^*$. We check the two required properties of this exchange separately.

1. **The objective value does not increase.** The cost changes by $d_g-d_u$. Since the greedy choice has minimum difference among the available question marks, $d_g \le d_u$, so $d_g-d_u \le 0$.
2. **The solution remains valid.** Prefix balances before both indices and after both indices are unchanged, because either neither flip or both flips contribute to those prefixes. Between the two indices:
   * If $g < u$, moving the flip earlier increases the balance by $2$, so those prefixes remain valid.
   * If $u < g$, moving the flip later decreases the balance by $2$. For any affected prefix $t$ (where $u \le t < g$), we have $t < k$. The greedy balance at $t$, after the earlier repair choices and before this repair at $k$, is nonnegative. The exchanged solution's balance at $t$ is that greedy balance plus contributions from any other flips in $S^*$ not among those earlier greedy choices; each such contribution is either $0$ or $2$. Thus its balance at $t$ is also nonnegative.

The replacement therefore preserves validity and makes the solution include one more greedy choice. Repeating this argument shows that some optimal solution includes every index chosen by the greedy algorithm.

### 4. Conclusion

Let $q$ be the number of question marks, and let $F$ be the sum of the fixed characters, using $+1$ for each fixed `'('` and $-1$ for each fixed `')'`. Any solution with total balance zero must flip exactly $\frac{q-F}{2}$ question marks, since its total balance is $F-q+2|S|$. The greedy solution also has total balance zero, so it has this same number of flips. Since an optimal solution can be transformed to include every greedy flip, and both solutions have the same number of flips, their sets of flips are equal.

Therefore:


$$\sum_{i \in S_{\text{greedy}}} d_i \le \sum_{j \in S^*} d_j$$


proving that the greedy choice is globally optimal.
