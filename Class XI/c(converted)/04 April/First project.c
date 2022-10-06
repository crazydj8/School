// practice: enter five numbers and find their average
#include <stdio.h>
int main(){
	int a, b, c, d, e, total;
	float average;
	printf("Enter first number:");
	scanf("%d", &a);
	printf("Enter second number:");
	scanf("%d", &b);
	printf("Enter third number:");
	scanf("%d", &c);
	printf("Enter fourth number:");
	scanf("%d", &d);
	printf("Enter fifth number:");
	scanf("%d", &e);
	total = a + b + c + d + e;
	average = total / 5;
	printf("Total =%d", total);
	printf("\nAverage =%f", average);
	return 0;
}