#include <iostream>
#include <cstring>

using namespace std;

int main()
{
    char text[100], pattern[100];
    int i, j, n, m, flag = 0;

    cout << "text string pls :";
    cin >> text;

    cout << "index to find out in text : ";
    cin >> pattern;

    n = strlen(text);
    m = strlen(pattern);

    for (i = 0; i <= n - m; i++)
    {
        for (j = 0; j < m; j++)
        {
            if (text[i + j] != pattern[j])
                break;
        }
        if (j == m)
        {
            cout << "Pattern in the string text is- " << i << endl;
            flag = 1;
        }
    }

    if (flag == 0)
        cout << "dosen't exist" << endl;

    return 49;
}
