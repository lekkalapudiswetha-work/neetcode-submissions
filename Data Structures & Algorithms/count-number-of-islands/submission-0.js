class Solution {
    /**
     * @param {character[][]} grid
     * @return {number}
     */
    numIslands(grid) {

        if(!grid) return 0;

       
        let islands = 0;

        let rows = grid.length;
        let columns = grid[0].length;
        const visit = Array.from(Array(rows),()=>Array(columns).fill(false) );

        const BFS = (i,j)=>{
            let q = [];
            visit[i][j]=true;
            q.push([i,j]);
           // console.log(visit);
            while(q.length>0){
                let directions = [[0,1],[1,0],[0,-1],[-1,0]];
                let res = q.shift();
                //console.log(res);
                let dr = res[0];
                let dc = res[1];
                for (let [a,b] of directions){
                    a=dr+a;
                    b=dc+b;
                    //console.log(a,b);
                    if(a < rows && a > -1 && b < columns && b > -1 && visit[a][b] === false && grid[a][b] === '1'){
                        q.push([a,b]);
                        visit[a][b]=true;
                        // console.log(q);
                        // console.log(visit);
                        
                        
                    }
                }

            }
        }
        for(let i =0;i<rows;i++){
            for(let j=0;j<columns;j++){
                if(grid[i][j] === '1' && visit[i][j] === false){
                    // console.log(visit);
                    // console.log(i,j);
                    islands++;
                    BFS(i,j);
                }
            }
        }

        return islands;
    }
}
