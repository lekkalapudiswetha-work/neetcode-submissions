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
     * @return {number[][]}
     */
    levelOrder(root) {
        let res = [];
        let q =[];
        if(root){
            q.push(root);
            while(q.length>0){
                let currLevel = [];
                let qLen = q.length;
                for(let i =0;i<qLen;i++){
                    let node = q.shift();
                    if(node){
                        currLevel.push(node.val);
                        q.push(node.left);
                        q.push(node.right);
                    }
                }
                currLevel.length ?res.push(currLevel):'';
            }
        }
        return res;
    }
}
