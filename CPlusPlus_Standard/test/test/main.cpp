//
//  main.cpp
//  test
//
//  Created by 王煜 on 2022/6/28.
//

#include<vector>
#include<iostream>
#include<stdio.h>
using namespace std;
int main() {
 //freopen("data.in.cpp","r",stdin);
 int n,m,map;
 while(cin>>n>>m) {
  vector<int>a(2*n);
  a.clear();
  map=m-1;
  a[map]=1;
  for(int i=1; i<n; i++) {
   int j=0;
   while(j!=m) {
    map++;
    if(map>2*n-1)
     map=map%(2*n);
    if(a[map]==0)
     j++;
   }
   a[map]=1;
  }
  for(int i=0; i<2*n; i++) {
//   if(!(i%50)&&i==i) cout<<endl;
   if(a[i]==1)
    cout<<'B';
   else
    cout<<'G';
  }
 }
 return 0;
}
