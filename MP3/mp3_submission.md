<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3 - Thankful Giving</td></tr>
<tr><td> <em>Student: </em> Hrithikka Guda (hg345)</td></tr>
<tr><td> <em>Generated: </em> 12/12/2023 5:46:21 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/hg345" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p><b>Initial Prep:</b><div><ol><li>Create a new app on heroku called course-section-ucid-td</li><ol><li>replace course, section, ucid accordingly</li></ol><li>Go to the Settings tab of the app and add the config var of DB_URL and your DB connection string<br></li><li>Go to your github repository and go to Settings and add a new repository secret called&nbsp;HEROKU_APP_NAME_MP3 and fill in your new app name as the value</li><li>Note: we will just have one instance</li><li>Grab the yml file from the shared branch containing the initial code templates and put it in your .github/workflows folder, you shouldn&#39;t need to edit it</li><li>Make sure Wakatime is setup correctly and recording time correctly</li></ol><div>Baseline code:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>Example Site:&nbsp;<a href="https://is601-mt85-td-f7d7f9bec981.herokuapp.com">https://is601-mt85-td-f7d7f9bec981.herokuapp.com</a></div><div><br></div><div><b>Primary Instructions:</b></div></div><div><ol><li>Checkout any latest branch (dev is fine) and pull the latest changes</li><li>Create a new branch per the recommended name below</li><li>Copy the rest of the files from the shared branch containing the initial code templates</li><ol><li>It&#39;s important that you have just one folder for this project at the root level of your repository, in my example I called mine MP3 and it contains the entire app</li><li>Make sure the .csv files are copied as csv data and not html tables (github may try to render them so choose the &quot;Raw&quot; button of the file to get the raw text)</li></ol><li>Create a virtual environment inside the MP3 related folder and pip install the requirements.txt (you shouldn&#39;t need to manually add anything else)</li><li>Copy your .env file from flask_sample into MP3 (again this should gray out as it should be in the .gitignore files) but it&#39;s necessary for local development</li><li>Once everything is copied over immediately add/commit the changes and record the commit message as something similar to &quot;template files&quot;</li><li>Push the baseline and open a pull request from this branch to dev (don&#39;t merge it until you have the markdown file)</li><li>Execute the init_db.py file for this project to generate the two required tables</li><li>Proceed to solve/implement the missing pieces noted by &quot;TODO&quot; comments throughout the code (which are also shown below in the various deliverables)</li><li>As soon as you start working on an item add your ucid-date as a comment so you don&#39;t forget</li><li><b>Add and commit after each TODO item (or relatively frequently to build up a proper history; do not save this process for the end)</b></li><li>For the below deliverables, you&#39;ll be capturing screenshots from your new heroku app (ensure the url is clearly visible)</li><li>Once finished, copy the markdown or download the file and add it to your MP3 related folder as a .md file (don&#39;t forget the extension)</li><li>Do your final add/commit/push once satisfied that everything is all set</li><li>Merge the pull request that was opened in step 7</li><ol><li>This will trigger a deploy to dev (due to the original yml files) but this app won&#39;t be affected</li></ol><li>Create a pull request from dev to prod and merge it</li><ol><li>This will trigger a deploy to prod (due to the original yml files) but this app won&#39;t be affected</li></ol><li>From the prod branch on github, navigate to your submission.md file and grab that link to paste to Canvas</li></ol><div><b>Objective/Project Description:</b></div></div><div>You&#39;ll be implementing a cross-organization Thanksgiving Drive application.</div><div>There will be CRUD operations to manage organizations and CRUD operations to manage donations related to organizations as well as an import page to preload given data.</div><div>Some files are provided as fully working and should not be modified, typically they&#39;ll have comments like &quot;DO NOT EDIT&quot;.</div><div>Other files are basic skeleton files with a number of &quot;TODO&#39;s&quot; that you need to solve. It&#39;s best to make the code changes near where the particular TODO is (do not delete the TODO comments).</div><div>There are also provided test case files.</div><div>Between the TODOs and the tests you must implement the missing pieces to get all tests to pass for full credit.</div><div>Do not edit any of the test cases except for a caveat I&#39;ll mention in another paragraph below.</div><div><br></div><div><b>Caveat:</b><br>If you can&#39;t solve a test case first ensure you run <code>pytest -rA</code> locally to show and capture the test pass/fail summary, then for any of the cases you can&#39;t achieve add the word &quot;off_&quot; in front of the function name. (i.e., if a test is test_myfile() rename it to off_test_myfile()).</div><div>This will disable the test case allowing you to deploy to potentially receive partial credit.</div><div><br></div><div>Files you shouldn&#39;t edit:</div><div>layout.html</div><div>country_state_selector.html</div><div>flash.html</div><div>organization_dropdown.html</div><div>sort_filter.html</div><div>any test files (unless it&#39;s for the caveat)</div><div>requirements.txt</div><div>Dockerfile</div><div>any files in the sql folder</div><div>geography.py</div><div>index.py</div><div>main.py</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div></p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Solving the index.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the index.html page being shown and of the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-11T07.29.31image.png.webp?alt=media&token=756348ce-3b41-400c-830a-efdacc32a03c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code changes<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T07.01.33image.png.webp?alt=media&token=b2071fab-89b1-4c5a-896f-aee55b4e65b6"/></td></tr>
<tr><td> <em>Caption:</em> <p>INDEX PAGE ON HEROKU<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Solving the nav.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the navbar and the edited code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T07.40.47image.png.webp?alt=media&token=2d20a99f-9730-4d0b-bfbf-225aa0166e55"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing navbar with my ucid and heroku url<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T07.51.12image.png.webp?alt=media&token=b08db736-396e-4e68-9f2f-391e8eb192d0"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing nav edited code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Solving the admin upload </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the code changes related to the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T07.57.59image.png.webp?alt=media&token=75c1a6b8-b7e6-409c-a391-68d80d71ec9e"/></td></tr>
<tr><td> <em>Caption:</em> <p>checking if the file is a .csv file, if not, flash a proper<br>error message and don&#39;t attempt to process the file<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T08.03.27image.png.webp?alt=media&token=6bd9f196-4053-4bda-a414-e60ea3e47d99"/></td></tr>
<tr><td> <em>Caption:</em> <p> Showing reading the csv file as a dict, extracting the organization data<br>and append it to the organization list as a dict for each row<br>that contains all of the required fields.,extract the donation data and append it<br>to the donation list as a dict for each row that contains all<br>of the required fields.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T08.05.48image.png.webp?alt=media&token=c48f2fa1-d015-46a7-954c-458e24e3b786"/></td></tr>
<tr><td> <em>Caption:</em> <p> Displaying a flash message about the number of organizations that were successfully<br>processed, a flash message (info) if no organizations were eligible/processed, a flash message<br>about the number of donations that were successfully processed and a flash message<br>(info) if no donations were eligible/processed<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Solve the donation related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T08.10.22image.png.webp?alt=media&token=d62e5377-ccc0-4c45-a2b4-8678f5fd5776"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing create view of donations with Add url<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T08.17.20image.png.webp?alt=media&token=4f1869db-7f3d-4dc3-8a43-a81b626ecfd8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing edit view of donations with Edit url<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T08.20.36image.png.webp?alt=media&token=4914e9cf-d342-4791-a21c-ef28def657a0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing manage_donations html code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T08.21.55image.png.webp?alt=media&token=cfd2b9da-7921-403c-a6bb-b9e65e938376"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing manage_donations html code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T09.58.08image.png.webp?alt=media&token=cc80016b-526a-4a07-8106-653807e696ca"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the search page loaded with proper list of donations (without any filter<br>applied)<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.00.41image.png.webp?alt=media&token=47ec8cd0-9566-41c7-a7bc-2e1364e979ae"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing donations from Carpenter, Fuller and Frye Donations organization<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.02.52image.png.webp?alt=media&token=d8451454-4e3a-442d-b7a5-b29c12da6d54"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing list donations html code of first and last name, Email, item name<br>and organization with my ucid and date<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.05.36image.png.webp?alt=media&token=1ba136aa-e113-4919-b8d7-8380cdfd5e0e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing html code d0nations filtering<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.07.56image.png.webp?alt=media&token=373e3a4d-e217-4677-8689-6e62770e4b19"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing html code for iteration over rows for generating proper tr &amp; yd<br>elements<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshots of the donations search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.11.08image.png.webp?alt=media&token=9d233d3d-612b-4446-ae99-3defd55b02be"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing code for Searches 1 to 5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.14.25image.png.webp?alt=media&token=9e5df0cc-1f14-4453-bfb0-5450c6d0958c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing code for Searches 6 to 12<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of the donations add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.16.43image.png.webp?alt=media&token=602de0dc-79cc-4a0e-8362-a37e427d34d5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing code for  adds1 to 6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.18.40image.png.webp?alt=media&token=70f89036-9352-4179-a237-0621f43cd503"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing add 7 to 12 and add 7 error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of donations edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.22.07image.png.webp?alt=media&token=9a02661d-5109-412e-98ad-dd8e6b405b1f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing code for edits 1 to 8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.24.11image.png.webp?alt=media&token=761f72b0-efc1-43ba-94c2-6242f2019932"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing code for edit 9 to 12<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.25.43image.png.webp?alt=media&token=c6e76bec-cfeb-4ff4-aed1-fd2afbbca26b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing edits 13 to 15<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of the donation delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.27.27image.png.webp?alt=media&token=05b378dd-d9db-4966-af1d-35a194f796b9"/></td></tr>
<tr><td> <em>Caption:</em> <p>showing delete 1 to 5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.29.26image.png.webp?alt=media&token=69703c7f-5b2b-4302-9052-4b1660982ffb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing deleting a donation record successfully from website<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Solve the organization related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.35.02image.png.webp?alt=media&token=bb654cf4-b090-4407-920c-7bac757fbd8e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing create view of the organization<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.35.54image.png.webp?alt=media&token=b4a04073-ebb4-4bfa-824f-aa8752c76e34"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing edit view of the organization<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.37.27image.png.webp?alt=media&token=6967c5d8-ebd1-48aa-b850-421a47bf1edf"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing code of manage organization<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.39.07image.png.webp?alt=media&token=45a851cd-fdf0-4956-afea-8b6fa1459cc0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search page of the Organizations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.41.43image.png.webp?alt=media&token=222107fa-ba37-497d-92ed-685dcf0e1835"/></td></tr>
<tr><td> <em>Caption:</em> <p>search page with filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.44.26image.png.webp?alt=media&token=e14adbf3-fbcb-40e2-a20f-cefe99df5138"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filter code <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.45.30image.png.webp?alt=media&token=ffd7cf6b-8c3d-4a8c-b930-856eb0f28afd"/></td></tr>
<tr><td> <em>Caption:</em> <p>code for iterating over rows and generating proper tr and td elements <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the organization search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.52.54image.png.webp?alt=media&token=3bd60de4-0667-45d8-9e0a-2fa07e5ec8ee"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for search 1 to 5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.54.13image.png.webp?alt=media&token=35d695d3-c0f3-40e2-b2d1-56553298b5ca"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for search 6 to 9<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of organization add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.56.03image.png.webp?alt=media&token=c1278ae2-e475-4883-a0ad-e9ba35e28e09"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for Add 1 to 6a<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T10.57.51image.png.webp?alt=media&token=fce17406-23cb-42aa-bad0-773c1c96fa9d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for Add 7 to 11<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of organization edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T11.06.41image.png.webp?alt=media&token=7c4e08a3-31be-49be-aa35-aa847f96ce62"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for Edit 1 to 6a<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T11.08.32image.png.webp?alt=media&token=d998b574-5a98-4f68-836a-834e68570a43"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for Edit 7 to 13<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of organization delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T11.09.38image.png.webp?alt=media&token=4f7db52d-5abe-412c-8a89-4454afa6e677"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for Delete 1 to 5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T11.13.06image.png.webp?alt=media&token=8c06a972-adc9-426d-ac7a-739b9486e8af"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successful deletion of Organization from website<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Test cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of passing test_donations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T11.24.08image.png.webp?alt=media&token=c882234c-f26c-4615-8d67-33ab6fd24cee"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing summary of 13 passed test cases of test_donations.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of passing test_organizations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T22.31.23image.png.webp?alt=media&token=3806239b-e949-473b-a305-184358adf94a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing summary test cases for test_organizations.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot of passing test_upload.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T22.34.03image.png.webp?alt=media&token=6dd63ce5-cf9c-4006-8992-e551f7c44be0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing failed test case of test_upload.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot of passing test_index.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T11.49.44image.png.webp?alt=media&token=b9b6fe25-00c7-487c-beee-3f9c3da98ed3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing summary of 3 passed test cases of test_index.py<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Did all tests pass? If no, list which failed and explain why</td></tr>
<tr><td> <em>Response:</em> <p>ERROR test/test_upload.py::test_upload_csv - Exception: Error while executing statement: Cannot delete or update a<br>parent row: a foreign key constraint fails<div></p><br><p class="MsoNormal">Foreign key constraint fails-&gt; Cannot delete<br>or<br>update a record because other records in a different table depend on it.<br>This<br>is to maintain data integrity, and the database prevents actions that would<br>leave related<br>records in an inconsistent state.<o:p></o:p></p><div><br><div><br></div></div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request link for this assignment branch</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/hrithikka/hg345-IS601-007/pull/24">https://github.com/hrithikka/hg345-IS601-007/pull/24</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of your commit history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T11.52.27image.png.webp?alt=media&token=7d0161ca-7e86-43db-adda-6af9b959aba4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing Git Commits<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of your wakatime dashboard for this class/project</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-12T22.45.50image.png.webp?alt=media&token=9c1ccac8-1f8f-4a30-97b7-bef6ff4fb715"/></td></tr>
<tr><td> <em>Caption:</em> <p>WakaTime Dashboard<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to the application from the new vm/app</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-007-hg345-td-e653c7cce8d9.herokuapp.com/">https://is601-007-hg345-td-e653c7cce8d9.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/hg345" target="_blank">Grading</a></td></tr></table>