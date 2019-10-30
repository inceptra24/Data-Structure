//implementation of TOH problem
#include<stdio.h>
void toh(int n, char from, char to, char aux){
	if(n==1){
		printf("move disc 1 from %c to %c\n",from,to);
		return;
	}	
	
		toh(n-1,from,aux,to);
		printf("move %d from %c to %c\n",n,from,to);
		toh(n-1,aux,to,from);
}
int main(void){
	printf("Enter num of discs : ");
	int n;
	scanf("%d",&n);
	toh(n,'a','b','c');
}
