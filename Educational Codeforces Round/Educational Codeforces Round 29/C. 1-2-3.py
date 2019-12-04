
k, a, b = map(int, raw_input().split())
A = []
for i in range(3):
    A.append(map(int, raw_input().split()))
B = []
for i in range(3):
    B.append(map(int, raw_input().split()))

states = []
next_state = (a, b)
hit = {}

while next_state not in hit:
    hit[tuple(next_state)] = len(states)
    states.append(next_state)
    i, j = next_state
    next_state = (A[i-1][j-1], B[i-1][j-1])

tail = len(states)
head = hit[next_state]


def compute_point(states):
    point_a = point_b = 0
    for state in states:
        x, y = state
        if x == y:
            continue
        if (x, y) in [(3,2), (2,1), (1,3)]:
            point_a += 1
        else:
            point_b += 1
    return point_a, point_b
        
def compute(k, head, tail, states):
    if k < head:
        return compute_point(states[:k])
    a0, b0 = compute_point(states[:head])
    a1, b1 = compute_point(states[head:tail])
    a2, b2 = compute_point(states[head:head+(k - head) % (tail - head)])
    return (a0 + (k - head) / (tail - head) * a1 + a2,
            b0 + (k - head) / (tail - head) * b1 + b2)

pa, pb = compute(k, head, tail, states)
print pa, pb

