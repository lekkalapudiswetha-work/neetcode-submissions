class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses, prerequisites) {

        const preMap = new Map();
        const visit = new Set();

        for(let i =0;i<numCourses;i++){
            preMap.set(i,[]);
        }

        for(let pair of prerequisites){
            preMap.get(pair[0]).push(pair[1]);
        }

        const dfs = (curr)=>{
            if(visit.has(curr)) return false;

            if(preMap.get(curr).length === 0){
                return true;
            }

            visit.add(curr);

            for(let pre of preMap.get(curr)){
                if(!dfs(pre)){
                    return false;
                }
            }

            visit.delete(curr);
            preMap.set(curr,[]);

            return true;

        }

        for(let c = 0 ;c<numCourses;c++){
            if(!dfs(c)) return false;
        }
        return true;
        
    }
}
