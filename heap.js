
// this is a heap class created in javascript in python there is an built in one 
class Heap {
    constructor() {
        this.data = [];
    }

    heapify(numbers) {


        for (let num of numbers) {
            this.push(num);
        }


    }

    length() {
        return this.data.length;
    }

    getParentIndex(i) {
        return Math.floor((i-1)/2)
    }

    getLeftChildIndex(i) {
        return i*2+1;
    }

    getRightChildIndex(i) {
        return i*2+2;
    }

    swap(i1, i2) {
        const temp = this.data[i1];
        this.data[i1] = this.data[i2];
        this.data[i2] = temp;
    }

    push(tuple) {
        // this.data[this.data.length] = tuple;
        this.data.push(tuple);
        this.heapifyUp();
    }

    heapifyUp() {
        let currentIdx = this.data.length-1;

        // while (this.data[currentIdx][0] < this.data[this.getParentIndex(currentIdx)][0]) {
        //     this.swap(currentIdx, this.getParentIndex(currentIdx));
        //     currentIdx = this.getParentIndex(currentIdx);
        // }
        while (currentIdx > 0 && this.data[currentIdx] < this.data[this.getParentIndex(currentIdx)]) {
            this.swap(currentIdx, this.getParentIndex(currentIdx));
            currentIdx = this.getParentIndex(currentIdx);
        }
    }

    poll() {
        const maxValue = this.data[0];

        this.data[0] = this.data[this.data.length-1];
        this.data.length--;
        this.heapifyDown();

        return maxValue;
    }

    heapifyDown() {
        let currentIdx = 0;

        while (this.data[this.getLeftChildIndex(currentIdx)] != undefined) {
            let smallestChildIdx = this.getLeftChildIndex(currentIdx);

            if (this.data[this.getRightChildIndex(currentIdx)] != undefined && this.data[this.getRightChildIndex(currentIdx)] < this.data[this.getLeftChildIndex(currentIdx)])  {
                smallestChildIdx = this.getRightChildIndex(currentIdx);
            }

            if (this.data[currentIdx] > this.data[smallestChildIdx]) {
                this.swap(currentIdx, smallestChildIdx);
                currentIdx = smallestChildIdx;
            } else {
                return;
            }
        }
    }

}

// const heap = new Heap();
// console.log(heap); //Heap { data: [] }
// heap.push(25);
// console.log(heap);
// heap.push(5);
// console.log(heap);
// heap.push(40);
// console.log(heap);
// heap.push(70);
// console.log(heap);
// heap.push(90);
// console.log(heap);
// heap.push(44);
// console.log(heap) // Heap { data: [ 5, 25, 40, 70, 90, 44 ] }
/*
        5
       / \
     25   40
    / \   /
   70 90 44


*/
// a = [];
// a.push(heap.poll());
// a.push(heap.poll());
// a.push(heap.poll());
// a.push(heap.poll());
// a.push(heap.poll());
// console.log('top 5:', a);

// Create an instance of the Heap class
const heap = new Heap();

// Define an array of tuples
const tuples = [
    25,
    5,
    40,
    70,
    90,
    44
];


heap.heapify(tuples);
console.log(heap.data) // [ 5, 25, 40, 70, 90, 44 ]


/**
 so hepify here does not really hepify created instance will make a heap and
 we just keep pushing into it and then the final output will be the heap so
 hre technically we have no heapify
 */
