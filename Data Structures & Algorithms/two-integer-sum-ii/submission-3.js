class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        /**
         * 2,3,5,8,9,11 -> 14
         * 
         * two pointers 
         * second pointer will be pointing at index in my array before target value
         * first pointer is gonna be at a[0]
         * while(fp!==sp)
         * if:
         * a[fp]+a[sp] === target:
         * return [fp,sp];
         * else:
         * a[fp]+a[sp] > target:
         * sp--
         * a[fp]+a[sp] < target:
         * fp++;
         * 
         */

        let firstPointer = 0 , secondPointer = 0;
        // for(let i = numbers.length-1;i>-1;i--){
        //     if(target>numbers[i]) {
        //         secondPointer = i;
        //         break;
        //     }
        // }
        secondPointer = numbers.length-1;


        while(firstPointer<secondPointer){
            if(numbers[firstPointer]+numbers[secondPointer] === target){
                return [firstPointer+1,secondPointer+1];
            }
            else{
                if((numbers[firstPointer]+numbers[secondPointer])<target){
                    firstPointer++;
                }
                else{
                    secondPointer--;
                }
            }
        } 
    }
}
