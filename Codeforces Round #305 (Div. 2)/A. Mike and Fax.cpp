#include<iostream>

using namespace std;

bool isPalindrome(string s, int off, int len){
	int i = off;
	int j = off + len - 1;
	while (i<j){
		if(s[i]!=s[j])
			break;
		i++;
		j--;
	}
	return i>=j;
}

int main(){
	string s;
	int k;
	cin>>s>>k;
	if(s.size()%k != 0){
		cout<<"NO"<<endl;
		return 0;
	}
	int t = s.size()/k;
	int i;
	for(i=0; i<k; i++){
		if (!isPalindrome(s, i*t, t))
			break;
	}
	if(i!=k)
		cout<<"NO"<<endl;
	else
		cout<<"YES"<<endl;
	return 0;
}