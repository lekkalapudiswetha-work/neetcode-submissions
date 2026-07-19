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
     * @param {TreeNode} subRoot
     * @return {boolean}
     * 
     * 
     * 
     */
    isSubtree(root, subRoot) {

        /**
         * base Case : if(root === subroot) 
         */
        const isSame=(root, subRoot)=>{
        if(!root && !subRoot) return true;
        if(root && subRoot && root.val === subRoot.val){
            return (isSame(root.left,subRoot.left) && isSame(root.right,subRoot.right))
        }
        return false;
        }
        if(!subRoot) return true;
        if(!root) return false;
        if(isSame(root,subRoot)) {
            return true;
        }
        return (this.isSubtree(root.left,subRoot) || this.isSubtree(root.right,subRoot));
    }
}
