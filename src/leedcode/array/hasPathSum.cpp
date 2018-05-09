//
//  hasPathSum.cpp
//  niuke
//
//  Created by Lili Wang on 11/7/16.
//  Copyright © 2016 Lili Wang. All rights reserved.
//

#include "hasPathSum.hpp"
#include <iostream>
using namespace std;
#include <stdio.h>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

bool hasPathSum::HasPathSum(TreeNode *root, int sum){
    
    if (!root) {
        return false;
    }
    if (root->left==NULL &&root->right==NULL && sum-root->val==0) {
        return true;
    }
    return HasPathSum(root->left,sum-root->val)||HasPathSum(root->right,sum - root->val);
}

void hasPathSum::CreateTree(TreeNode* &root)
{
   
    cout<<"input val"<<endl;
    int val;
    cin>>val;
    if(val == -1)
    {
        return ;
    }
    root->val = val;
    root->left = nullptr;
    root->right = nullptr;
    CreateTree(root->left);
    CreateTree(root->right);
}