#include <stdio.h>
#include <math.h>

long double _eval(long double r)
	{
		int i;
		long double sum=0;
		for(i=1;i<=5000;i++)
		 sum+=(long double)(900.0-3.0*i)*pow(r,(long double)(i-1));
		//printf("r= %.12llf ",r);
		//printf("sum= %.12llf\n",sum);
		return sum;
	}

int main()
	{
		long double lo=1.001999000000,hi=1.002999000000;

		int cnt=0;
		while(cnt++<100)
		{
			long double mid=(lo+hi)*0.5;
			if(_eval(mid)<(-600000000000.0))hi=mid;
			else lo=mid;
		}
		printf("%0.12Lf\n",lo);
	}

