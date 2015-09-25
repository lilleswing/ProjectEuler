#include <stdio.h>
int main() {
	long long n = 600851475143;
	long long k = 2;
	while(n % k == 0) {
		n = n / k;	
	}
	k++;
	while(n != 1) {
		while(n % k == 0) {
			n = n /k;
		}
		k += 2;
	}
	printf("%lld\n",k-2);
	return 0;
}
