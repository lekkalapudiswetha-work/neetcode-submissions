class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {number}
     */
    countComponents(n, edges) {

        const preMap = new Map();
        const visit = new Set();
        let cc = 0;

        for(let i=0;i<n;i++){
            preMap.set(i,[]);
        }

        for(let ed of edges){
            preMap.get(ed[0]).push(ed[1]);
            preMap.get(ed[1]).push(ed[0]);
        }

        const dfs = (v)=>{
            if(visit.has(v)) return;
            visit.add(v);
            if(preMap.get(v).length === 0) return;
            for(let adj of preMap.get(v)){
                dfs(adj);
            }
            return;
        }

        for(let v = 0 ;v<n;v++){
            if(!visit.has(v)){
                cc++;
                dfs(v);
            }
        }

        return cc;


        
    }
}
