class TrieNode{
    constructor(){
        this.children = {};
        this.word = false;
    }
}

class WordDictionary {
    constructor() {
        this.root = new TrieNode();
    }

    /**
     * @param {string} word
     * @return {void}
     */
    addWord(word) {
        let curr = this.root;
        for(let char of word){
            const child = curr.children[char] || new TrieNode();
            curr.children[char]=child;
            curr=child;
        }
        curr.word = true;
    }

    /**
     * @param {string} word
     * @return {boolean}
     */
    search(word) {
        
        const dfs = (index,curr)=>{
          
            let node = curr;
            //console.log(node);

            for(let i=index; i<word.length;i++){
                let char = word[i];
                if(char === '.'){
                    for(const char of Object.keys(node.children)){
                      //console.log(node.children[child]);
                        if(dfs(i+1, node.children[char])){
                            return true;
                        }
                    }
                    return false;
                }else{
                  
                    if(char in node.children){
                        node = node.children[char];
                        
                    }else{
                        return false;
                    }
                }
            }
            return node.word;
        }

        let prev = this.root;
        return dfs(0,prev);

    }
}