import datetime
from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB


import re
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False
donations = Blueprint('donations', __name__, url_prefix='/donations')


@donations.route("/search", methods=["GET"])
def search():
    rows = []
    organization_name = ""
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve donation id as id, donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments, organization_name using a LEFT JOIN
    #hg345 - 12-11-2023
    query = """SELECT DON.id, DON.donor_firstname, DON.donor_lastname, DON.donor_email, ORG.id AS organization_id, DON.item_name, DON.item_description, DON.item_quantity, DON.donation_date, DON.comments, ORG.name AS organization_name
 FROM IS601_MP3_Donations AS DON LEFT JOIN IS601_MP3_Organizations AS ORG ON DON.organization_id = ORG.id WHERE 1=1"""
    args = {} # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["donor_firstname", "donor_lastname", "donor_email", "comments","organization_name" ,"item_name", "item_quantity","donation_date"]
    # TODO search-2 get fn, ln, email, organization_id, column, order, limit from request args
    #hg345 - 12-11-2023
    fn = request.args.get("fn")
    ln = request.args.get("ln")
    email = request.args.get("email")
    org_id = request.args.get("organization_id")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit",10)
    # TODO search-3 append like filter for donor_firstname if provided
    #hg345 - 12-11-2023
    if fn:
        query += " AND donor_firstname LIKE CONCAT('%', %(donor_firstname)s, '%') "
        args["donor_firstname"] = fn
    # TODO search-4 append like filter for donor_lastname if provided
    #hg345 - 12-11-2023
    if ln:
        query += " AND donor_lastname LIKE CONCAT('%', %(donor_lastname)s, '%')"
        args["donor_lastname"] = ln
    # TODO search-5 append like filter for donor_email if provided
    #hg345 - 12-11-2023
    if email:
        query += " AND donor_email LIKE CONCAT('%',%(donor_email)s, '%')"
        args["donor_email"] = email
    # TODO search-6 append like filter for item_name if provided
    #hg345 - 12-11-2023
    item_name = request.args.get("item")
    if item_name:
        query += " AND item_name LIKE %(item_name)s "
        args["item_name"] = item_name
    # TODO search-7 append equality filter for organization_id if provided
    #hg345 - 12-11-2023
    if org_id:
        query += " AND organization_id = %(organization_id)s "
        args["organization_id"] = org_id
    # TODO search-8 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    #hg345 - 12-11-2023
    if column and order and column in allowed_columns and order in ["asc", "desc"]:
        query += f" ORDER BY {column} {order}"
    # TODO search-9 append limit (default 10) or limit greater than 1 and less than or equal to 100
    #hg345 - 12-11-2023
    try:
        
        if 1 <= int(limit) <= 100:
            query += " LIMIT %(limit)s"
            args["limit"] = limit
    # TODO search-10 provide a proper error message if limit isn't a number or if it's out of bounds
    #hg345 - 12-11-2023
        else:
            flash("Limit must be a number between 1 and 100", "error")
    except ValueError:
        flash("Limit must be a valid number", "error")
    
    
    #limit = 10 # TODO change this per the above requirements
    #hg345 - 12-11-2023
    #query += " LIMIT %(limit)s"
    #args["limit"] = limit
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
            print(f"rows: {rows}")
    except Exception as e:
        # TODO search-11 make message user friendly
        flash(f"Error Occured try modifying search:{e}", "error")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    #hg345 - 12-11-2023
    allowed_columns_tup=[(column,column.replace("_"," ").title())for column in allowed_columns]
    # TODO search-12 if request args has organization identifier set organization_name variable to the correct name
    #hg345 - 12-11-2023
    organization_id= request.args.get("organization_id")
    if organization_id:
        organization_name_result = DB.selectOne("SELECT name FROM IS601_MP3_Organizations WHERE id=%(organization_id)s", 
                                                {"organization_id": organization_id})
        if organization_name_result.status:
            organization_name = organization_name_result.row["name"]

    return render_template("list_donations.html", organization_name=organization_name, rows=rows, allowed_columns=allowed_columns_tup)


