# MongoDB Transaction Analyzer
FSU COP4064: Application Development with Non-Traditional Databases Project with Dr. Karen Works

<h2>Description</h2>
This project simulates a backend data application by creating and managing a MongoDB database using Python, with support for CRUD-style operations such as adding and viewing records. It features a menu-driven interface and robust input validation to ensure consistent and accurate data handling.


<h2>Languages and Utilities Used</h2>

- <b>Python</b>
- <b>MongoDB</b>
- <b>MongoClient via Pymongo</b>

<h2>Environments Used </h2>

- <b>PyCharm</b>

<h2>Program walk-through:</h2>

<p align="center">
With a local MongoDB server running, run DBCreate.py. JSON data is hardcoded into DBCreate.py, so there is no need for the sample_analytics data. Below is the expected output: <br/>
*********************************************
USING transactions.json FROM sample_analytics
*********************************************

_id 			 <class 'bson.objectid.ObjectId'> 			 69e843824edace9e89e897f1
account_id 			 <class 'str'> 			 191983839
transaction_count 			 <class 'int'> 			 652
bucket_start_date 			 <class 'str'> 			 2022-05-13T00:00:00.000+00:00
bucket_end_date 			 <class 'str'> 			 2023-12-27T00:00:00.000+00:00
transactions 			 <class 'dict'> 			 {'date': '20025-10-5T00:00:00.000+00:00', 'amount': '37', 'transaction_code': 'nontradDBproj', 'symbol': 'amg', 'price': 8.9, 'total': 10}
Sub Object:
			date 			 <class 'str'> 			 20025-10-5T00:00:00.000+00:00
			amount 			 <class 'str'> 			 37
			transaction_code 			 <class 'str'> 			 nontradDBproj
			symbol 			 <class 'str'> 			 amg
			price 			 <class 'float'> 			 8.9
			total 			 <class 'int'> 			 10
***************
limit attributes
account_id
191983839                      		 652 		 2022-05-13T00:00:00.000+00:00 		 2022-05-13T00:00:00.000+00:00
204882912                      		 418 		 2021-03-02T00:00:00.000+00:00 		 2021-03-02T00:00:00.000+00:00
177492001                      		 973 		 2020-09-15T00:00:00.000+00:00 		 2020-09-15T00:00:00.000+00:00
199820776                      		 211 		 2022-01-10T00:00:00.000+00:00 		 2022-01-10T00:00:00.000+00:00
185678422                      		 540 		 2021-07-05T00:00:00.000+00:00 		 2021-07-05T00:00:00.000+00:00
200115334                      		 864 		 2022-10-23T00:00:00.000+00:00 		 2022-10-23T00:00:00.000+00:00
178943555                      		 327 		 2021-12-30T00:00:00.000+00:00 		 2021-12-30T00:00:00.000+00:00
196412980                      		 745 		 2020-06-09T00:00:00.000+00:00 		 2020-06-09T00:00:00.000+00:00
209887641                      		 589 		 2021-11-25T00:00:00.000+00:00 		 2021-11-25T00:00:00.000+00:00
175554229                      		 680 		 2022-03-18T00:00:00.000+00:00 		 2022-03-18T00:00:00.000+00:00
***************
sort ascending and descending
account_id
209887641                      		 589
204882912                      		 418
200115334                      		 864
199820776                      		 211
196412980                      		 745
191983839                      		 652
185678422                      		 540
178943555                      		 327
177492001                      		 973
175554229                      		 680
***************
limit rows
account_id
191983839                      		 652 		 2022-05-13T00:00:00.000+00:00 		 2022-05-13T00:00:00.000+00:00
***************
limit rows and columns
account_id
191983839                      		 652 		 2022-05-13T00:00:00.000+00:00
***************
sort by one
account_id
175554229                      		 680
191983839                      		 652
209887641                      		 589
185678422                      		 540
204882912                      		 418
178943555                      		 327
199820776                      		 211
Disconnected from MongoDB

Process finished with exit code 0
<br />
<br />
Search for a camera body. Here, I searched for names like 'n':  <br/>
<img src="https://i.imgur.com/OErn4ZA.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Select 'Add Camera' and add a new record to the database: <br/>
<img src="https://i.imgur.com/ebYaI5Z.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Select View on the Cameras page to see the new entry to update or delete:  <br/>
<img src="https://i.imgur.com/2mNTNZx.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
