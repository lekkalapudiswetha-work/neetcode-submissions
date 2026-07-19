class Solution {
    /**
     * @param {number[][]} grid
     */
    islandsAndTreasure(grid) {
        /**
         * Input : we have n*m grid matrix
         * I have queue and visit array 
         * for all i,j have a[i][j] === 0
         * add it to queue
         * add mark it visited
         * 
         * let dist = 0;
         * until q is empty :
         * grid[i][j]=dist;
         * traverse to add adj a[i][j]
         * if(adj[i][j]!==-1 && !visited) 
         *   add a[i][j] to queue
         *   and mark a[i][j] visited
         * dist ++;
         *        
         */

        let q = [];
        let visit = new Set();
        let rows = grid.length;
        let columns = grid[0].length;

        const directions = (i,j)=>{
            if(i<rows && j<columns && i>-1 && j>-1 && grid[i][j]!== -1 && !visit.has(i+','+j)){
                q.push([i,j]);
                visit.add(i+','+j);
            }

        }

        for(let r =0;r<rows;r++){
            for(let c=0;c<columns;c++){
                if(grid[r][c] === 0){
                    q.push([r,c]);
                    visit.add(r+','+c);
                }
            }
        }
        let dist = 0;
        while(q.length){
            let len = q.length;
            for(let i=0;i<len;i++){
                let [r,c] = q.shift();
                grid[r][c] = dist;
                directions(r+1,c);
                directions(r-1,c);
                directions(r,c+1);
                directions(r,c-1);
            }
            dist+=1;
        }
    }
}
