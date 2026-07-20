class Solution {
    /**
     * @param {string} word1
     * @param {string} word2
     * @return {number}
     */
    minDistance(word1, word2) {
        /**
         * create a grid with r = word1.length+1 , c = word2.length+1
         * Assign all the base cases
         * traverse through a both grid;
         * subproblem : a[i] , b[j] -> these things are same
         * relation:
         * if same i+1,j+1
         * else
         * insert : (i,j+1) + 1
         * delete : (i+1,j) + 1
         * relocate : (i+1,j+1) + 1
         * take min of all three and assign to grid[i][j]
         * 
         */

        let cols = word1.length;
        let rows = word2.length;
      

        let grid = Array.from(Array(rows+1),()=>Array(cols+1).fill(0));

        for(let i = 0;i<rows;i++){
            grid[i][cols] = rows-i; 
        }
        for(let j = 0;j<cols;j++){
            grid[rows][j] = cols-j; 
        }
        
        for(let i = rows-1;i>-1;i--){
            for(let j = cols-1 ;j>-1;j--){
                //console.log(i,j)
                if(word1[j]===word2[i]) {
                   // console.log(grid[i][j])
                    grid[i][j] = grid[i+1][j+1];
                }
                else{
                    grid[i][j]= 1 + Math.min(Math.min(grid[i][j+1],grid[i+1][j]),grid[i+1][j+1]);
                }
            }
        }
        return grid[0][0];

    }
}

