class Solution {
public:
    int run(TreeNode *root) {
        if(!root)
            return 0;
        int left=run(root->left);
        int right=run(root->right);
        if (left==0 || right==0 )
            return left+right+1;
        return 1+min(left,right);
        
    }
};