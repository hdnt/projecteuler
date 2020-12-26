#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

const int MAX_NUMBER = 5000000;
unordered_map<int, int> table;
unordered_map<int, int> ans;

void solve(int);
void calc(int);
int next(int);

int main()
{
    table.reserve(MAX_NUMBER);
    table[1] = ans[1] = 1;
    ans.reserve(MAX_NUMBER);
    solve(MAX_NUMBER);

    int most_terms_until = 1;
    for (int n = 2; n <= MAX_NUMBER; ++n)
    {
        if (table[n] >= table[most_terms_until])
            most_terms_until = n;
        ans[n] = most_terms_until;
    }

    int num_test_cases;
    cin >> num_test_cases;

    for (int _case = 0; _case < num_test_cases; ++_case)
    {
        int target;
        cin >> target;

        cout << ans[target] << endl;
    }
}

void solve(int target)
{
    for (int n = 2; n <= target; ++n)
    {
        calc(n);
    }
}

void calc(int n)
{
    vector<int> termsList;

    while (table.find(n) == table.end()) // not in table
    {
        termsList.push_back(n);
        n = next(n); 
    }

    auto eit = termsList.end();
    for (auto it = termsList.cbegin(); it != eit; ++it)
    {
        table[*it] = (eit - it) + table[n];
    }
}

int next(int n)
{
    if (n % 2 == 0)
        return n >> 1;
    return 3*n + 1;
}
