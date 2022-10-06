// read the radius and calculate the area and circumference for circle
#include <stdio.h>
int main(){
	int r;
	float a, c;
	printf("Enter the radius of circle in cm:");
	scanf("%d", &r);
	printf("Circumference is: %f", 2 * 3.14 * r);
	printf("\nArea is: %f", 3.14 * r * r);
	return 0;
}