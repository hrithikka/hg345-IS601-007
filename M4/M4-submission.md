<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Hrithikka Guda (hg345)</td></tr>
<tr><td> <em>Generated: </em> 10/16/2023 11:39:40 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/hg345" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sub-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-17T01.01.17image.png.webp?alt=media&token=7e8dc0a4-eaf1-4c93-8d9b-14a8052a6602"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing function and output for Addition<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-17T02.45.49image.png.webp?alt=media&token=b83de073-b791-4e20-93e6-12065d171ae4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing function and output for subtraction<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-17T01.07.50image.png.webp?alt=media&token=9986fe20-4fb8-4ba6-b04d-176c635b2565"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing function and output for Multiplication <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-17T01.11.19image.png.webp?alt=media&token=a5e6b730-56b7-4175-8f13-ebd8569af81b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing function and output foe Division (Handelling errors)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-17T02.30.10image.png.webp?alt=media&token=b890c55c-16b8-487e-9fc4-fccb6d27cc7a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing test case code and output of number-add-number <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-17T02.34.07image.png.webp?alt=media&token=fe53d017-a7da-4688-9e19-a74c3d73114f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing test case code and output of ans-add-number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-17T02.35.02image.png.webp?alt=media&token=fd2f7072-0d2a-49ec-be9d-509c1616d3f2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing test case code and output of number-sub-number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-17T02.36.23image.png.webp?alt=media&token=2344c877-197d-444d-9dcb-e22d96fe6c0c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing test case code and output of ans-sub-number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-17T02.38.19image.png.webp?alt=media&token=3e97694f-f109-4d74-ab9b-6bbfae864ae7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing test case code and output of number-mult-number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-17T02.39.37image.png.webp?alt=media&token=61e744c7-4193-4613-bcb6-f4804bbb566c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing test case code and output of ans-mult-number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-17T02.40.56image.png.webp?alt=media&token=75cb5092-12fd-4d5a-b5f1-c3f594d48868"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing test case code and output of number-div-number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-17T02.43.16image.png.webp?alt=media&token=bdbfaf07-19bf-4948-a8ec-2be01d7517a3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing test case code and output of ans-div-number<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal">In this assignment, I've deepened my understanding of Python<br>programming. I've developed a<br>basic calculator class, applying fundamental<br>concepts of object-oriented programming, and learned to handle errors,<br>especially<br>division by zero. Writing comprehensive test cases using <b>pytest</b><br>has been a valuable skill,<br>ensuring the accuracy and robustness of the code.<br>This module highlighted the importance of<br>clear and well-documented code, as it<br>aids in troubleshooting and collaboration. Overall, I've gained<br>practical<br>experience and insights that will be instrumental in my software development<br>journey.<o:p></o:p></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment, specially include how fixtures and parameterized tests work</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal">I deepened my understanding of the core concepts of test<br>cases, and parameterized<br>tests. Test cases serve as the backbone of software testing,<br>enabling us to validate<br>the correctness of our code. Fixtures play a pivotal<br>role in creating a controlled<br>testing environment, ensuring consistency and<br>helping avoid interference between test cases. Parameterized tests enhance<br>the<br>efficiency of testing by allowing multiple scenarios to be tested with a single<br>test<br>function, thereby reducing redundancy and making test suites more<br>maintainable.&nbsp;<o:p></o:p></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/hrithikka/hg345-IS601-007/pull/9">https://github.com/hrithikka/hg345-IS601-007/pull/9</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/hg345" target="_blank">Grading</a></td></tr></table>