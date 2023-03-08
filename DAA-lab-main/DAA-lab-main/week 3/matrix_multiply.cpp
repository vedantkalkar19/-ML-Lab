#include <iostream>
using namespace std;

int main()
{
    int MAX_SIZE = 10;
    int A[MAX_SIZE][MAX_SIZE], B[MAX_SIZE][MAX_SIZE], C[MAX_SIZE][MAX_SIZE];
    int m, n, p, q, i, j, k;

    cout << "Enter the number of rows/columns of the 1st matrix: ";
    cin >> m >> n;

    cout << "Enter the elements of the 1st matrix: " << endl;
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < n; j++)
        {
            cin >> A[i][j];
        }
    }

    cout << "Enter the number of rows / columns of the 2nd matrix: ";
    cin >> p >> q;

    cout << "Enter the elements of the 2nd matrix: " << endl;
    for (i = 0; i < p; i++)
    {
        for (j = 0; j < q; j++)
        {
            cin >> B[i][j];
        }
    }

    if (n != p)
    {
        cout << "Error: Matrix multiply nahi hoga !!" << endl;
        return 0;
    }

    for (i = 0; i < m; i++)
    {
        for (j = 0; j < q; j++)
        {
            C[i][j] = 0;
            for (k = 0; k < n; k++)
            {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    cout << "the multiplication if the given matrix is  " << endl;
    for (i = 0; i < m; i++)
    {
        for (j = 0; j < q; j++)
        {
            cout << C[i][j] << " ";
        }
        cout << endl;
    }

    return 49;
}
