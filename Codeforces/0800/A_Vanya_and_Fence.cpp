// Problem: A. Vanya and Fence
// URL: https://codeforces.com/problemset/problem/677/A
// Tag: Implementation

#include <iostream>
using namespace std;
typedef long long ll;
ll i,n,h,ans,x;
int main()
{
	cin >> n >> h;
	ans = n;
	for (i = 0; i < n; i++)
	{
		cin >> x;
		ans += (x>h);
	}
	cout << ans << endl;
	return 0;
}

/*
    Explanation:
    We read the number of friends n and the height of the fence h. We initialize the answer ans to n, because each friend will take at least 1 unit of width on the road.

    Then we loop through each friend's height x. If a friend's height is greater than h, it means they need to bend down to pass under the fence, which takes an additional unit of width. Therefore, we increment ans by 1 for each friend whose height exceeds h.

    Finally, we output the total width ans needed for all friends to pass the fence.
*/