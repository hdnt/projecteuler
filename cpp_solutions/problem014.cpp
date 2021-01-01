#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

const ll MAX_NUMBER = 5000000;
ll table[MAX_NUMBER + 1];
ll ans[MAX_NUMBER + 1];

void init();
void solve(ll);
void calc(ll);
ll next(ll);

int main()
{
    init();
    solve(MAX_NUMBER);

    ll most_terms_until = 1;
    for (ll n = 2; n <= MAX_NUMBER; ++n)
    {
        if (table[n] >= table[most_terms_until])
            most_terms_until = n;
        ans[n] = most_terms_until;
    }

    ll num_test_cases;
    cin >> num_test_cases;

    for  (ll _case = 0; _case < num_test_cases; ++_case)
    {
        ll target;
        cin >> target;

        cout << ans[target] << endl;
    }
}

void init()
{
    for (ll idx = 0; idx < MAX_NUMBER + 1; ++idx)
        table[idx] = -1;
    table[1] = 1;
}

void solve (ll target)
{
    for (ll n = 2; n <= target; ++n)
    {
        calc(n);
    }
}

void calc (ll n)
{
    vector <ll> termsList;

    while (n > MAX_NUMBER || table[n] == -1) // not in table
    {
        termsList.push_back(n);
        n = next(n); 
    }

    auto eit = termsList.end();
    for (auto it = termsList.cbegin(); it != eit; ++it)
    {
        if (*it <= MAX_NUMBER)
            table[*it] = (eit - it) + table[n];
    }
}
 ll next (ll n)
{
    if (n % 2 == 0)
        return n >> 1;
    return 3*n + 1;
}
