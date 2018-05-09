class Solution {
public:
    /**
     * @param root: The root of binary tree.
     * @return: An integer
     */
    int maxDepth(TreeNode *root) {
        // write your code here
        if(root == NULL)
           return 0;
        int leftDepth=maxDepth(root->left);
        int rightDepth=maxDepth(root->right);
        int ret=max(leftDepth,rightDepth)+1;
        return ret;
    }
};