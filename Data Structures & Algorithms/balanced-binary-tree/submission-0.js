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
     * @return {boolean}
     */
    isBalanced(root) {
        let maxHeightDiff = 0;
        const dfs = (root)=>{
            if(root ===null) return 0;
            let leftHeight = dfs(root.left);
            let rightHeight = dfs(root.right);
            if(Math.abs(leftHeight-rightHeight) > 1) {
                maxHeightDiff = leftHeight - rightHeight;
            }
            return 1+Math.max(leftHeight,rightHeight);
        }
        dfs(root);
        return maxHeightDiff===0?true:false;
    }
}
