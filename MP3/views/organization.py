from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB

import pycountry
organization = Blueprint('organization', __name__, url_prefix='/organization')

@organization.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, donation count as donations for the organization
    # don't do SELECT * and replace the below "..." portion
    #hg345 - 12-11-2023
    allowed_columns = ["name", "city", "country", "state", "modified", "created"]
    query = "SELECT DISTINCT ORG.id, ORG.name, ORG.address, ORG.city, ORG.country,ORG.description ,ORG.state, ORG.zip, ORG.website, ORG.modified, ORG.created FROM IS601_MP3_Organizations AS ORG LEFT JOIN IS601_MP3_Donations AS DON ON ORG.id = DON.organization_id WHERE 1=1"
    args = {} # <--- add values to replace %s/%(named)s placeholders
   
    
    # TODO search-2 get name, country, state, column, order, limit request args
    #hg345 - 12-11-2023
    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit", 10) 
    # TODO search-3 append a LIKE filter for name if provided
    #hg345 - 12-11-2023
    if name:
        query += " AND name LIKE %(name)s "
        args["name"] = f"%{name}%"
    # TODO search-4 append an equality filter for country if provided
    #hg345 - 12-11-2023
    if country:
        query += " AND country = %(country)s "
        args["country"] = f"%{country}%"
    # TODO search-5 append an equality filter for state if provided
    #hg345 - 12-11-2023
    if state:
        query += " AND state = %(state)s "
        args["state"] = f"%{state}%"
    # TODO search-6 append sorting if column and order are provided and within the allows columns and allowed order asc,desc
    #hg345 - 12-11-2023
    if column and order and column in allowed_columns and order in ["asc", "desc"]:
        query += f" ORDER BY {column} {order}"
    # TODO search-7 append limit (default 10) or limit greater than or equal to 1 and less than or equal to 100
    #hg345 - 12-11-2023
    try:
        #limit = int(request.args.get("limit", 10))
        if 1 <= int(limit) <= 100:
            query += f" LIMIT %(limit)s"
            args["limit"] = limit
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    #hg345 - 12-11-2023
        else:
            raise ValueError("Limit number between -> 1 and 100")
    except ValueError as e:
        flash("Invalid limit value. Please provide a proper number between 1 and 100.", "danger")
    limit = 10 # TODO change this per the above requirements
    #hg345 - 12-11-2023
    
    #query += " LIMIT %(limit)s"
    #args["limit"] = limit
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        print(f"result {result.rows}")
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-9 make message user friendly
        #hg345 - 12-11-2023
        flash("Error occurred while fetching the organizations. Please try again.", "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    #hg345 - 12-11-2023
    allowed_columns=[(column,column.replace("_"," ").title())for column in allowed_columns]
    # do this prior to passing to render_template, but not before otherwise it can break validation
    
    return render_template("list_organizations.html", rows=rows, allowed_columns=allowed_columns)


@organization.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        has_error = False # use this to control whether or not an insert occurs
        
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website, description
        #hg345 - 12-11-2023
        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zip_code = request.form.get("zip")
        website = request.form.get("website")
        description = request.form.get("description")
        # TODO add-2 name is required (flash proper error message)
        #hg345 - 12-11-2023
        if not name:
            flash("Name Required", "danger")
            has_error = True

        # TODO add-3 address is required (flash proper error message)
        #hg345 - 12-11-2023
        if not address:
            flash("Address Required", "danger")
            has_error = True
        # TODO add-4 city is required (flash proper error message)
        #hg345 - 12-11-2023
        if not city:
            flash("City Required", "danger")
            has_error = True
        # TODO add-5 state is required (flash proper error message)
        #hg345 - 12-11-2023
        if not state:
            
            flash("State Required", "danger")
            has_error = True
        else:
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation to solve this
        #hg345 - 12-11-2023
            if "US-"+state not in [state_.code for state_ in pycountry.subdivisions.get(country_code=country)]:
                flash("Invalid State Selected", "danger")
                has_error = True    
        # TODO add-6 country is required (flash proper error message)
        #hg345 - 12-11-2023
        if not country:
            flash("Country Required", "danger")
            has_error = True
        else:
        # TODO add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation to solve this
        #hg345 - 12-11-2023
            if country not in [country_.alpha_2 for country_ in pycountry.countries]:
                flash("Invalid Country Selected", "danger")
                has_error = True
        # TODO add-7 website is not required
        #hg345 - 12-11-2023

        # TODO add-8 zip is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
        #hg345 - 12-11-2023
        if not zip_code:
            flash("ZIP Code Required", "danger")
            has_error = True
        # TODO add-9 description is not required
        #hg345 - 12-11-2023

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Organizations (name, address, city, state, country, zip, website, description)
                VALUES (%(name)s, %(address)s, %(city)s, %(state)s, %(country)s, %(zip)s, %(website)s, %(description)s)
                """, {"name": name, "address": address, "city": city, "state": state, "country": country,
                      "zip": zip_code, "website": website, "description": description}) # <-- TODO add-10 add query and add arguments
                #hg345 - 12-11-2023
                
                if result.status:
                    flash("Organization Added Successfully", "success")
            except Exception as e:
                # TODO add-11 make message user friendly
                #hg345 - 12-11-2023
                flash("Failed to add the organization. Please try again.", "danger")
        
    return render_template("manage_organization.html", org=request.form)

@organization.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    #hg345 -  12-11-2023
    id = request.args.get("id")
    if not id: # TODO update this for TODO edit-1
        flash("Organization ID Required", "danger")
        return redirect(url_for("organization.search"))
    
    if request.method == "POST":
        data = {"id": id} # use this as needed, can convert to tuple if necessary
        # TODO edit-2 retrieve form data for name, address, city, state, country, zip, website
        #hg345 - 12-11-2023

        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zip_code = request.form.get("zip")
        website = request.form.get("website")
        
        # TODO edit-3 name is required (flash proper error message)
        #hg345 - 12-11-2023
        if not name:
            flash("Name Required", "danger")
            return redirect(url_for("organization.edit", id=id))
        # TODO edit-4 address is required (flash proper error message)
        #hg345 - 12-11-2023
        if not address:
            flash("Address Required", "danger")
            return redirect(url_for("organization.edit", id=id))
        # TODO edit-5 city is required (flash proper error message)
        #hg345 - 12-11-2023
        if not city:
            flash("City Required", "danger")
            return redirect(url_for("organization.edit", id=id))
        # TODO edit-6 state is required (flash proper error message)
        #hg345 - 12-11-2023
        if not state:
            flash("State Required", "danger")
            return redirect(url_for("organization.edit", id=id))
        else:
        # TODO edit-6a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation
        #hg345 - 12-11-2023
            print([state_.code for state_ in pycountry.subdivisions.get(country_code=country)])
            if "US-"+state not in [state_.code for state_ in pycountry.subdivisions.get(country_code=country)]:
                flash("Invalid State Selected", "danger")
                return redirect(url_for("organization.edit", id=id))
        # TODO edit-7 country is required (flash proper error message)
        #hg345 - 12-11-2023
        if not country:
            flash("Country Required", "danger")
            return redirect(url_for("organization.edit", id=id))
        else:
        # TODO edit-7a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation
        #hg345 - 12-11-2023
            if country not in [country_.alpha_2 for country_ in pycountry.countries]:
                flash("Invalid Country Selected", "danger")
                return redirect(url_for("organization.edit", id=id))
        # TODO edit-8 website is not required
        #hg345 - 12-11-2023
        # TODO edit-9 zipcode is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues
         #hg345 - 12-11-2023
        if not zip_code:
            flash("ZIP Code Required", "danger")
            return redirect(url_for("organization.edit", id=id))
        # populate data dict with mappings
        #hg345 - 12-11-2023

        has_error = False # use this to control whether or not an insert occurs

        if not has_error:
            try:
                # TODO edit-10 fill in proper update query
                # name, address, city, state, country, zip, website
                 #hg345 - 12-11-2023
                result = DB.update("""
                UPDATE IS601_MP3_Organizations
                SET name = %(name)s, address = %(address)s, city = %(city)s, state = %(state)s,
                    country = %(country)s, zip = %(zip)s, website = %(website)s
                WHERE id = %(id)s
                """, {"name": name, "address": address, "city": city, "state": state,
                      "country": country, "zip": zip_code, "website": website, "id": id})
                    
                if result.status:
                    print("updated record")
                    flash("Updated Record", "success")
            except Exception as e:
                # TODO edit-11 make this user-friendly
                 #hg345 - 12-11-2023
                print(f"{e}")
                flash("Failed Updating Organization. Please try again.", "danger")
    row = {}
    try:
        # TODO edit-12 fetch the updated data
         #hg345 - 12-11-2023
        result = DB.selectOne("SELECT * FROM IS601_MP3_Organizations WHERE id = %(id)s", {"id": id})
        if result.status:
            row = result.row
                
    except Exception as e:
            # TODO edit-13 make this user-friendly
             #hg345 - 12-11-2023
        flash("Failed fetching Organization Data. Please try again.", "danger")
    
    return render_template("manage_organization.html", org=row)

@organization.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 if id is missing, flash necessary message and redirect to search
    #hg345 - 12-11-2023
    id = request.args.get("id")
    if not id:
        flash("Organization ID Required", "danger")
        return redirect(url_for("organization.search"))

    try:
    # TODO delete-2 delete organization by id (note: you'll likely need to trigger a delete of all donations related to this organization first due to foreign key constraints)
    #hg345 - 12-11-2023
        result = DB.delete("DELETE FROM IS601_MP3_Organizations WHERE id = %(id)s", {"id": id})
        print(result)
        if result.status:
    # TODO delete-3 ensure a flash message shows for successful delete
    #hg345 - 12-11-2023
            flash("Deleted Organization successfully", "success")
        else:
            flash("Failed Deleting Organization. Please try again.", "danger")

    except Exception as e:
    # TODO delete-4 pass all argument except id to this route
    #hg345 - 12-11-2023
        flash("Failed Deleting Organization. Please try again.", "danger")

    # TODO delete-5 redirect to organization search
    #hg345 - 12-11-2023
    return redirect(url_for("organization.search"))