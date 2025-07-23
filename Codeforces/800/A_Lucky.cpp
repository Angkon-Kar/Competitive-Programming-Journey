// Problem: A. Lucky?
// URL: https://codeforces.com/problemset/problem/1676/A
// Tag: Implementation

int main()
{

    int n;
    cin >> n;
    while (n--)
    {
        string s;
        cin >> s;

        if (s[0] + s[1] + s[2] == s[3] + s[4] + s[5])
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
}