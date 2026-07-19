/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    diameterOfBinaryTree(root) {
       let max = 0;
       const dfs = (root) => {
        if(root===null) return 0;
        let leftHeight = dfs(root.left);
        let rightHeight = dfs(root.right);
        max = Math.max(max , leftHeight+rightHeight);
        return 1+Math.max(leftHeight,rightHeight); 
       }
       dfs(root);
       return max;
    }

    // dfs(root,val){
    //     if(root === null) return 0;
    //     let leftHeight = this.dfs(root.left,val);
    //     let rightHeight = this.dfs(root.right,val);
    //     val[0] = Math.max(val[0] , leftHeight+rightHeight);
    //     return 1 + Math.max(leftHeight,rightHeight);
    // }

}
