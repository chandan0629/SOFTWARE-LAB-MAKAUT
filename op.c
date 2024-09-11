#include <stdio.h>

int main() {
    int s, r, c, x, op, reuse;

    printf("Enter no. of screens: ");
    scanf("%d", &s);

    printf("Enter no. of reports: ");
    scanf("%d", &r);

    printf("Enter no. of components: ");
    scanf("%d", &c);

    printf("Enter 1 for simple, 2 for medium and 3 for High: ");
    scanf("%d", &x);

    if (x == 1) {
        op = s * 1 + r * 2 + c * 10;
    } else if (x == 2) {
        op = s * 2 + r * 5 + c * 10;
    } else if (x == 3) {
        op = s * 3 + r * 8 + c * 10;
    }

    printf("Enter reusability: ");
    scanf("%d", &reuse);

    int nop = op * (100 - reuse) / 100;

    printf("Object point: %d\n", op);
    printf("New object point: %d\n", nop);

    return 0;
}
