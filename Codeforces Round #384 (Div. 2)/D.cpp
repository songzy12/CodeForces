int a[maxn];
vector<int> g[maxn];

ll sum_subTree[maxn], mx_subTree[maxn];

void dfs1(int v, int p) {
    sum_subTree[v] = a[v];
    mx_subTree[v] = -llinf;
    for (int i = 0; i < g[v].size(); i++) {
        int to = g[v][i];
        if (to == p)
            continue;
        dfs1(to, v);
        sum_subTree[v] += sum_subTree[to];
        mx_subTree[v] = max(mx_subTree[v], mx_subTree[to]);
    }
    mx_subTree[v] = max(mx_subTree[v], sum_subTree[v]);
}

ll ans = -llinf;

void dfs2(int v, int p, ll out) {
    if (out != -llinf)
    ans = max(ans, sum_subTree[v] + out);

    vector<pair<ll, int> > miniset;
    for (int i = 0; i < g[v].size(); i++) {
        int to = g[v][i];
        if (to == p)
            continue;
        miniset.pb(mp(mx_subTree[to], to));
        sort(miniset.rbegin(), miniset.rend());
        if (miniset.size() == 3)
            miniset.pop_back();
    }
    miniset.pb(mp(-llinf, -1));
    for (int i = 0; i < g[v].size(); i++) {
        int to = g[v][i];
        if (to == p)
            continue;
        ll cur = miniset[0].s == to ? miniset[1].f : miniset[0].f;
        dfs2(to, v, max(out, cur));
    }
}

int main() {
    for (int i = 0; i + 1 < n; i++) {
        int u, v;
        read(u, v);
        u--, v--;
        g[u].pb(v);
        g[v].pb(u);
    }

    dfs1(0, -1);
    dfs2(0, -1, -llinf);
    cout << ((ans == -llinf) ? ("Impossible") : to_string(ans));
    return 0;
}

/*
Our task is to choose two disjoint subtrees, such that sum of numbers in the first plus the sum in the second is maximal.

Lets calculate for each vertex this dynamic programming using dfs seach: sumv ¡ª sum of all the numbers in subtree of vertex v, and mxv ¡ª maximal value from all sumk in subtree of vertex v (k belongs to subtree of v).

We can calculate the answer using another dfs search, maintaining the value of maximal subtree, which is outside of current subtree. For example, if we are in vertex v, to update this value when going to call dfs(s) (where s is some son of v) we have to find maximal mxv from all other sons of v.

The complexity is O(n). 
*/