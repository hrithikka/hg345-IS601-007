<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 API Project</td></tr>
<tr><td> <em>Student: </em> Hrithikka Guda (hg345)</td></tr>
<tr><td> <em>Generated: </em> 12/24/2023 4:58:58 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-3-api-project/grade/hg345" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Data Association </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> How will this data relate to the User</td></tr>
<tr><td> <em>Response:</em> <p>In this project, users interact with API data to curate a collection of<br>their favorite horror genre movies based on specific criteria, such as IMDb ratings,<br>release years, and language. They initiate data retrieval by specifying their preferences, and<br>the project utilizes API endpoints to provide movie details like title, genre, IMDb<br>rating, and synopsis. Users can add selected movies to their favorites and view<br>in-depth information about each film, aiding them in making informed decisions about which<br>movies to include in their collection. Additionally, there may be an option for<br>users to build a watchlist for future viewing. Overall, the user&#39;s goal is<br>to discover, organize, and enjoy a personalized selection of horror movies through seamless<br>interaction with the provided API data.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Data changes</td></tr>
<tr><td> <em>Response:</em> <p>When updates are applied via the manual edit form or future API data<br>synchronization in this application, the behavior of associated data depends on the relationship<br>type and the role of administrators. The data association appears to involve a<br>many-to-many relationship, where users can have multiple favorite horror movies, and movies can<br>be favorited by multiple users. When users update their favorite movies through the<br>manual edit form, the application likely manages these changes by creating, updating, or<br>deleting entries in a junction table that represents the user-movie relationship. Future API<br>data synchronization involves updating the application&#39;s local database with changes from the API,<br>including modifications to movie details and the removal of movies that no longer<br>meet user criteria. Admins, who have the authority to add, update, and assign<br>privileges, play a crucial role in managing these updates, ensuring data accuracy, and<br>controlling user access to these functions.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how/where the user can associate the data with themselves</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-24T21.11.26image.png.webp?alt=media&token=d2ba8033-2895-4ac7-b4b1-60c5d441f425"/></td></tr>
<tr><td> <em>Caption:</em> <p>Movies are listed as per the data in from the api<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-24T21.14.02image.png.webp?alt=media&token=4c7507a6-c5fd-4334-a814-54f8ba0fc8ea"/></td></tr>
<tr><td> <em>Caption:</em> <p>User can then add them to their favourites<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-24T21.16.14image.png.webp?alt=media&token=27e3eb5b-9734-4c78-b393-5e04758018c9"/></td></tr>
<tr><td> <em>Caption:</em> <p>related table<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-24T21.17.29image.png.webp?alt=media&token=5b902cbd-4534-48ae-bac5-08f4ffc19203"/></td></tr>
<tr><td> <em>Caption:</em> <p>related code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> List Associated Entities to the logged in user </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the page where a user can list related/associated entities</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-24T21.25.08image.png.webp?alt=media&token=d2a2d761-3a7f-47fe-b5fa-d2a4e7bf6d09"/></td></tr>
<tr><td> <em>Caption:</em> <p>list of roles<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-24T21.26.33image.png.webp?alt=media&token=475cc4bc-2a48-47b1-a336-39119d7a6179"/></td></tr>
<tr><td> <em>Caption:</em> <p>the details related to it<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/hrithikka/hg345-IS601-007/pull/63">https://github.com/hrithikka/hg345-IS601-007/pull/63</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List entities associated with users </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a page that lists entities that are associated with at least 1 user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-24T21.30.39image.png.webp?alt=media&token=914d9db4-b81f-4990-b805-6bf31bbc4630"/></td></tr>
<tr><td> <em>Caption:</em> <p> entities associated with users<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-24T21.54.09image.png.webp?alt=media&token=7d466bd1-0d6e-42d3-9afc-3516053ab47d"/></td></tr>
<tr><td> <em>Caption:</em> <p> entities associated with users<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/hrithikka/hg345-IS601-007/pull/64">https://github.com/hrithikka/hg345-IS601-007/pull/64</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin Association Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Admin page to search for users and entities</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-24T21.32.17WhatsApp%20Image%202023-12-24%20at%2016.31.59_2e82bee7.jpg.webp?alt=media&token=638fad28-0571-4635-adf6-261f32a8f414"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin Association Page <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-24T21.33.12image.png.webp?alt=media&token=372d56e8-685c-4ed9-8561-766af3130191"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin Association Page <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/hrithikka/hg345-IS601-007/pull/64">https://github.com/hrithikka/hg345-IS601-007/pull/64</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Project Related Screens not yet shown </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of other pages not yet shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-24T21.34.34image.png.webp?alt=media&token=d314f73a-aa7c-497d-b63e-b430c8bc4778"/></td></tr>
<tr><td> <em>Caption:</em> <p>Welcome page of admin<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fhg345%2F2023-12-24T21.35.31image.png.webp?alt=media&token=cc3e7eef-a0df-42b7-8c66-aa7f71c4d032"/></td></tr>
<tr><td> <em>Caption:</em> <p>Welcome page of the normal user<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain each screen shown above</td></tr>
<tr><td> <em>Response:</em> <p>The application comprises three key pages related to Task 1: the Manual Edit<br>Form Page, the API Data Sync Page, and the Admin Privileges Management Page.<br>The Manual Edit Form Page enables users to manually edit their list of<br>favorite horror movies, permitting them to add, remove, and modify movie selections. This<br>page interacts with the application&#39;s database to update user-movie relationships based on user<br>actions. The API Data Sync Page allows users to synchronize their favorite movies<br>with the latest external API data, ensuring that their favorites are always up-to-date.<br>This synchronization process involves comparing and updating local movie records with the most<br>recent information from the API. Lastly, the Admin Privileges Management Page, accessible to<br>administrators only, empowers admins to manage user privileges, including granting and revoking admin<br>status for other users. Admins can also designate new administrators, with these changes<br>reflected in the application&#39;s user database. These pages collectively provide an efficient and<br>user-friendly means of managing movie preferences, ensuring data accuracy, and controlling user access<br>to admin functionalities.<br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/hrithikka/hg345-IS601-007/pull/63">https://github.com/hrithikka/hg345-IS601-007/pull/63</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div><br></div><div>Throughout this milestone, challenges included effective data synchronization with an external API, managing<br>admin privileges, and implementing error handling and validation. Valuable lessons encompassed the importance<br>of robust role-based access control (RBAC), the need for clear error feedback, and<br>the incorporation of user feedback to enhance usability. Security considerations highlighted the necessity<br>of strong authentication mechanisms. These experiences have contributed to a deeper understanding of<br>application development and ongoing improvements.</div><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-3-api-project/grade/hg345" target="_blank">Grading</a></td></tr></table>