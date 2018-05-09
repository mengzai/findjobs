//
//  hasPathSum.hpp
//  niuke
//
//  Created by Lili Wang on 11/7/16.
//  Copyright © 2016 Lili Wang. All rights reserved.
//

#ifndef hasPathSum_hpp
#define hasPathSum_hpp


#endif /* hasPathSum_hpp */
#include <stdio.h>

class hasPathSum

{
public:
    struct TreeNode {
        int val;
        TreeNode *left;
        TreeNode *right;
        TreeNode(int x) : val(x), left(NULL), right(NULL) {}
        };
    bool HasPathSum(TreeNode *root, int sum);
    void CreateTree(TreeNode* &root);
};

