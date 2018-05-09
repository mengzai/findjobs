/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int sumNumbers(TreeNode *root) {
        int sum=0;
        if (!root)
            return sum;
        return preordersumNumbers(root,sum);
    }
    int preordersumNumbers(TreeNode *root,int sum){
    if (!root)
        return 0;
    sum=sum*10+root->val;
    if (root->left==NULL &&root->right==NULL )
        return sum;
    return preordersumNumbers(root->left,sum)+preordersumNumbers(root->right,sum);
	}
};