@donations.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
        #hg345 - 12-11-2023
        donor_firstname = request.form.get("donor_firstname")
        donor_lastname = request.form.get("donor_lastname")
        donor_email = request.form.get("donor_email")
        organization_id = request.form.get("organization_id")
        item_name = request.form.get("item_name")
        item_description = request.form.get("item_description")
        item_quantity = request.form.get("item_quantity")
        donation_date = request.form.get("donation_date")
        comments = request.form.get("comments")
        # TODO add-2 donor_firstname is required (flash proper error message)
        #hg345 - 12-11-2023
        if not donor_firstname:
            flash("Donor First Name Required", "error")
            return render_template("manage_donation.html", donation=request.form)
        # TODO add-3 donor_lastname is required (flash proper error message)
        #hg345 - 12-11-2023
        if not donor_lastname:
            flash("Donor Last Name Required", "error")
            return render_template("manage_donation.html", donation=request.form)
        # TODO add-4 donor_email is required (flash proper error message)
        #hg345 - 12-11-2023
        if not donor_email:
            flash("Donor Email Required", "error")
            return render_template("manage_donation.html", donation=request.form)
        # TODO add-4a email must be in proper format (flash proper message)
        #hg345 - 12-11-2023
        if not is_valid_email(donor_email):  
            flash("Invalid Email-id", "error")
            return render_template("manage_donation.html", donation=request.form)
        # TODO add-5 organization_id is required (flash proper error message)
        #hg345 - 12-11-2023
        if not organization_id:
            flash("Organization ID Required", "error")
            return render_template("manage_donation.html", donation=request.form)
        # TODO add-6 item_name is required (flash proper error message)
        #hg345 - 12-11-2023
        if not item_name:
            flash("Item Name Required", "error")
            return render_template("manage_donation.html", donation=request.form)
        # TODO add-7 item_description is optional
        #hg345 - 12-11-2023
        # TODO add-8 item_quantity is required and must be more than 0 (flash proper error message)
        #hg345 - 12-11-2023
        if not item_quantity or not item_quantity.isdigit() or int(item_quantity) <= 0:
            flash("Item Quantity Required i.e.>0", "error")
            return render_template("manage_donation.html", donation=request.form)

        # TODO add-9 donation_date is required and must be within the past 30 days
        #hg345 - 12-11-2023
        if not donation_date:
            flash("Donation Date Required", "error")
            return render_template("manage_donation.html", donation=request.form)
        try:
            donation_date = datetime.datetime.strptime(donation_date, "%Y-%m-%d").date()
            thirty_days_ago = datetime.datetime.now().date() - datetime.timedelta(days=30)
            if donation_date < thirty_days_ago:
                flash("Donation Date with in past 30 days", "error")
                return render_template("manage_donation.html", donation=request.form)
        except ValueError:
            flash("Invalid Donation Date", "error")
            return render_template("manage_donation.html", donation=request.form)
        # TODO add-10 comments are optional
        #hg345 - 12-11-2023
        has_error = False # use this to control whether or not an insert occurs
        
        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Donations(donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments)
                VALUES (%(donor_firstname)s, %(donor_lastname)s, %(donor_email)s, %(organization_id)s, %(item_name)s, %(item_description)s, %(item_quantity)s, %(donation_date)s, %(comments)s)
                """, {
                    "donor_firstname": donor_firstname,
                    "donor_lastname": donor_lastname,
                    "donor_email": donor_email,
                    "organization_id": organization_id,
                    "item_name": item_name,
                    "item_description": item_description,
                    "item_quantity": item_quantity,
                    "donation_date": donation_date,
                    "comments": comments,
                }) # <-- TODO add-11 add query and add arguments
                #hg345 - 12-11-2023
                if result.status:
                    print("donation record created")
                    flash("Created Donation Record", "success")
            except Exception as e:
                # TODO add-7 make message user friendly
                #hg345 - 12-11-2023
                print(f"insert error {e}")
                flash("Error occurred Creating Donation Record. Please try again.", "danger")
    return render_template("manage_donation.html",donation=request.form)

@donations.route("/edit", methods=["GET", "POST"])
def edit():
    row = {}
    
    # TODO edit-1 request args id is required (flash proper error message)
    #hg345 - 12-11-2023
    #id = False
    donation_id = request.args.get("id")
    #if not id: # TODO update this for TODO edit-1
    if not donation_id:
        flash("Donation ID is missing", "error")
        return redirect(url_for("donations.search"))
        
    else:
        if request.method == "POST":
            
            # TODO add-2 retrieve form data for donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
            #hg345 - 12-11-2023
            donor_firstname = request.form.get("donor_firstname")
            donor_lastname = request.form.get("donor_lastname")
            donor_email = request.form.get("donor_email")
            organization_id = request.form.get("organization_id")
            item_name = request.form.get("item_name")
            item_description = request.form.get("item_description")
            item_quantity = request.form.get("item_quantity")
            donation_date = request.form.get("donation_date")
            comments = request.form.get("comments")
            # TODO add-3 donor_firstname is required (flash proper error message)
            #hg345 - 12-11-2023
            if not donor_firstname:
                flash("Donor First Name Required", "error")
                return render_template("manage_donation.html", donation=request.form)

            # TODO add-4 donor_lastname is required (flash proper error message)
            #hg345 - 12-11-2023
            if not donor_lastname:
                flash("Donor Last Name Required", "error")
                return render_template("manage_donation.html", donation=request.form)
            # TODO add-5 donor_email is required (flash proper error message)
            #hg345 - 12-11-2023
            if not donor_email:
                flash("Donor Email Required", "error")
                return render_template("manage_donation.html", donation=request.form)
            # TODO add-5a email must be in proper format (flash proper message)
            #hg345 - 12-11-2023
            if not is_valid_email(donor_email):  # You need to implement the is_valid_email function
                flash("Invalid Email-ID. Please enter valid email address.", "error")
                return render_template("manage_donation.html", donation=request.form)
            # TODO add-6 organization_id is required (flash proper error message)
            #hg345 - 12-11-2023
            if not organization_id:
                flash("Organization Rrequired", "error")
                return render_template("manage_donation.html", donation=request.form)
            # TODO add-7 item_name is required (flash proper error message)
            #hg345 - 12-11-2023
            if not item_name:
                flash("Item Name Required", "error")
                return render_template("manage_donation.html", donation=request.form)
            # TODO add-8 item_description is optional
            #hg345 - 12-11-2023
            # TODO add-9 item_quantity is required and must be more than 0 (flash proper error message)
            #hg345 - 12-11-2023
            if not item_quantity or not item_quantity.isdigit() or int(item_quantity) <= 0:
                flash("Item Quantity Required i.e.>0", "error")
                return render_template("manage_donation.html", donation=request.form)
            # TODO add-10 donation_date is required and must be within the past 30 days
            #hg345 - 12-11-2023
            if not donation_date:
                flash("Donation Date Required", "error")
                return render_template("manage_donation.html", donation=request.form)
            try:
                donation_date = datetime.datetime.strptime(donation_date, "%Y-%m-%d").date()
                thirty_days_ago = datetime.datetime.now().date() - datetime.timedelta(days=30)
                if donation_date < thirty_days_ago:
                    flash("Donation Date within past 30 days", "error")
                    return render_template("manage_donation.html", donation=request.form)
            except ValueError:
                flash("Invalid Donation Date ex:YYYY-MM-DD", "error")
                return render_template("manage_donation.html", donation=request.form)
            # TODO add-11 comments are optional
            #hg345 - 12-11-2023
            has_error = False # use this to control whether or not an insert occurs
                
            if not has_error:
                try:
                    # TODO edit-12 fill in proper update query
                    #hg345 - 12-11-2023
                    result = DB.update("""
                    UPDATE IS601_MP3_Donations SET
                    donor_firstname = %(donor_firstname)s,
                    donor_lastname = %(donor_lastname)s,
                    donor_email = %(donor_email)s,
                    organization_id = %(organization_id)s,
                    item_name = %(item_name)s,
                    item_description = %(item_description)s,
                    item_quantity = %(item_quantity)s,
                    donation_date = %(donation_date)s,
                    comments = %(comments)s
                    WHERE id = %(id)s
                    """, {
                        "donor_firstname": donor_firstname,
                        "donor_lastname": donor_lastname,
                        "donor_email": donor_email,
                        "organization_id": organization_id,
                        "item_name": item_name,
                        "item_description": item_description,
                        "item_quantity": item_quantity,
                        "donation_date": donation_date,
                        "comments": comments,
                        "id": donation_id,
                    })
                    
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-13 make this user-friendly
                    #hg345 - 12-11-2023
                    print(f"update error {e}")
                    flash("Error occurred Updating Donation Record. Please try again.", "danger")
        
        try:
            # TODO edit-14 fetch the updated data 
            #hg345 - 12-11-2023
            result = DB.selectOne("""SELECT 
            id,donor_firstname, donor_lastname, donor_email, organization_id, item_name, item_description, item_quantity, donation_date, comments
            FROM IS601_MP3_Donations 
            WHERE id = %s
            """, donation_id)
            
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-15 make this user-friendly
            #hg345 - 12-11-2023
            flash("Error occurred Fetching Updated Data. Please try again.", "danger")
    
    return render_template("manage_donation.html", donation=row)

@donations.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 if id is missing, flash necessary message and redirect to search
    #hg345 - 12-11-2023
    donation_id = request.args.get("id")
    if not donation_id:
        flash("Donation ID Missing", "error")
        return redirect(url_for("donations.search"))

    try:
    # TODO delete-2 delete donation by id (fetch the id from the request)
    #hg345 - 12-11-2023
        result = DB.delete("DELETE FROM IS601_MP3_Donations WHERE id = %s", donation_id)
        
        if result.status:
    # TODO delete-3 ensure a flash message shows for successful delete
    #hg345 - 12-11-2023
            flash("Deleted Donation Record", "success")
        else:
            flash("Failed Deleting Donation Record", "error")
    except Exception as e:
        flash(str(e), "danger")
    # TODO delete-4 pass all argument except id to this route
    #hg345 - 12-11-2023
    args = request.args.copy()
    args.pop('id', None)
    # TODO delete-5 redirect to donation search
    #hg345 - 12-11-2023
    return redirect(url_for("donations.search", **args))
