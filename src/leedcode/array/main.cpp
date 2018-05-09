//
//  main.cpp
//  niuke
//
//  Created by Lili Wang on 11/7/16.
//  Copyright © 2016 Lili Wang. All rights reserved.
//

#include <iostream>
#include "hasPathSum.hpp"
#include "longestConsecutive.hpp"
#include <iostream>
#include <unordered_set>
#include <string>
#include <vector>
using namespace std;
const int Max=4;

//struct TreeNode {
//    int val;
//    TreeNode *left;
//    TreeNode *right;
//    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
//};

int main(int argc, const char * argv[]) {
//    int gof[Max];
//    cout<<"please enter your golf scores"<<endl;
//    cout<<"you must enter "<<Max<<" scores"<<endl;
//    for (int i=0;i<Max;i++)
//    {
//        cout<<"round #"<<i+1<<" : "<<endl;
//        while (!(cin>>gof[i])){
//            cin.clear();
//            while (cin.get()!='\n') {
//                continue;
//            }
//            cout<<"please enter a number"<<endl;
//            
//        }
//    }
    
    vector<int> vec;
    int numm=1;
    vec.push_back(1);
    vec.push_back(2);
    vec.push_back(100);
    vec.push_back(200);
    vec.push_back(3);
    vec.push_back(4);
    vec.push_back(5);
    vec.push_back(7);
    
    longestConsecutive longestConsecutive;
    longestConsecutive.LongestConsecutive(vec);
    return 0;
}
