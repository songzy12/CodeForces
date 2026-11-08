## Greedy

Greedy algorithms build a solution through a sequence of locally best choices.
The categories below group common patterns; a locally best choice is not
automatically correct for every problem.

### Selection and exchange

- **Activity selection / interval scheduling** — sort by finishing time and
  repeatedly take the compatible activity that finishes earliest. Maximizes the
  number of non-overlapping activities.
- **Fractional knapsack** — sort by value-to-weight ratio and take the best
  remaining fraction first. This is optimal when items can be split; it does
  not solve 0/1 knapsack.
- **Matroid greedy** — consider elements in weight order and add one whenever
  independence is preserved. Finds a maximum-weight independent set for a
  matroid, and explains why greedy works for problems such as minimum spanning
  trees.

### Scheduling and resource allocation

- **Interval partitioning** — process intervals by start time and reuse a
  resource whose current interval ends earliest; otherwise open a new resource.
  The resulting number of resources is minimal.
- **Earliest deadline first (minimum maximum lateness)** — schedule jobs in
  nondecreasing deadline order. Minimizes the maximum lateness when jobs are
  available at the start and run on one machine.
- **Job sequencing with deadlines** — for unit-time jobs with deadlines and
  profits, consider jobs by decreasing profit and place each in the latest
  available slot before its deadline.

### Graph algorithms

- **Kruskal's minimum spanning tree** — scan edges by increasing weight and add
  an edge only when it joins two different components (usually with
  union-find).
- **Prim's minimum spanning tree** — grow one tree by repeatedly adding its
  cheapest edge to a vertex outside the tree.
- **Dijkstra's shortest paths** — repeatedly settle the unsettled vertex with
  the smallest tentative distance and relax its outgoing edges. Requires
  nonnegative edge weights.

### Merging and coding

- **Huffman coding** — repeatedly combine the two least-frequent symbols or
  subtrees. Produces an optimal prefix code for the given symbol frequencies.
- **Optimal merge pattern** — repeatedly merge the two smallest files or
  sequences. Minimizes total merge cost when merging two objects costs their
  combined size.

### Approximation and problem-specific greedy rules

- **Greedy set cover** — repeatedly choose the set covering the most uncovered
  elements (or the best coverage-to-cost ratio). This is an approximation
  algorithm, not generally an exact solution.
- **Coin change** — repeatedly take the largest coin not exceeding the
  remainder. This is optimal for some coin systems, but not for arbitrary
  denominations.

### References

1. https://en.wikipedia.org/wiki/Greedy_algorithm
2. https://www.geeksforgeeks.org/dsa/greedy-algorithms/
3. https://lovaeye.com/blogs/greedy
