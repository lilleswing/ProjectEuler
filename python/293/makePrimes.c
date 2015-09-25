#include <stdio.h>
#include <string.h>
int main() {
	int lim = 1, i,j,k;
	for(i=0;i<9;i++){
		lim *=10;
	}
	char sieve[1000000000];
	memset(sieve,0,sizeof(sieve));
	printf("sieve allocated\n");
	for(i=2;i<lim;i++){
		k = 2;
		while(i*k < lim){
			sieve[i*k] = 1;
			k++;
		}
	}
	for(i=2;i<lim;i++){
		if(sieve[i]==0) {
			printf("%d\n",i);
		}
	}
	return 0;
}
