// calculate area and perimeter of rectangle
#include <stdio.h>
int main(){
	int l, b, a, p;
	
	printf("Enter the length of the rectangle in cm: ");
	scanf("%d", &l);
	printf("Enter the breadth of the rectangle in cm: ");
	scanf("%d", &b);
	
	p = 2 * (l + b);
	a = l * b;
	
	printf("Perimeter = %d", p);
	printf("Area = %d", a);
	return 0;
}