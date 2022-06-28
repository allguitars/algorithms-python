Amazon Fresh is a new grocery store designed from the ground up to offer a seamless grocery shopping experience to consumers. As a part of a stock clearance exercise at the store, given many piles of fresh products, follow the rules given below to stack the products in an orderly manner.

There are a total of `n` piles of products.

The number of products in each pile is represented by the array `numProducts`.

Select any subarray from the array `numProducts` and pick up products from that subarray such that the number of products you pick from the `ith` pile is strictly less than the number of products you pick from the `(i-1)th` pile for all indices `i` of the subarray.
Find the maximum number of products that can be picked.

Input: [7,4,5,2,6,5]

Constraints: 1<= n <= 5000, 1<= numProducts <= 10^9

Output: 12

Explanation:

Let subarray be **[7,4,5]**, then only **3** can be picked from first pile of 7 (**since 3 < 4**). Thus, sum of products would be **12**, **[3 + 4 + 5]**.

Let subarray be **[7,4,5,2]**, then **3** can be picked from first pile but **None** can be picked from last pile (**since 2 < 5**). Hence, **Invalid** subarray.

Let subarray be **[5,2,6]**, then since last pile has 6 products, **2** can be picked from second pile (**since 2 < 6**). Since second pile has 2 products, only **1** can be picked from first pile of 5 products (**since 1 < 2**). Thus, sum of products would be **9**, **[1 + 2 + 6]**.

Let subarray be **[5,2,6,5]**, then since last pile has 5 products, only **4** can be picked from third pile of 6 (**since 4 < 5**). Since third pile has 4 products, **2** can be picked from second pile (**since 2 < 4**). Since second pile has 2 products, only **1** can be picked from first pile of 5 products (**since 1 < 2**). Thus, sum of products would be **12**, **[1 + 2 + 4 + 5]**.
... and so on.

The **maximum** of all of these sum is 12, hence, return **12**.
