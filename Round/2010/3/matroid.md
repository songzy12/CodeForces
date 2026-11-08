## Greedy Algorithms and Matroids

Greedy algorithms build a solution through a sequence of locally best choices. At each step, the algorithm selects an available option according to a ranking or rule, then keeps it if doing so preserves feasibility.

Greedy is attractive because it is often simple and efficient, but a locally optimal choice does not automatically lead to a globally optimal solution. The key is to identify a property of the problem that justifies the choices.

### 1. Matroids

A **matroid** is a pair $M = (E, \mathcal{I})$, where $E$ is a finite ground set and $\mathcal{I}$ is a collection of subsets of $E$, called the independent sets. The collection must satisfy:

1. **Non-emptiness:** $\emptyset \in \mathcal{I}$.
2. **Hereditary property:** If $A \in \mathcal{I}$ and $B \subseteq A$, then $B \in \mathcal{I}$.
3. **Exchange property:** If $A, B \in \mathcal{I}$ and $|A| < |B|$, then some element $x \in B \setminus A$ can be added to $A$ while keeping it independent: $A \cup \{x\} \in \mathcal{I}$.

The exchange property is what distinguishes matroids from arbitrary hereditary feasibility systems. It says, in effect, that a smaller independent solution can always be extended using an element from a larger one.

An independent set that cannot be extended by adding another element is called a **basis**. The exchange property implies that all bases of a matroid have the same size, called its rank.

### 2. The Greedy Theorem

Assign each element $e \in E$ a weight $w(e)$. The weighted matroid greedy algorithm sorts elements by decreasing weight and scans them in that order, adding an element whenever the enlarged set remains independent. It returns a maximum-weight basis. Equivalently, if only a maximum-weight independent set is required, negative-weight elements can be skipped.

For minimum-weight bases, sort by increasing weight instead.

The **Rado–Edmonds theorem** characterizes this behavior: a finite independence system is a matroid if and only if the greedy algorithm finds an optimal basis for every assignment of element weights.

This theorem does not say that every problem that can be solved greedily is a matroid problem. Nor does it justify an arbitrary greedy rule. The guarantee applies when the feasible sets satisfy the matroid axioms and the algorithm uses the appropriate weight order.

### 3. Examples

These are classical examples of matroids: graphic, uniform, and partition matroids are among the standard basic classes, while laminar matroids generalize nested and disjoint capacity constraints. Each example has a rule that says which selections are allowed (the independent sets) and an objective that says which allowed selection is best (the weights).

#### [Graphic matroid](https://en.wikipedia.org/wiki/Graphic_matroid)

