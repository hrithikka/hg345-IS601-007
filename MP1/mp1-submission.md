<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Hrithikka Guda (hg345)</td></tr>
<tr><td> <em>Generated: </em> 10/10/2023 1:30:07 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/hg345" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T01.52.22image.png.webp?alt=media&token=32b39c83-359d-46be-bc59-6b531daaed13"/></td></tr>
<tr><td> <em>Caption:</em> <p>add_task function<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T01.55.03image.png.webp?alt=media&token=28132249-37b9-44c0-8e04-3f80cd0f13df"/></td></tr>
<tr><td> <em>Caption:</em> <p>Complete add_task edited function<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T01.59.17image.png.webp?alt=media&token=9cc0b185-8955-48cd-886b-a582c1029aea"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task added successfully with Task name, description and due. <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T02.03.55image.png.webp?alt=media&token=a3931a0d-62c3-40e7-b982-489855022918"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task rejected to add due to invalid date format<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T02.05.05image.png.webp?alt=media&token=3f21d736-5d8c-462a-b792-ee0fe7ce2ed1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task rejected to add due to empty input.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal" style="margin-bottom: 0cm; line-height: normal; background-image: initial; background-position: initial; background-size: initial; background-repeat:<br>initial; background-attachment: initial; background-origin: initial; background-clip: initial;"><span style="font-size: 10.5pt; font-family: Roboto;">The <b>add_task()</b> function<br>ensures<br>the addition of tasks with data integrity. It begins by updating the <b>lastActivity</b><br>with<br>the current datetime and then proceeds to validate and set the name,<br>description, and<br>due date, rejecting the addition if any are missing. The due<br>date is verified<br>against allowed formats using <b>str_to_datetime()</b>. If all<br>checks pass, a new task is appended<br>to the task list, and a confirmation<br>message is generated. Importantly, the <b>save()</b> function<br>is called last.&nbsp;<o:p></o:p></span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T02.16.16image.png.webp?alt=media&token=db9dda49-d565-4f17-a49f-343c8d22dcd1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Complete process update function.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal"><span style="font-size: 10pt; line-height: 107%; font-family: Roboto; background-image: initial; background-position: initial; background-size:<br>initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">The<b> "Process Update Logic"</b><br>function is<br>designed to update a task by index. This is done by first retrieving<br>the<br>task from the tasks list using the provided index. To ensure data<br>integrity, it<br>is checked for index out-of-bounds scenarios and generates<br>appropriate error messages if the index<br>is invalid. This function also displays<br>the existing values for each property, replacing the<br>"TODO"<br>placeholders in the input text with the actual task data.<o:p></o:p></span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T02.26.47image.png.webp?alt=media&token=620dbc4d-9ab7-4f3c-889f-b16c1c70dc99"/></td></tr>
<tr><td> <em>Caption:</em> <p>Update task logic<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T02.28.29image.png.webp?alt=media&token=404a3a0e-21ac-404e-91b8-e353b349136c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Complete Update Task logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T02.33.41image.png.webp?alt=media&token=2fa7b0e9-cf56-4c39-8759-e04daac714f6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output of Successful Task update.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T02.40.15image.png.webp?alt=media&token=2fb74103-957b-4fe1-a551-029fb725e5b0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task update rejected due to empty response.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T02.39.20image.png.webp?alt=media&token=8d7eecb6-2690-47ba-9fc3-29810914a316"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task update rejected due to invalid index.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal"><span style="font-size: 10pt; line-height: 107%; font-family: Roboto; background-image: initial; background-position: initial; background-size:<br>initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">The<b> "Update Task"</b> function<br>allows for<br>modifying a task by its index while ensuring valid indices and<br>displaying informative error<br>messages. It updates task properties with provided<br>data, records the last activity as the<br>current date and time, and confirms<br>updates with a message. It concludes by calling<br><b>save()</b>.<o:p></o:p></span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T03.14.22image.png.webp?alt=media&token=65575b10-3d2b-40ec-98f1-c360359df30f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Complete mark done logic with the comment<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T03.16.41image.png.webp?alt=media&token=ea1bd5a5-eae7-48a9-86f7-eb4a2a3f7b53"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully marked done for the completed tasks.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T03.17.51image.png.webp?alt=media&token=4b9432fb-887c-4196-bdc3-dcf603acb80e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Tasks already completed<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T03.31.26image.png.webp?alt=media&token=25d69d33-0155-4b06-81b3-3f3ddd0c3cf5"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid index<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal"><span style="font-size: 10pt; line-height: 107%; font-family: Roboto; background-image: initial; background-position: initial; background-size:<br>initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">The "mark done" function locates<br>a task by index and address out-of-bounds scenarios with error messages.<br>If the task<br>is not already marked as completed, it is updated to<br>"done," and the current<br>date and time is recorded. A message is displayed for tasks that are<br>already completed.&nbsp; the "save" operation is called after all other<br>modifications.<o:p></o:p></span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T03.38.09image.png.webp?alt=media&token=6b5a0909-0042-4727-a048-6d51768b6799"/></td></tr>
<tr><td> <em>Caption:</em> <p>Complete logic of the View_task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T03.39.44image.png.webp?alt=media&token=ea0eb97a-ced6-4749-8b84-1b305b56c62c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully view of the task details.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T03.40.55image.png.webp?alt=media&token=7082afa8-9cca-42cb-a073-d5c38e503e21"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid index<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T03.43.33image.png.webp?alt=media&token=afd49a24-3458-4ae9-a1b7-8e026258332e"/></td></tr>
<tr><td> <em>Caption:</em> <p>list of four tasks<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T03.49.44image.png.webp?alt=media&token=01364271-ae49-4739-94b3-17b72c0f25e7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Complete logic for deletion of required task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T03.51.47image.png.webp?alt=media&token=9ed60163-ea5c-465e-8659-15f407c14fcf"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully deleting a task.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T03.52.43image.png.webp?alt=media&token=84cc9c69-d8b5-429b-8beb-54a040de3d2f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Task not found<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal"><span style="font-size: 10pt; line-height: 107%; font-family: Roboto; background-image: initial; background-position: initial; background-size:<br>initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">The <b>delete_task()</b> function handles<br>the removal<br>of tasks from the tracker using the provided index. It displays<br>success or failure<br>messages, with success indicating the successful removal of<br>the task and failure messages for<br>invalid indices. The "save()" operation is called last to save the updated task<br>list.<o:p></o:p></span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T04.18.09image.png.webp?alt=media&token=f9b9f8c6-6805-4593-acf9-aea3fae7fa5c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Complete logic for incomplete tasks.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T04.19.25image.png.webp?alt=media&token=d881bd2a-85e7-4ba8-bf84-0c4572b825dd"/></td></tr>
<tr><td> <em>Caption:</em> <p>One incomplete task is shown<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T04.35.55image.png.webp?alt=media&token=1455640a-5fd3-4ff1-9d64-f8a80363902b"/></td></tr>
<tr><td> <em>Caption:</em> <p>No incomplete tasks<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal"><span style="font-size: 10pt; line-height: 107%; font-family: Roboto; background-image: initial; background-position: initial; background-size:<br>initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">&nbsp;</span><span style="font-family: Roboto; font-size: 10pt;">The<br></span><b style="font-family: Roboto; font-size: 10pt;">get_overdue_tasks()</b><span style="font-family: Roboto; font-size: 10pt;"> function is used to<br>generate a list of tasks that have overdue due dates (older than<br>the current<br>date and time) and are not marked as complete. This list is then<br>passed<br>to a task listing function for display or further processing.</span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T04.31.08image.png.webp?alt=media&token=a4cc9b7f-b6e6-4118-827c-205bbef56f26"/></td></tr>
<tr><td> <em>Caption:</em> <p>Complete logic for overdue tasks<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T04.34.07image.png.webp?alt=media&token=98e6808a-483a-40fe-8e36-ac9104408cf9"/></td></tr>
<tr><td> <em>Caption:</em> <p>One overdue task is shown<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T04.34.58image.png.webp?alt=media&token=e35e928e-e1b4-4949-b163-fc04885b3541"/></td></tr>
<tr><td> <em>Caption:</em> <p>no overdue tasks<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <p><span style="--tw-border-spacing-x: 0; --tw-border-spacing-y: 0; --tw-translate-x: 0; --tw-translate-y: 0; --tw-rotate: 0; --tw-skew-x: 0;<br>--tw-skew-y: 0; --tw-scale-x: 1; --tw-scale-y: 1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness:<br>proximity; --tw-gradient-from-position: ; --tw-gradient-via-position: ; --tw-gradient-to-position: ; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ;<br>--tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width: 0px; --tw-ring-offset-color: #fff; --tw-ring-color: rgb(59 130<br>246 / 0.5); --tw-ring-offset-shadow: 0 0 #0000; --tw-ring-shadow: 0 0 #0000; --tw-shadow: 0<br>0 #0000; --tw-shadow-colored: 0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale:<br>; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ;<br>--tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate:<br>; --tw-backdrop-sepia: ; font-family: Roboto; font-size: 10pt;">The&nbsp;</span><b style="--tw-border-spacing-x: 0; --tw-border-spacing-y: 0; --tw-translate-x: 0;<br>--tw-translate-y: 0; --tw-rotate: 0; --tw-skew-x: 0; --tw-skew-y: 0; --tw-scale-x: 1; --tw-scale-y: 1; --tw-pan-x:<br>; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness: proximity; --tw-gradient-from-position: ; --tw-gradient-via-position: ; --tw-gradient-to-position: ;<br>--tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing: ; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width:<br>0px; --tw-ring-offset-color: #fff; --tw-ring-color: rgb(59 130 246 / 0.5); --tw-ring-offset-shadow: 0 0 #0000;<br>--tw-ring-shadow: 0 0 #0000; --tw-shadow: 0 0 #0000; --tw-shadow-colored: 0 0 #0000; --tw-blur:<br>; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ; --tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ;<br>--tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness: ; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate:<br>; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ; --tw-backdrop-sepia: ; font-family: Roboto; font-size: 10pt;">get_overdue_tasks()</b>&lt;span<br>style=&quot;--tw-border-spacing-x: 0; --tw-border-spacing-y: 0; --tw-translate-x: 0; --tw-translate-y: 0; --tw-rotate: 0; --tw-skew-x: 0; --tw-skew-y:<br>0; --tw-scale-x: 1; --tw-scale-y: 1; --tw-pan-x: ; --tw-pan-y: ; --tw-pinch-zoom: ; --tw-scroll-snap-strictness: proximity;<br>--tw-gradient-from-position: ; --tw-gradient-via-position: ; --tw-gradient-to-position: ; --tw-ordinal: ; --tw-slashed-zero: ; --tw-numeric-figure: ; --tw-numeric-spacing:<br>; --tw-numeric-fraction: ; --tw-ring-inset: ; --tw-ring-offset-width: 0px; --tw-ring-offset-color: #fff; --tw-ring-color: rgb(59 130 246<br>/ 0.5); --tw-ring-offset-shadow: 0 0 #0000; --tw-ring-shadow: 0 0 #0000; --tw-shadow: 0 0<br>#0000; --tw-shadow-colored: 0 0 #0000; --tw-blur: ; --tw-brightness: ; --tw-contrast: ; --tw-grayscale: ;<br>--tw-hue-rotate: ; --tw-invert: ; --tw-saturate: ; --tw-sepia: ; --tw-drop-shadow: ; --tw-backdrop-blur: ; --tw-backdrop-brightness:<br>; --tw-backdrop-contrast: ; --tw-backdrop-grayscale: ; --tw-backdrop-hue-rotate: ; --tw-backdrop-invert: ; --tw-backdrop-opacity: ; --tw-backdrop-saturate: ;<br>--tw-backdrop-sepia: ; font-family: Roboto; font-size: 10pt;&quot;&gt;&nbsp;function is used to generate a list of<br>tasks that have overdue due dates (older than the current date and time)<br>and are not marked as complete. This list is then passed to a<br>task listing function for display or further processing.</span><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T04.46.26image.png.webp?alt=media&token=88a1bad2-b5c0-4348-8429-b2fd2d49b5c5"/></td></tr>
<tr><td> <em>Caption:</em> <p>get remaining time logic<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T04.48.30image.png.webp?alt=media&token=bec7eee0-29cf-4877-adfd-9159ec4e67b0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Complete get remaining time logic<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T04.50.34image.png.webp?alt=media&token=e63496c5-02d0-42f7-ae29-2eb909acb54b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Time of task overdue<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T04.51.40image.png.webp?alt=media&token=870442e9-6f96-48d5-ad75-15887d01cb11"/></td></tr>
<tr><td> <em>Caption:</em> <p>Time of the task remaining<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal"><span style="font-size: 10pt; line-height: 107%; font-family: Roboto; background-image: initial; background-position: initial; background-size:<br>initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">The <b>get_time_remaining()</b> function<br>retrieves a task<br>based on the provided index, considers scenarios where the<br>index might be invalid, and<br>provides with appropriate error messages in such<br>cases. It calculates the time remaining in<br>terms of days, hours, minutes, and<br>seconds between the task's due date and the<br>current time. The function prints<br>this time remaining in a clear format, separating the<br>time components. If the<br>due date is in the past, the function indicates how<br>many days, hours, minutes,<br>and seconds the task is overdue, ensuring that the values<br>are positive.&nbsp;<o:p></o:p></span></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T04.56.36image.png.webp?alt=media&token=ea431973-98a1-4190-89d0-33d65a7ad561"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output of the deliverables from VS Code terminal<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T04.59.46image.png.webp?alt=media&token=5b627210-1ae1-4e56-8407-539e0acd7d43"/></td></tr>
<tr><td> <em>Caption:</em> <p>Present Screenshot of the git bash working <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T05.01.24image.png.webp?alt=media&token=d0ed5f7e-7236-441f-a869-efdbc2215a16"/></td></tr>
<tr><td> <em>Caption:</em> <p>JSON FILE<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-10-10T05.02.08image.png.webp?alt=media&token=449af4b7-cf40-4ecf-89ca-898cf5765cbe"/></td></tr>
<tr><td> <em>Caption:</em> <p>Json file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p class="MsoNormal"><span style="font-size: 10pt; line-height: 107%; font-family: Roboto; background-image: initial; background-position: initial; background-size:<br>initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial;">In this "Tracker app" project,<br>I<br>learned practical lessons about making sure users provide accurate information,<br>handling data effectively, and<br>giving clear feedback to users. The project also<br>taught me how to organize my<br>work and manage different dates, keeping<br>everything well-documented. It's important to ensure that data<br>is complete and<br>correct, and the project showed me how to store and protect<br>data properly.<br>Dealing with various date formats helped me get better at understanding and<br>processing<br>dates. Finally, I learned how structured project management and<br>organized code can make the<br>development process smoother. These lessons have<br>improved my software development skills and my ability<br>to create user-friendly<br>applications.<o:p></o:p></span></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/hrithikka/hg345-IS601-007/pull/7">https://github.com/hrithikka/hg345-IS601-007/pull/7</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/hg345" target="_blank">Grading</a></td></tr></table>