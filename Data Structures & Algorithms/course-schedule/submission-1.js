class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses, prerequisites) {
        const preMap = new Map();
        const visiting = new Set();

        for (let i = 0; i < numCourses; i++) {
            preMap.set(i, []);
        }

        for (const pair of prerequisites) {
            preMap.get(pair[0]).push(pair[1]);
        }

        for (let c = 0; c < numCourses; c++) {
            if (!this.dfs(c, preMap, visiting)) {
                return false;
            }
        }
        return true;
    }

    /**
     * @param {number} crs
     * @param {Map} preMap
     * @param {Set} visiting
     * @return {boolean}
     */
    dfs(crs, preMap, visiting) {
        if (visiting.has(crs)) {
            return false;
        }
        if (preMap.get(crs).length === 0) {
            return true;
        }

        visiting.add(crs);
        for (const pre of preMap.get(crs)) {
            if (!this.dfs(pre, preMap, visiting)) {
                return false;
            }
        }
        visiting.delete(crs);
        preMap.set(crs, []);
        return true;
    }
}
