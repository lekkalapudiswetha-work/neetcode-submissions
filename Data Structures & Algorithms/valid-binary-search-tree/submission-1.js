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
    isValidBST(root) {
        const isBST = (root,min,max)=>{
            if(!root) return true;
            if(root.val > min && root.val < max){
                return (isBST(root.left,min,root.val) && isBST(root.right,root.val,max));
            }else{
                return false;
            }
        }
        return isBST(root, -Infinity , Infinity);

    }
}
