class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let final = []
        let ans = []
        for(let i = 0; i < strs.length; i++) {
        let bSort = strs[i].split("").sort().join('');
        if(final.includes(bSort)) {
            let indexVal = final.indexOf(bSort)
            ans[indexVal].push(strs[i])
        } else {
            
        final.push(bSort)
        ans.push([strs[i]])
        }
}
    return ans
    }
}
