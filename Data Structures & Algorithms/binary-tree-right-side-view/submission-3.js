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
     * @return {number[]}
     */
    rightSideView(root) {
        let res = [];
        let q = [];
        
        q.push(root);
        while(q.length>0){
            let qLen = q.length;
            let lastPop = null;
            for(let i=0;i<qLen;i++){
                let node = q.shift();
                if(node){lastPop = node;
                q.push(node.left);
                q.push(node.right);}
            }
            lastPop ? res.push(lastPop.val):'';
        }
        return res;
    }
}