**Problem:** Given a connected graph whose edges have costs, choose edges that connect every vertex with minimum total cost. This is the [minimum spanning tree problem](https://en.wikipedia.org/wiki/Minimum_spanning_tree).

Let the vertices be $A,B,C,D$, with edges

| Edge | Weight |
| --- | ---: |
| $AB$ | 1 |
| $BC$ | 2 |
| $AC$ | 3 |
| $CD$ | 4 |
| $BD$ | 5 |

The ground set is the set of edges, and a set is independent if it contains no cycle. For example, $\{AB, BC, CD\}$ is independent, while $\{AB, BC, AC\}$ is dependent because those three edges form a cycle.

To find a minimum spanning tree, process edges in increasing weight order and add an edge only when it does not create a cycle. Kruskal's algorithm first adds $AB$ and $BC$, rejects $AC$, then adds $CD$. The resulting spanning tree has total weight $1+2+4=7$.

#### [Uniform matroid](https://en.wikipedia.org/wiki/Uniform_matroid)

**Problem:** From a collection of items, choose at most two items to maximize the total value.

Suppose $E=\{a,b,c,d\}$ and at most two elements may be chosen. The independent sets are exactly the subsets of size at most $2$. If the weights are $w(a)=9$, $w(b)=7$, $w(c)=5$, and $w(d)=1$, the best choice is $\{a,b\}$, with total weight $16$.

In general, a **uniform matroid** of rank $r$ allows any subset of at most $r$ elements. Greedy therefore selects the $r$ highest-weight elements when constructing a maximum-weight basis (or skips negative-weight elements when seeking a maximum-weight independent set of any size).

#### [Partition matroid](https://en.wikipedia.org/wiki/Partition_matroid)

**Problem:** Choose candidates with the highest total score, subject to category limits: at most one red candidate and at most two blue candidates.

Suppose candidates are split into two categories:

* Red: $r_1$ with weight $8$, and $r_2$ with weight $6$; choose at most one red candidate.
* Blue: $b_1$ with weight $9$, $b_2$ with weight $7$, and $b_3$ with weight $5$; choose at most two blue candidates.

A set is independent if it respects both category limits. Processing candidates by decreasing weight selects $b_1$, $r_1$, and $b_2$, for total weight $24$. The remaining candidates are rejected: $r_2$ because the red capacity is full, and $b_3$ because the blue capacity is full.

More generally, partition the ground set into disjoint groups $E_1,\ldots,E_m$, with capacity $c_j$ for group $E_j$. A set is independent when it contains at most $c_j$ elements from each group. This models selection with separate per-category limits.

#### Laminar matroid

**Problem:** Choose elements with the highest total value while respecting several nested or disjoint group limits.

A family of subsets is **laminar** if any two sets in it are disjoint or one contains the other. A laminar matroid is a standard matroid class; see the [Wikipedia overview of matroid theory](https://en.wikipedia.org/wiki/Matroid_theory) for general background. Consider

$$E=\{a,b,c,d,e,f\}, \qquad X=\{a,b,c,d\}, \qquad Y=\{a,b\}, \qquad Z=\{e,f\}.$$

Impose these upper bounds:

* At most $3$ elements from $E$.
* At most $2$ elements from $X$.
* At most $1$ element from each of $Y$ and $Z$.

The sets $Y$ and $Z$ are disjoint, and both are contained in $E$; $Y$ is also contained in $X$. Thus the constrained subsets are laminar. For weights $w(a)=10$, $w(b)=9$, $w(c)=8$, $w(d)=7$, $w(e)=6$, and $w(f)=5$, greedy processes elements in that order. It selects $a$, skips $b$ because $Y$ already has one element, selects $c$, skips $d$ because $X$ is full, then selects $e$. It rejects $f$ because the total capacity of $E$ is full. The result $\{a,c,e\}$ satisfies every capacity and has total weight $24$.

In general, given a laminar family and an upper capacity for each member, the sets that respect all those capacities form a matroid. Nested prefix limits are one example of laminar constraints, though a particular optimization problem may include additional conditions that need separate analysis.

### 4. A Practical Checklist

When considering a greedy solution:

1. **Define the choices.** What are the ground-set elements, and what does selecting a subset mean?
2. **Define feasibility.** Which subsets are allowed? Check whether feasibility is hereditary.
3. **Check exchange.** For any two feasible sets of different sizes, can an element from the larger set be added to the smaller one?
4. **Justify the order.** For a matroid, process elements by weight (descending for maximum weight, ascending for minimum weight).
5. **Use an independence test.** Add an element only if the enlarged set remains feasible.

If these conditions hold, the matroid greedy theorem provides a strong optimality guarantee. If they do not, greedy may still work, but it needs a different proof—for example, an exchange argument tailored to the problem—or a counterexample may show that the rule is not optimal.

### 5. Matroids and Other Greedy Patterns

Some greedy algorithms process items in chronological order, maintain a priority queue, and revise earlier choices when a constraint is exceeded. These are often described informally as **regret greedy** or **lazy greedy**. Such a method is not automatically the weighted matroid greedy algorithm: its correctness depends on the specific problem and should be established separately.

Likewise, prefix constraints alone do not guarantee that a problem is a matroid, and a priority queue is only an implementation tool—it does not prove optimality. First model the feasible sets and identify the relevant exchange or structural property; then choose the data structure that makes the algorithm efficient.

### References

1. [Matroid theory — Wikipedia](https://en.wikipedia.org/wiki/Matroid_theory)
2. [Graphic matroid — Wikipedia](https://en.wikipedia.org/wiki/Graphic_matroid)
3. [Minimum spanning tree — Wikipedia](https://en.wikipedia.org/wiki/Minimum_spanning_tree)
4. [Uniform matroid — Wikipedia](https://en.wikipedia.org/wiki/Uniform_matroid)
5. [Partition matroid — Wikipedia](https://en.wikipedia.org/wiki/Partition_matroid)
6. [Introduction to Algorithms: Lecture 17 slides, Johns Hopkins University](https://www.cs.jhu.edu/~mdinitz/classes/IntroAlgorithms/Fall2021/Lectures/Lecture17/lecture17slides.pdf)
