class Solution {
    /**
     * @param {character[][]} board
     * @param {string[]} words
     * @return {string[]}
     */
    findWords(board, words) {
        /**
         * first create trie for all the words present in words array
         * now do dfs for each element in grid 
         * compare with the trie and see if the words exists in trie is formed.
         * how to compare :
         * DFS(r,c,node,word):
         *   start at root:
         *       if grid[i][j] is in root.children && r and c are in bounds and grid[i][j] is not visited
         *            mark visites[i][j]
         *            add letter to work 
         *            node <- node.children[grid[i][j]];
         *            check if(its the end of the word) add to result;
         * 
         *            before calling dfs of other adjacensies we can check if node.children is not null.
         *            if true 
         *             remove visited (i,j);
         *             we can return;
         *            
         */
         
         
         const DFS = (i,j,node,word)=>{
           if(i < 0 || i >= rows || j < 0 || j >= cols || visited.has(i +','+ j) || !node.children[board[i][j]]){
             return;
           }
           visited.add(i +',' +j);
           word+=board[i][j];
           node = node.children[board[i][j]];
           if(node.isWord){
             result.add(word);
           }
           
             DFS(i+1,j,node,word);
             DFS(i-1,j,node,word);
             DFS(i,j+1,node,word);
             DFS(i,j-1,node,word);
           
             visited.delete(i + ',' + j);
             
           
           
           
         }
         
         let visited = new Set();
         let result = new Set();
         let root = new TrieNode();
         
         let rows = board.length;
         let cols = board[0].length;
         
         for(const word of words){
           root.insert(word);
         }
         
         console.log(root.children);
         
         
         for(let i = 0;i<rows;i++){
           for(let j = 0;j<cols;j++){
              DFS(i,j,root,'');
           }
         }
         
         return Array.from(result);
         
         
         
         
         
    }
}


class TrieNode{
  constructor(){
    this.children = {};
    this.isWord = false;
  }
  
  
  insert(word){
    let curr = this;
    for(let char of word){
      if(!curr.children[char]){
         curr.children[char] = new TrieNode();
      }
      curr = curr.children[char]
    }
    curr.isWord = true;
    
  }
}