class PrefixTreeNode{
    constructor(){
        this.children = {};
        this.isEndOfWord = false;
    }
}

class PrefixTree {
    constructor() {
        this.root = new PrefixTreeNode();
    }

    /**
     * @param {string} word
     * @return {void}
     */
    insert(word) {
        let curr = this.root;
        for(let char of word){
            const child = curr.children[char] || new PrefixTreeNode();
            curr.children[char] = child;
            curr = child;
        }
        curr.isEndOfWord = true;
    }

    /**
     * @param {string} word
     * @return {boolean}
     */
    search(word) {
        let curr = this.root;
        for(let char of word){
            if(curr.children[char]){
                curr = curr.children[char];
            }else{
                return false;
            }
        }
        return curr.isEndOfWord;
    }

    /**
     * @param {string} prefix
     * @return {boolean}
     */
    startsWith(prefix) {
        let curr = this.root;
        for(let char of prefix){
            if(curr.children[char]){
                curr = curr.children[char]
            }
            else{
                return false;
            }
        }
        return true;
    }
}
