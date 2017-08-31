The assignment is to implement a simple address book library in Python.


Overview
========

* Assignment version: 1.0

* Language: Python

* Type: Library

* Estimated effort needed: 3-4 hours



Requirements
============

Facts:

* A person has a first name and a last name. **DONE**

* A person may have one or more street addresses. **DONE**

>p=PersonOperation()<br>
>p.create_person("aakash","tewari")<br>
>p.add_address_for_user("Some place in world")<br>

* A person may have one or more email addresses. **DONE**
>p.add_email_for_user("Some place in world")<br>

* A person may have one or more phone numbers. **DONE**
>p.add_phone_for_user(['1111111111','2222222222'])<br>

* A person can be a member of one or more groups. **DONE**


* An address book is a collection of persons and groups. **DONE But considered database as single addressbook**


Required features (these need to be unit tested):

* Add a person to the address book. **DONE** 
>p=PersonOperation()<br>
>p.create_person("aakash","tewari")
 
* Add a group to the address book. **DONE**
>p.add_user_to_group('group1')<br>
>p.add_user_to_group('group2')<br>

* Given a group we want to easily find its members.**DONE**
>grp=GroupOperations()
>grp.get_group_member('group1')

* Given a person we want to easily find the groups the person belongs to.**DONE**
>p.get_person_groups()

* Find person by name (can supply either first name, last name, or both).**DONE**
>p.find_person('aakash tewari')<br>
>p.find_person('aakash')<br>
>p.find_person('tewari')<br>


* Find person by email address (can supply either the exact string or a prefix
  string, ie. both "alexander@company.com" and "alex" should work).**DONE**
>p.find_person_by_email('alexander@company.com')<br>
>p.find_person_by_email('alex')<br>



Design-only questions:

* Find person by email address (can supply any substring, ie. "comp" should
  work assuming "alexander@company.com" is an email address in the address
  book) - discuss how you would implement this without coding the solution.**DONE I have used SQL LIKE in this and it works perfectlr=y** 

>p.find_person_by_email_design('comapny')<br>




