var merge = function (nums1, m, nums2, n) {
    let updatePointer = m + n - 1;
    let insertPointer = n - 1;
    let positionPointer = m - 1;

    while (insertPointer >= 0) {
        while (nums1[positionPointer] > nums2[insertPointer]) {
            positionPointer--;
        }

        while (updatePointer > positionPointer) {
            nums1[updatePointer] = nums1[updatePointer - 1]
            updatePointer--;
        }

        nums1[positionPointer + 1] = nums2[insertPointer];

        insertPointer--;
        positionPointer++;
        updatePointer = m + n - 1;
    }
    return nums1;
}

console.log(merge([1, 2, 7, 0, 0, 0], 3, [2, 5, 6], 3))
