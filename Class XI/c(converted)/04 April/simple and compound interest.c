// calculate simple and compound interest
#include <stdio.h>
#include <math.h>
int main(){
	int p, t;
	float r;
	double ci, si;
	
	printf("Enter the principal amount:");
	scanf("%d", &p);
	printf("Enter the rate of interest:");
	scanf("%f", &r);
	printf("Enter the time(in years):");
	scanf("%d", &t);
	
	si = (p * r * t) / 100;
	ci = p * pow(1 + r /100, t);
	
	printf("Simple Interest= %lf", si);
	printf("Compund Interest= %lf", ci);
	return 0;
}
	