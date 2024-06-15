<h2><a href="https://www.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/0?category&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=max-sum-in-sub-arrays">Max sum in sub-arrays</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 20px;">Given an array <strong>Arr</strong>, with indexes running from <strong>0 to N-1</strong>, select any two indexes, <strong>i</strong> and <strong>j</strong> such that <strong>i&lt;=j-1</strong>. From subarray <strong>Arr[i...j]</strong>, find the <strong>two smallest numbers </strong>and add them, you will get <strong>score </strong>for that subarray. Your task is to return <strong>maximum score </strong>possible in the given array <strong>Arr</strong>.</span><br>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input :</strong> arr[] = [4, 3, 1, 5, 6]
<strong>Output :</strong> 11
Subarrays with smallest and 
second smallest are,
[4, 3]        
smallest = 3    second smallest = 4
[4, 3, 1]    
smallest = 1    second smallest = 3
[4, 3, 1, 5]    
smallest = 1    second smallest = 3
[4, 3, 1, 5, 6]    
smallest = 1    second smallest = 3
[3, 1]         
smallest = 1    second smallest = 3
[3, 1, 5]     
smallest = 1    second smallest = 3
[3, 1, 5, 6]    
smallest = 1    second smallest = 3
[1, 5]        
smallest = 1    second smallest = 5
[1, 5, 6]    
smallest = 1    second smallest = 5
[5, 6]         
smallest = 5    second smallest = 6
Maximum sum among all 
above choices is, 5 + 6 = 11</span></pre>
<div>&nbsp;</div>
<div><span style="font-size: 18px;"><strong>Example 2:</strong></span></div>
<pre><span style="font-size: 18px;"><strong>Input :</strong> arr[] = {5, 4, 3, 1, 6} </span>
<span style="font-size: 18px;"><strong>Output :</strong> 9</span></pre>
<p>&nbsp;</p>
<p><span style="font-size: 18px;"><strong>Your Task:&nbsp;&nbsp;</strong><br>You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>pairWithMaxSum()</strong>&nbsp;which takes the array <strong>Arr[]</strong> and its size <strong>N</strong><strong> </strong>as inputs and returns </span><span style="font-size: 20px;">the maximum sum of smallest and second smallest elements chosen from all possible subarrays.</span><br><br><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(N)<br><strong>Expected Auxiliary Space:</strong> O(1)</span><br><br><span style="font-size: 20px;"><strong>Constraints:</strong><br>2 ≤ N ≤ 10<sup>5</sup><br>1 ≤ A[i] ≤ 10<sup>18</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Stack</code>&nbsp;<code>Data Structures</code>&nbsp;