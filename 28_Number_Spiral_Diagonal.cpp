#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    long long int t,i,n;
    cin>>t;
    for(i=1;i<=t;i++){
        long long int z1,z2,z3,z4,z5,z6,t1,t2,t3,x,j,s = 1;
        long long int mod = pow(10,9) + 7;
        cin>>n;
        x = n/2;
        if((x+1)%3 == 0){
            z1 = (x+1)/3;
            z2 = 8*x;
            z3 = 2*x+1;
        }
        else if(x%3 == 0){
            z1 = (x/3)*8;
            z2 = x+1;
            z3 = 2*x + 1;
        }
        else{
            z1 = (2*x+1)/3;
            z2 = 8*x;
            z3 = x+1;
        }
            t1 = ((((z1%mod)*(z2%mod))%mod) * z3%mod)%mod;
  
        t2 = 4*x + 1;
        t3 = (((2*x)%mod) * (x+1)%mod)%mod;
        cout<<((t1 + t2%mod)%mod + t3)%mod<<endl;
    }
    return 0;
}
